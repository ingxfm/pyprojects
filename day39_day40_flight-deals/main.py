# Built-in modules
from datetime import datetime, timedelta
import os

# 3rd-party modules
import requests
from twilio.rest import Client

# My own modules and classes
from data_manager import DataManager
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve
# the program requirements.
# # Program Requirements

# TODO 1: Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International
#  Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include
#  multiple airports, you want the city code (not the airport code see here).

# data_manager = DataManager()
# locations_list = data_manager.cities
# print(f"from MAIN: {locations_list}")

flight_searching = FlightSearch()
# city_codes_list = flight_searching.request_get_city_code(locations_list)
# print(f"from MAIN: {city_codes_list}")

# data_manager.update_rows_to_sheet(city_codes_list)

# TODO 2: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later
#  for all the cities in the Google Sheet.
city_codes_list = ["PAR", "BER", "TYO", "SYD", "IST", 'KUL', "NYC", "SFO", "CPT", "PUJ", "HAQ"]
prices = [54, 42, 485, 551, 95, 414, 240, 260, 378, 400, 450]
flight_searching.request_flight_info(city_codes_list, prices)

# TODO 3: If the price is lower than the lowest price listed in the Google Sheet then send an SMS to
#  your own number with the Twilio API.

# TODO 4: The SMS should include the departure airport IATA code, destination airport IATA code,
#  departure city, destination city, flight price and flight dates. e.g.