# 3rd-party modules
import requests
import bs4
import os

HEADERS = {
    'Request Line': 'GET / HTTP/1.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Dnt': '1',
    'Sec-Gpc': '1',
    'Upgrade-Insecure-Requests': '1',
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
}


class OnlineShopItem:

    def __init__(self):
        self.current_price: float = 0
        self.preset_price: float = 0
        self.url: str = os.environ['ITEM_URL']  # input('What is the URL of the item? ')
        self.save_preset_value()

    def scrape_price(self):
        response = requests.get(url=os.environ['ITEM_URL'], headers=HEADERS)
        response.raise_for_status()
        html_data = response.text
        soup = bs4.BeautifulSoup(html_data, 'html.parser')
        price_value = soup.find(name='span', class_='a-offscreen')
        self.current_price = float(price_value.getText().strip('$'))
        print(self.current_price)

    def is_current_lower_than_preset_price(self):
        if self.current_price <= self.preset_price:
            return True
        else:
            return False

    def save_preset_value(self):
        try:
            with open('preset_price_point.txt', mode='r') as file:
                self.preset_price = float(file.readline())
        except FileNotFoundError as file_error:
            print('No preset price record. Please, add a price.')
            self.preset_price: float = float(input('What price are you aiming for? '))
            with open('preset_price_point.txt', mode='w') as file:
                file.write(f'{self.preset_price}')
        except KeyboardInterrupt as key_error:
            print(key_error)
