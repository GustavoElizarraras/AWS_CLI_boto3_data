import requests
from requests.auth import HTTPBasicAuth
import json


closed_issues_data = []

for j in range(1, 100):
    try:
        response = requests.get(f"https://api.github.com/repos/aws/aws-cli/issues?state=closed&per_page=100&page={j}").json()
        for data in response:
            if "pull_request" not in data.keys():
                issue_data = {"title": data["title"], "body": data["body"], "labels": data["labels"]}
                closed_issues_data.append(issue_data)
    except Exception as e:
        print(e)
        break

open_issues_data = []

for j in range(1, 100):
    try:
        response = requests.get(f"https://api.github.com/repos/aws/aws-cli/issues?per_page=100&page={j}").json()
        for data in response:
            if "pull_request" not in data.keys():
                issue_data = {"title": data["title"], "body": data["body"], "labels": data["labels"]}
                open_issues_data.append(issue_data)
    except Exception as e:
        print(e)
        break


issues_data_for_json = {"closed_issues": closed_issues_data, "open_issues": open_issues_data}


with open('issues_data.json', 'w', encoding='utf-8') as f:
    json.dump(issues_data_for_json, f, ensure_ascii=True, indent=4)