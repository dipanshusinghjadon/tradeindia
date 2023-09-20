from sys import argv
import csv
import random

URL = argv[1] if len(argv) > 1 else "https://www.tradeindia.com/fp_sitemap7.xml"
LIMIT = int(argv[2]) if len(argv) > 2 else 50

from bs4 import BeautifulSoup as soup
from lxml import etree
import re
import requests  as req

REPORT_FIELDS = ["URL", "STATUS_CODE", "COMMENT", "ERROR"]

def check_url(url):
    report = {"URL":url,"ERROR":"NO ERROR"}
    try:
        response = req.get(url)
    except Exception as e:
        response
    else:

        report['STATUS_CODE'] = response.status_code
        if response.status_code == 200:
            report['COMMENT'] = "GOOD"
        else:
            report['ERROR'] = response.text
            report['COMMENT'] = "BAD"
    
    return report
        
    
    
if __name__ == "__main__":
    
    markup = req.get(URL).text
    soup = soup(markup,features="xml")

    urls = soup.select('loc')

    all_urls = [u.text for u in urls]

    random.shuffle(all_urls)


    file_pointer = open("./report.csv","w")
    
    writer = csv.DictWriter(file_pointer,fieldnames=REPORT_FIELDS)
    writer.writeheader()
    
    for x in all_urls[:LIMIT]:
        report = check_url(x)
        writer.writerow(report)
    
    file_pointer.close()

    print("REPORT GENERATED")
    