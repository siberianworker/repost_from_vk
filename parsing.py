import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
url = "https://m.vk.com/public216440909"

response = requests.get(url)

print(response)