import requests as req
from typing import List
from bs4 import BeautifulSoup as beauty

URL = "https://getdistributors.com/subcategories_sitemap.xml"
FIELD_NAME = "loc"

def soup_parse(data:str,format_:str = "lxml")->List[str]:
    """
        function to parse the text as xml
    """
    soup = beauty(data, features="xml")
    soup.prettify()

    return [x.get_text() for x in soup.find_all(FIELD_NAME)]

def fetch_site_map_urls(url, field_name):
    try:
        resp = req.get(url)
        if resp.status_code == 200:
            return soup_parse(resp.text,field_name)
        return "Couldn't load sitemap"
    except Exception as e:
        raise e
        return "Check internet connection"


print("STATUS_CODE, URL")
def check_url(url):
    resp = req.get(url)
    print(resp.status_code, url, sep=",")

if __name__ == "__main__":
    for url in fetch_site_map_urls(url=URL,field_name=FIELD_NAME):
        check_url(url)