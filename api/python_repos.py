import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:starts+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code : {r.status_code}")

response_dict = r.json()
print(response_dict.keys())

repo_dicts = response_dict['items']
print(f"repositories returned: {len(repo_dicts)}")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

repo_dicts = repo_dicts[0]
print(f"\nkeys: {len(repo_dicts)}")

for key in sorted(repo_dicts.keys()):
    print(key)



