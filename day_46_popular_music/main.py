# my own modules
from spotify_accesses import AccessSpotify
from billboard_info import RequestBillboardInfo


def get_hot100_playlists():
    bill_object = RequestBillboardInfo()
    if '-' in bill_object.date_to_travel:
        if len(bill_object.date_to_travel.split("-")) == 3:
            spotify_object = AccessSpotify()  # token info object
            bill_object.request_billboard_info()
            spotify_object.request_spotify_info(song_list=bill_object.song_list, artist_list =bill_object.artist_list)
            spotify_object.create_playlist(bill_object.date_to_travel)
            spotify_object.add_items_to_playlist()
    else:
        print('Please use the date format YYYY-MM-DD.')
        get_hot100_playlists()


get_hot100_playlists()

# References
# https://www.delftstack.com/howto/python/remove-n-from-string-python/
