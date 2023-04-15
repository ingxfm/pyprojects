import requests
import os
import datetime as dt

PIXELA_ENDPOINT: str = "https://pixe.la/v1/users"
PIXELA_USER: str = os.environ["PIX_USER"]
PIXELA_KEY = os.environ["PIX_KEY"]
PIXELA_PARAMS: dict = {
    "token": PIXELA_KEY,
    "username": PIXELA_USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# This next line was used to create my user. It is no longer needed, unless I need another user/pass.
# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMS)
# print(response.text)

GRAPH_ENDPOINT: str = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"
graph_id: str = "graph01"

graph_config: dict = {
    "id": graph_id,
    "name": "Habit graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

headers: dict = {
    "X-USER-TOKEN": PIXELA_KEY,
}

# the graph was already created, so we can comment this next line of code
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime.today().date().strftime("%Y%m%d")


POST_PIXEL_ENDPOINT: str = f"{GRAPH_ENDPOINT}/{graph_id}"

# pixel_config: dict = {
#     "date": today,
#     "quantity": "26",
# }

# a pixel was posted, I can go ahead to the next step
# response_pixel = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(response_pixel.text)

date_to_change = "22020311"
yesterday = (dt.datetime.today() - dt.timedelta(days=1)).date().strftime("%Y%m%d")

# PUT_PIXEL_ENDPOINT: str = f"{POST_PIXEL_ENDPOINT}/{yesterday}"
# pixel_put_config: dict = {
#     "quantity": "27",
# }
# Here is updating, let's go to the next step
# update_pixel = requests.put(url=PUT_PIXEL_ENDPOINT, json=pixel_put_config, headers=headers)

DELETE_PIXEL_ENDPOINT: str = f"{POST_PIXEL_ENDPOINT}/{today}"

delete_pixel = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(delete_pixel.text)
