# built-in modules
import os
from datetime import datetime, timedelta

# 3rd-party modules
import requests


# endpoints
KIWI_LOCATION_ENDPOINT: str = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT: str = "https://tequila-api.kiwi.com/v2/search"
# the parameters will be variable
KIWI_HEADERS: dict = {
    "apikey": os.environ["KIWI_KEY"],
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # datetime
        self.tomorrow = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.plus_6_months = (datetime.today() + timedelta(days=181)).strftime("%d/%m/%Y")
        self.min_return = (datetime.today() + timedelta(days=8)).strftime("%d/%m/%Y")
        self.max_return = (datetime.today() + timedelta(days=201)).strftime("%d/%m/%Y")
        # get city codes
        self.kiwi_location_parameters: dict = {
            "term": "any",
            "locale": "en-US",
            "location_types": "airport",
            "limit": 4,
            "active_only": True,
        }
        # get flights
        self.kiwi_search_parameters: dict = {
            "fly_from": "VIE",
            "fly_to": "PUJ",
            "dateFrom": self.tomorrow,
            "dateTo": self.plus_6_months,
            "return_from": self.min_return,
            "return_to": self.max_return,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "adults": 1,
            "max_fly_duration": 20,
            "flight_type": "round",
            "one_per_date": 1,
            "selected_cabins": "M",
            "price_to": 1000,
            "max_stopovers": 2,
            "vehicle_type": "aircraft",
            "only_working_days": True,
        }

    def request_get_city_code(self, locations: list):
        location_list = []
        for location in locations:
            self.kiwi_location_parameters["term"] = location
            response_location = requests.get(url=KIWI_LOCATION_ENDPOINT,
                                             params=self.kiwi_location_parameters,
                                             headers=KIWI_HEADERS)
            city_code = response_location.json()["locations"][0]["city"]["code"]
            location_list.append(city_code)
        return location_list

    def request_flight_info(self, city_code_list: list, prices: list):
        flight_info_list = []
        for i in range(len(city_code_list)):
            self.kiwi_search_parameters["fly_to"] = city_code_list[i]
            self.kiwi_search_parameters["price_to"] = prices[i]
            response = requests.get(url=KIWI_SEARCH_ENDPOINT,
                                    params=self.kiwi_search_parameters,
                                    headers=KIWI_HEADERS)
            flight_info_list.append(response.json())
            print(flight_info_list)
