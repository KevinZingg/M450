import requests
import csv
from io import StringIO
import urllib
from urllib import parse

class web_scraper_urlhaus:

    all_urls = set()

    def get_all_urls(self):
        self._get_data_csv()
        self._get_data_hostfile()
        self._get_data_text()
        web_scraper_urlhaus.all_urls = set(self.all_urls)
        return web_scraper_urlhaus.all_urls

    def _get_data_csv(self):
        url = "https://urlhaus.abuse.ch/downloads/csv_online/"

        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            csv_content = "\n".join(line for line in content.split("\n") if not line.startswith('#'))

            csv_reader = csv.reader(StringIO(csv_content), delimiter=',', quotechar='"')
            for row in csv_reader:
                parsed_url = urllib.parse.urlparse(row[2])
                self.all_urls.add(parsed_url.netloc)
        else:
            print(f"Error :( : {response.status_code}")

    def _get_data_hostfile(self):
        url = "https://urlhaus.abuse.ch/downloads/hostfile/"

        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            hostfile_content = "\n".join(line for line in content.split("\n") if not line.startswith('#'))

            urls = [line.split('\t')[1].replace("\r", "").replace("127.0.0.1\t", "") for line in
                    hostfile_content.split("\n") if '\t' in line]
            for url in urls:
                self.all_urls.add(url)
        else:
            print(f"Error :( : {response.status_code}")

    def _get_data_text(self):
        url = "https://urlhaus.abuse.ch/downloads/text/"

        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            filtered_lines = {line.replace("\r", "") for line in content.split("\n") if not line.startswith('#')}

            for line in filtered_lines:
                parsed_url = urllib.parse.urlparse(line)
                self.all_urls.add(parsed_url.netloc)
        else:
            print(f"Error :( : {response.status_code}")


scraper = web_scraper_urlhaus()
scraper.get_all_urls()
print(web_scraper_urlhaus.all_urls)
