import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

#results = spotify.search(q='artist:' + name, type='artist')
results = spotify.search(
    "Discover Weekly",
    10,
    offset=0,
    type="playlist",
    market="US"
)["playlists"]["items"]
for result in results:
    print(result)
# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print(artist['name'], artist['images'][0]['url'])