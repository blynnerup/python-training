import requests
from bs4 import BeautifulSoup
import random

def make_url_request():
    url = "http://quotes.toscrape.com"
    response = requests.get(url, headers={"Accept": "application/json"})
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    quotes_data = []
    for quote in quotes:
        quotes_data.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio_link": quote.find("a")["href"]
        })
    print(random.choice(quotes_data)["text"])



make_url_request()