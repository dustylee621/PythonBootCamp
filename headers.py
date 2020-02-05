import requests

url = "https://icanhazdadjoke.com/search"


response = requests.get(url, headers={"Accept": "text/json"})

data = response.json()

print(data["joke"])
print(f"status: {data['status']}")