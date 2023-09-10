import requests
from bs4 import BeautifulSoup
import random

def play_game():
    num_guesses = 4
    quotes = make_url_request()
    random_quote = random.choice(quotes)

    while num_guesses > 0:
        if num_guesses == 4:
            print("Can you guess who is the author behind the following quote?")
            print(random_quote["text"])
        if num_guesses == 3:
            print("Here's a hint:")
            hints = get_author_bio(random_quote["bio_link"])
            print("The author was born " + hints["born"])
        if num_guesses == 2:
            print("Maybe some information about the author will help, author initials are: ")
            names = random_quote["author"].split(" ")
            initials = ""
            for name in names:
                if initials == "":
                    initials = name[0] + "."
                else:    
                    initials = initials + " " + name[0] +"."
            print(initials)
        if num_guesses == 1:
            print(hints["description"])
        answer = input()
        if answer == random_quote["author"]:
            print("Well done! You guessed it.")
            num_guesses = 0
        else:
            print("Incorrect sorry.")
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

def get_author_bio(quote_link):
    url = "http://quotes.toscrape.com" + quote_link
    response = requests.get(url, headers={"Accept": "application/json"})
    soup = BeautifulSoup(response.text, "html.parser")
    born = soup.find(class_="author-born-date").text
    born = born + " " + soup.find(class_="author-born-location").text
    bio_description = soup.find(class_="author-description").text

    return {
        "born": born,
        "description": bio_description
    }

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