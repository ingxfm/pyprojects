import requests
import os

SHEETY_ENDPOINT = os.environ["SH_URL"]
SHEETY_KEY = os.environ["SH_KEY"]
SHEETY_PARAMETERS = {}
SHEETY_HEADERS = {
    "Authorization": os.environ["SH_KEY"],
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.cities = []
        self.ids = []
        self.iatas = []
        self.get_response_from_sheety()

    def get_response_from_sheety(self):
        response_sheety_get = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        response_sheety_get.raise_for_status()
        cities_dict_list = response_sheety_get.json()["prices"]
        self.cities = [item["city"] for item in cities_dict_list]
        self.ids = [item["id"] for item in cities_dict_list]
        self.iatas = [item["iataCode"] for item in cities_dict_list]

    def update_rows_to_sheet(self, city_code_list: list):
        for item in range(len(city_code_list)):
            sheety_put_config = {
                "price": {
                    "iataCode": city_code_list[item],
                }
            }
            if self.iatas[item] == "":
                response_sh_put = requests.put(url=f"{SHEETY_ENDPOINT}/{self.ids[item]}",
                                               json=sheety_put_config,
                                               headers=SHEETY_HEADERS)
