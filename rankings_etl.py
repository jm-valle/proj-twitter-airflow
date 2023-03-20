import requests
import pandas as pd
import json


API_URL = 'https://api.vagalume.com.br' 
API_RANK_SEARCH_URL = API_URL + '/rank.php'     
api_key = '5beabcd3768f7b93c4ba4a84cac4aa2a' 

params = {
    'type': 'mus',
    'period': 'week',
    'periodVal': '202301',
    'scope': 'all',
    'limit': '10'
}

r = requests.get(API_RANK_SEARCH_URL, params=params)
top10_songs = r.json()
# json_object = json.loads(top10_albums)
aux = top10_songs['mus']['week']['all']


songs_names = [] # list of dicts

# print(aux)

for song in aux:
    # print(album['name'])
    songs_dict = {'song': song['name'].replace('(tradução)',''), 
                  'artist': song['art']['name']}
    songs_names.append(songs_dict)

