import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyAuthBase
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="89b99e94edc743308c38b79819528ca5", client_secret="104203283c1e47a1afbd1ee94b47a263", redirect_uri="http://localhost:8888/callback"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

# print(sp.artist_related_artists("06HL4z0CvFAxyc27GXpf02")['artists'][0])

# print(sp.artist_top_tracks("06HL4z0CvFAxyc27GXpf02")['tracks'][0])

# print(sp.recommendation_genre_seeds())

songs = sp.recommendations(seed_artists=['06HL4z0CvFAxyc27GXpf02'], seed_tracks=['1BxfuPKGuaTgP7aM0Bbdwr'], seed_genres=['sad', 'romance'], limit=10, country='US')
for song in songs['tracks']:
    print(song['name'], " – ", song['artists'][0]['name'])
for seed in songs['seeds']:
    print(seed['type'], " – ", seed['id'])
