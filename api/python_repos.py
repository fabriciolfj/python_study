import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:starts+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code : {r.status_code}")

response_dict = r.json()
print(response_dict.keys())