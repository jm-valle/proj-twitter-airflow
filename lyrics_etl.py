import requests  
import pandas as pd

def run_vagalume_etl():
    API_URL = 'https://api.vagalume.com.br' 
    API_LYRIC_SEARCH_URL = API_URL + '/search.php' 

    
    api_key = '5beabcd3768f7b93c4ba4a84cac4aa2a' 
    artist_name = 'Gorillaz' 
    # song_title = 'Controllah' 
    # params = {
    #     'art': artist_name, 
    #     'mus': song_title, 
    #     'apikey': api_key, 
    # }

    with open('songs.txt') as f:
        songs = f.readlines()

    all_lyrics = []


    for song in songs:
        print(song)
        print('---------------------------------------------------------------------------------')
        params = {
        'art': artist_name, 
        'mus': song, 
        'apikey': api_key
        }
        try:  
            r = requests.get(API_LYRIC_SEARCH_URL, params)
            lyrics = r.json().get('mus')[0].get('text')
            lyrics_cleaned = lyrics.replace('"', '')
        except TypeError:
            print('Song not found')
            continue
        refined_lyric = {
            'name': 'Gorillaz',
            'song': song,
            'lyrics': lyrics_cleaned
        }
        print(refined_lyric)
        all_lyrics.append(refined_lyric)
        
    # for tweet in tweets:
    #     text = tweet._json['full_text']
    #     refined_tweet = {'user': tweet.user.screen_name,
    #                      'text': text,
    #                      'favorite_count': tweet.favorite_count,
    #                      'retweet_count': tweet.retweet_count,
    #                      'created_at': tweet.created_at}
        
    #     tweet_list.append(refined_tweet)

    df = pd.DataFrame(all_lyrics)
    df.to_csv('s3://joaomarcos-airflow-lyrics-bucket/gorillaz_lyrics.csv')