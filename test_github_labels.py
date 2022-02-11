import requests
import csv

response1 = requests.get("https://api.github.com/repos/boto/boto3/labels?&per_page=100").json()
boto1 = [label["name"] for label in response1]
response2 = requests.get("https://api.github.com/repos/boto/boto3/labels?&per_page=100&page=2").json()
boto2 = [label["name"] for label in response2]
boto3_labels = [*boto1, *boto2]

response3 = requests.get("https://api.github.com/repos/aws/aws-cli/labels?&per_page=100").json()
cli1 = [label["name"] for label in response3]
response4 = requests.get("https://api.github.com/repos/aws/aws-cli/labels?&per_page=100&page=2").json()
cli2 = [label["name"] for label in response4]
cli_labels = [*cli1, *cli2]

with open("cli_labels.txt", "w", newline="") as f:
    f.write("\n".join(cli_labels))

with open("boto3_labels.txt", "w", newline="") as f:
    f.write("\n".join(boto3_labels))
