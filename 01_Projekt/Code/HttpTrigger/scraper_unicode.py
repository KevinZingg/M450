from bs4 import BeautifulSoup
import requests
import re

def get_website_info():


    url = "https://www.whois.com/whois/siemens.com"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    x = re.findall("[a-m]", result.text)
    print(x)

get_website_info()

