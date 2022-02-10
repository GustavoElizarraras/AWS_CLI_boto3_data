import requests

response1 = requests.get("https://api.github.com/repos/aws/aws-cli/labels?&per_page=100").json()
labels1 = [label["name"] for label in response1]
response2 = requests.get("https://api.github.com/repos/aws/aws-cli/labels?&per_page=100&page=2").json()
labels2 = [label["name"] for label in response2]
all_labels = [*labels1, *labels2]

print(len(all_labels))