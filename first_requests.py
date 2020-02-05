import requests
url = "http://www.google.com"
res = requests.get(url)

print(f"Your request to {url} came by w/ status code {requests.status_code} ")