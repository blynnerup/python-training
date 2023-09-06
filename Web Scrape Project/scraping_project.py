import requests
from bs4 import BeautifulSoup

def make_url_request():
    url = "http://quotes.toscrape.com"

    response = requests.get(url, headers={"Accept": "application/json"})
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    return quotes



print(make_url_request())