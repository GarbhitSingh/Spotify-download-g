# Spotify Download Bot

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/GarbhitSingh/Spotify-download-g.git
   cd Spotify-download-g
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**:
   - You need to create a `.env` file in the root directory and add your Spotify API credentials:
   ```env
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   ```

## Features
- Download songs or playlists from Spotify.
- Supports high-quality audio format.
- User-friendly command-line interface.
- Allows searching for songs directly.

## Usage Examples
- To download a single song:
  ```bash
  python download.py "Song Title" 
  ```

- To download a playlist:
  ```bash
  python download.py --playlist "Playlist URL"
  ```

## How to Use the Bot
1. **Run the bot**:
   ```bash
   python main.py
   ```
2. **Follow the on-screen instructions** to select what you want to download and provide necessary information.

3. **Enjoy your music!**