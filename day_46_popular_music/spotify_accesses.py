import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pandas as pd
from time import sleep
import requests

SPOTIFY_ID = os.environ['SPOT_ID']
SPOTIFY_KEY = os.environ['SPOT_KEY']
BASE_URL = 'https://example.com'

SPOTIFY_ENDPOINT: str = 'https://api.spotify.com/v1/search'
spotify_create_playlist_url = 'https://api.spotify.com/v1/users'


class AccessSpotify:

    def __init__(self):
        self.uri_dict: dict = {}
        self.new_playlist = None
        self.user_id = None
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope='user-follow-modify user-library-modify playlist-read-private playlist-modify-private',
                                      redirect_uri=BASE_URL,
                                      client_id=SPOTIFY_ID,
                                      client_secret=SPOTIFY_KEY,
                                      show_dialog=True,
                                      cache_path='token.txt',
                                      ))

        self.token_sp = self.request_token()

    def request_token(self):
        self.user_id = self.sp.current_user()['id']
        print('Please, accept the terms if asked.')
        sleep(1)
        return self.get_token()

    def get_token(self):
        data = pd.read_csv('token.txt')
        new_data = data.to_dict(orient='split')
        return new_data["columns"][0].strip('{').strip('"access_token": ')

    def request_spotify_info(self, song_list, artist_list):
        spotify_headers: dict = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token_sp}',
        }

        try:
            if len(artist_list) == len(song_list):
                uri_list = []
                for index_number in range(len(song_list)):
                    song_name: str = song_list[index_number]
                    # artist_name: str = self.artist_list[index_number]
                    spotify_params: dict = {
                        'q': f'{song_name}',
                        'type': 'track',
                        'limit': 1,
                    }
                    response_spotify = requests.get(url=SPOTIFY_ENDPOINT,
                                                    params=spotify_params,
                                                    headers=spotify_headers)
                    data_uri = response_spotify.json()['tracks']['items'][0]['uri']
                    uri_list.append([data_uri])
                self.uri_dict['uris'] = uri_list
        except IndexError as ie:
            print(ie)
        except KeyError as ke:
            print(ke)

    def create_playlist(self, travel_to_date):
        self.new_playlist = self.sp.user_playlist_create(user=self.user_id,
                                                         name=f'Bb_{travel_to_date}_hot100',
                                                         public=False,
                                                         description=f'Billboard Hot100: {travel_to_date}.')

    def add_items_to_playlist(self):
        for uri in self.uri_dict['uris']:
            self.sp.playlist_add_items(playlist_id=self.new_playlist['id'], items=uri)

# https://ingxfm.github.io/cv/
