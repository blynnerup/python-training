import requests

def obtain_jokes(query_term):
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": query_term}
    ).json()

    if len(response) == 0:
        return f"Sorry I got no jokes about {query_term}"
    elif len(response) == 1:
        selected_joke = response["results"][0]["joke"]
        return f"I got one joke for you about {query_term}, here is it: \n{selected_joke}"
    else:
        selected_joke = response["results"][1]["joke"]
        return f"I have several jokes about {query_term}, let me tell you one of them. \n{selected_joke}"

joke_topic = input("Let me tell you a joke. Give me a topic.\n")
print(obtain_jokes(joke_topic))