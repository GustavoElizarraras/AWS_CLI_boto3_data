import requests

response = requests.get("https://api.github.com/repos/aws/aws-cli/issues").json()
print(response)
# for data in response:
#         print("nooooo")
    # print(data["pull_request"])
# i = 0
# for j in range(1, 1000):
#     try:
#         response = requests.get(f"https://api.github.com/repos/aws/aws-cli/issues?page={j}").json()
#         for data in response:
#             if "pull_request" in data.keys():
#                 i += 1
#     except:
#         break
# print(i)