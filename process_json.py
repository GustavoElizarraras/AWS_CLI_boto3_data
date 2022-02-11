import json

with open("issues_data.json", "r") as f:
    data = json.load(f)
    for issue in data["closed_issues"]:
        issue["labels"] = [label["name"] for label in issue["labels"]]
    for issue in data["open_issues"]:
        issue["labels"] = [label["name"] for label in issue["labels"]]
    with open("aws_cli_issues.json", "w") as pf:
        json.dump(data, pf, ensure_ascii=True, indent=4)
