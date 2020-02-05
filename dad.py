import termcolor
import pyfiglet
import requests
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="green")
print(header)

term = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers={"Accept": "application/json"},
	params={"term": term}
).json()
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} about: {term}. Here's one")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"There is one joke about: {term} ")
	print(res["results"][0]['joke'])
else:
	print(f"Sorry, coundn't find your search term: {term}")