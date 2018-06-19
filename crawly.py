# crawly
import requests
from bs4 import BeautifulSoup
import datetime
import csv
import sys

def cert_crawler():
    url = "https://www.us-cert.gov/ncas/bulletins/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for issue_no in soup.findAll('span', {"class" : "document_id"}):
        issue_no = int(issue_no.string.replace(" ","")[5:8])
        if 155 <= issue_no <= 400:
            issue_no += 6
            link_to_crawl = url + "SB18-" + str(issue_no)
            # print(link_to_crawl)
        # else:
        #     pass
        # ltc = requests.get(link_to_crawl).text
        # ltc_soup = BeautifulSoup(ltc, "html.parser")
        # for test_validity in ltc_soup.findAll('article', {"class": "id"}):
        #     print(test_validity.text)
        
            # if go_parse.text == "There are no bulletins currently available for this year":
            #     pass
            # else:
            #     print(link_to_crawl)

    # for vuln_name in soup.findAll('td', {'class': 'vendor-product'}):
    #     vuln_name = vuln_name.text
    #     print(vuln_name)

cert_crawler()
