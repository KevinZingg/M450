from bs4 import BeautifulSoup
import requests

def get_website_info(website):
    url = "https://www.whois.com/whois/" + website
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")


    def extract_data(label, value):
        data_dict = {}
        for i in range(min(len(label), len(value))):
            label_text = label[i].get_text(strip=True)
            value_text = value[i].get_text(strip=True)
            data_dict[label_text] = value_text
            print(f"datadict: {data_dict[label_text]}")
        return data_dict

    label = doc.find_all("div", {"class": "df-label"})
    value = doc.find_all("div", {"class": "df-value"})

    return extract_data(label, value)
