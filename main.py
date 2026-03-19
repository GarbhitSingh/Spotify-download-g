import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os

# Replace with your Spotify API credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to search tracks, albums and playlists

def search_spotify(query, search_type='track'):
    results = sp.search(q=query, type=search_type)
    return results

# Function to download a single track

def download_track(track_id):
    track = sp.track(track_id)
    audio_url = track['preview_url']  # Note: Spotify does not provide full track downloads.
    if audio_url:
        response = requests.get(audio_url)
        if response.status_code == 200:
            with open(f"{track['name']}.mp3", 'wb') as track_file:
                track_file.write(response.content)
            print(f"Downloaded: {track['name']}")
        else:
            print("Failed to download track.")

# Function to download a playlist

def download_playlist(playlist_id):
    playlist = sp.playlist_tracks(playlist_id)
    for item in playlist['items']:
        download_track(item['track']['id'])

# Function to download an album

def download_album(album_id):
    album = sp.album_tracks(album_id)
    for item in album['items']:
        download_track(item['id'])

# Main function

def main():
    query = input('Enter your search query: ')
    search_type = input('Search for (track/album/playlist): ')
    results = search_spotify(query, search_type)
    print(results)  # Display search results

if __name__ == '__main__':
    main()