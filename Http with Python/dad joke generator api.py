import requests

def obtain_jokes(query_term):
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(
        url,
        headers={"Accept": "application/json"}
    )

    data = response.json()
    if len(data) == 0:
        return f"Sorry I got no jokes about {query_term}"
    elif len(data) == 1:
        selected_joke = data.results[0]
        return f"I got one joke for you about {query_term}, here is it: \n {selected_joke}"
    else:
        selected_joke = data.results[1]
        return f"I have several jokes about {query_term}, let me tell you one of them. \n {selected_joke}"

joke_topic = input("Let me tell you a joke. Give me a topic.")
print(obtain_jokes(joke_topic))