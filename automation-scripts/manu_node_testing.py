import psycopg2, time, requests as req
SQL = """
    select fmtd_filename_kw from general.seo_keyword_master;
"""

PROD_URL = "https://api.tradeindia.com/manufacturers/manufacturers/single-api?url={URL}&page=1&per_page=28&current_page=1&top_rated_seller_limit=5&top_rated_product_limit=10&testimonial_limit=10&complete_url={URL}"

DEV2_URL = "https://api-preprod.tradeindia.com/manufacturers/manufacturers/single-api?url={URL}&page=1&per_page=28&current_page=1&top_rated_seller_limit=5&top_rated_product_limit=10&testimonial_limit=10&complete_url={URL}"

# SQL = """
#     SELECT * FROM mykhata.bank_details limit 1;
# """
connection = dict(
    database="tradein_clients",
    user="tradein_dev",
    password="ti_hacker",
    host="127.0.0.1",
    port="3433"
)

with psycopg2.connect(**connection) as conn:
    cursor = conn.cursor()
    cursor.execute(SQL)
    keywords = cursor.fetchall()

columns =['sno'] + ["dev2_"+col for col in "url status_code response_time count response".split()]
columns += ["prod_"+col for col in "url status_code count response".split()]

print(*columns,sep=",")
# print(keywords)
def get_stats(sno, url):
    sno += 1
    dev2_complete_url = DEV2_URL.format_map(dict(URL=url))
    prod_complete_url = PROD_URL.format_map(dict(URL=url))
    dev2_stats = {}
    prod_stats = {}
    dev2_resp = prod_resp = None
    dev2_stats['url'] = dev2_complete_url
    prod_stats['url'] = prod_complete_url
    
    ############### GETTING STATS FOR DEV2 ######################
    try:

        try:
            dev2_resp = req.get(dev2_complete_url)
        except Exception:
            raise TypeError("Node response failed")

        try:
            prod_resp = req.get(prod_complete_url)
        except Exception:
            raise ValueError("Live response failed")

    except TypeError as e:
        dev2_stats['response'] = f'UNABLE TO CALL THE API --> {str(e)}'
        dev2_stats['status_code'] = 'FAILED'
        dev2_stats['count'] = 0
    except ValueError as e:
        prod_stats['response'] = f'UNABLE TO CALL THE API --> {str(e)}'
        prod_stats['status_code'] = 'FAILED'
        prod_stats['count'] = 0

    else:
        if dev2_resp.status_code == prod_resp.status_code and dev2_resp.status_code == 200 and prod_resp.status_code == 200:
        # if dev2_resp.status_code == 200:
            json_data = dev2_resp.json()
            count = json_data['listing_data']['listing_data']['listing_count']
            dev2_stats['count'] = count
            dev2_stats['status_code'] = 200
            dev2_stats['response'] = 'SUCCESS'
        else:
            dev2_stats['status_code'] = dev2_resp.status_code
            dev2_stats['response'] = dev2_resp.text
            dev2_stats['count'] = 0

        if prod_resp.status_code == 200:
            json_data = prod_resp.json()
            count = json_data['listing_data']['listing_data']['listing_count']
            prod_stats['count'] = count
            prod_stats['status_code'] = 200
            prod_stats['response'] = 'SUCCESS'
        else:
            prod_stats['status_code'] = prod_resp.status_code
            prod_stats['response'] = prod_resp.text
            prod_stats['count'] = 0
        

    
    ############### GETTING STATS FOR PROD ######################
    # try:
    #     prod_resp = req.get(prod_complete_url)

    # except Exception as e:
    #     prod_stats['response'] = f'UNABLE TO CALL THE API --> {str(e)}'
    #     prod_stats['status_code'] = 'FAILED'
    #     prod_stats['count'] = 0
    # else:
    #     if prod_resp.status_code == 200:
    #         json_data = prod_resp.json()
    #         count = json_data['listing_data']['listing_data']['listing_count']
    #         prod_stats['count'] = count
    #         prod_stats['status_code'] = 200
    #         prod_stats['response'] = 'SUCCESS'
    #     else:
    #         prod_stats['status_code'] = prod_resp.status_code
    #         prod_stats['response'] = prod_resp.text
    #         prod_stats['count'] = 0

    print(
        sno,
        dev2_stats['url'],
        dev2_stats['status_code'],
        dev2_resp.elapsed.total_seconds() if dev2_resp else "No Response",
        dev2_stats['count'],
        dev2_stats['response'],
        sep=",",
        end=","
    )

    print(
        prod_stats['url'],
        prod_stats['status_code'],
        prod_stats['count'],
        prod_stats['response'],
        sep=",",
    )


def main():
    for sno,mcat in enumerate(keywords):
        keyword = mcat[0]
        url = f"/manufacturers/{keyword}.html"
        get_stats(sno,url)
        if sno == 2:
            break

if __name__ == '__main__':
    main()
    


    

    