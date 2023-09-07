import requests
from bs4 import BeautifulSoup
import random

def play_game():
    num_guesses = 4
    selected_quote = make_url_request()

    while num_guesses > 0:
        if num_guesses == 4:
            print("Can you guess is the author behind the following quote?")
            print(selected_quote["text"])
        if num_guesses == 3:
            print("Here's a hint:")
            print(selected_quote["bio_link"])
        answer = input()
        if answer == selected_quote["author"]:
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
                selected_quote = make_url_request()
            else:
                print("Thanks for playing.")
                break

def make_url_request():
    url = "http://quotes.toscrape.com"
    response = requests.get(url, headers={"Accept": "application/json"})
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    num_guesses = 4

    quotes_data = []
    for quote in quotes:
        quotes_data.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio_link": quote.find("a")["href"]
        })

    return random.choice(quotes_data)

play_game()