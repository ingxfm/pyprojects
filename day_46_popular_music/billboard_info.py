# 3rd-party modules
import requests
from bs4 import BeautifulSoup

URL: str = 'https://www.billboard.com/charts/hot-100/'  # billboard web info
CLASS_FOR_SONG: str = 'u-line-height-125'
CLASS_FOR_ARTIST: str = 'a-truncate-ellipsis-2line'


class RequestBillboardInfo:

    def __init__(self):
        self.date_to_travel: str = input("What year would like to travel? Type the data in the format YYYY-MM-DD: ")
        self.song_list: list = []
        self.artist_list: list = []
        self.spotify_headers = None

    def request_billboard_info(self):
        response = requests.get(f'{URL}/{self.date_to_travel}/')
        web_html = response.text
        soup = BeautifulSoup(web_html, 'html.parser')
        html_song_extracted = soup.find_all(name='h3', id='title-of-a-story', class_=CLASS_FOR_SONG)
        html_artist_extracted = soup.find_all(name='span', class_=CLASS_FOR_ARTIST)
        self.song_list = [item.getText().replace('\n', '').replace('\t', '') for item in html_song_extracted]
        self.artist_list = [item.getText().replace('\n', '').replace('\t', '') for item in html_artist_extracted]

