from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

URL = 'https://www.billboard.com/charts/hot-100'
CLASS_FOR_SONG: str = 'u-line-height-125'
SPOTIFY_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIFY_KEY = os.environ['SPOTIPY_CLIENT_SECRET']
BASE_URL = 'https://example.com'

user_date = input('Which date do you want to travel to?\n'
                  'Enter the date in the format (YYYY-MM-DD): ')

year_entered = user_date.split('-')[0]

response = requests.get(f'{URL}/{user_date}')
billboard_100_html = response.text

soup = BeautifulSoup(billboard_100_html, 'html.parser')

top_songs = soup.find_all(name='h3', id='title-of-a-story', class_=CLASS_FOR_SONG)
top_songs_list = [song.getText().replace('\n', '').replace('\t', '') for song in top_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-follow-modify playlist-modify-private',
                                               redirect_uri=BASE_URL,
                                               client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_KEY,
                                               show_dialog=True,
                                               cache_path='token.txt',
                                               ))

current_user = sp.current_user()['id']
songs_uris = []

for song in top_songs:
    search_song = sp.search(q=f'{song}', limit=1, type='track')
    # print(search_song)
    try:
        song_uri = search_song['tracks']['items'][0]['uri']
        print(song_uri)
    except IndexError:
        pass
    else:
        songs_uris.append(song_uri)

print(songs_uris)
new_playlist = sp.user_playlist_create(user=current_user, name=f'{user_date} Billboard Hot 100', public=False)
sp.playlist_add_items(playlist_id=new_playlist['id'], items=songs_uris)
