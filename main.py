import requests
import datetime as dt

date_now = dt.datetime.now().strftime("%Y%m%d")

TOKEN = ""
USERNAME = ""
ID = "taskgraph"
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN,
}
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=params)
print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
print(graph_endpoint)

params_graph = {
    "id": ID,
    "name": "Task Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

response_graph = requests.post(url=graph_endpoint, json=params_graph, headers=headers)

post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{ID}'

params_point = {
    "date": f"{date_now}",
    "quantity": "1"
}

response_post = requests.post(url=post_endpoint, json=params_point, headers=headers)
print(response_post.text)
