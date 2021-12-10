""" A program to download all spotify songs in a playlist by searching it through youtube and downloading it\
    testing 2
"""
import os
import spotipy
from googleapiclient.discovery import build
from pytube import YouTube
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

clientID = os.getenv('CLIENTID')
ClientSecret = os.getenv('CLIENTSECRET')
youtubeAPI = os.getenv('YOUTUBEAPI')
youtubeAPI2 = os.getenv('YOUTUBEAPI2')
=======
song_id_list = []

#search the playlist from spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientID, client_secret=ClientSecret))
youtubeSearch =build("youtube", "v3", developerKey=youtubeAPI)
playlist = input("Insert playlist")
results = sp.playlist_tracks(playlist_id=playlist, fields="items(track.name, track(artists.name))")
song_list=results["items"]

#puts all the song searched to into a playlist
#searches the song name by the author
for i in range(len(song_list)):
    song_name = song_list[i]["track"]["name"]
    author = song_list[i]["track"]["artists"]
    name = author[0]["name"]
    request = youtubeSearch.search().list(part='snippet',maxResults=1,q= (song_name + " by " + name))
    response = request.execute()
    song_id_list.append((response["items"][0]["id"]["videoId"]))

#download the videos in playlist
print(song_id_list)
for song in song_id_list:
    yt = YouTube(f"https://www.youtube.com/watch?v={song}")
    print(yt.streams.filter(only_audio=True))
    yt_stream = yt.streams.get_audio_only()
    yt_stream.download()


