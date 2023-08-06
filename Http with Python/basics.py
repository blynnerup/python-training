import requests

url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(url, headers={"Accept": "application/json"})

print(response.text)
print(response.json())