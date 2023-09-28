import urllib
from urllib import parse

parsed_url = urllib.parse.urlparse('https://www.example.com/page.html')

print(parsed_url)
print(parsed_url.netloc)

def custom_sum(a, b):
    summe = a + b
    print(summe)
    return summe

a = 3
b = 3

custom_sum(a, b)
