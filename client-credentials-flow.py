import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import os
import config.py

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#get username form commandline
username = sys.argv[1]

#set Environ vars:
os.environ["SPOTIPY_CLIENT_ID"] = "Client ID 583081c07bdd4f199416678ac19c396c"
os.environ["SPOTIPY_CLIENT_SECRET"] = "XXXXXXXXXXXXXXXXX"

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)