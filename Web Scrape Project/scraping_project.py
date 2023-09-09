import requests
from bs4 import BeautifulSoup
import random

def play_game():
    num_guesses = 4
    quotes = make_url_request()
    random_quote = random.choice(quotes)

    while num_guesses > 0:
        if num_guesses == 4:
            print("Can you guess is the author behind the following quote?")
            print(random_quote["text"])
        if num_guesses == 3:
            print("Here's a hint:")
            print(random_quote["bio_link"])
        answer = input()
        if answer == random_quote["author"]:
            print("Well done! You guessed it.")
            num_guesses = 0
        else:
            num_guesses -= 1

        if num_guesses == 0:
            print("Do you want to play again (y/n)?")
            play_again = input()
            if play_again == "y":
                print("Alright, lets go again.")
                num_guesses = 4
                random_quote = random.choice(quotes)
            else:
                print("Thanks for playing.")
                break

# def get_author_bio():
#     url = 

def make_url_request():
    url = "http://quotes.toscrape.com"
    response = requests.get(url, headers={"Accept": "application/json"})
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    next_page = soup.find(class_="next")

    if next_page:
        next_page_href = next_page.contents[1]['href']

    quotes_data = []
    while next_page:
        for quote in quotes:
            quotes_data.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio_link": quote.find("a")["href"]
            })
        
        next_url = url + next_page_href
        response = requests.get(next_url, headers={"Accept": "application/json"})
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        next_page = soup.find(class_="next")

        if next_page:
            next_page_href = next_page.contents[1]['href']
        

    return quotes_data

play_game()