class SongDatabase:
    def __init__(self):
        # Initialize the song database as an empty dictionary
        self.songs = {}
        # Initialize user search history as an empty list
        self.user_search_history = []

    def add_song(self, title, artist, genre):
        # Method to add a new song to the database
        self.songs[title] = {'artist': artist, 'genre': genre}

    def search_song(self, title):
        # Method to search for a song by title
        if title in self.songs:
            song_info = self.songs[title]
            self.user_search_history.append(title)  # Log the search
            return song_info
        else:
            return None

    def get_search_history(self):
        # Method to get the user search history
        return self.user_search_history

# Example usage
if __name__ == '__main__':
    database = SongDatabase()
    database.add_song('Shape of You', 'Ed Sheeran', 'Pop')
    print(database.search_song('Shape of You'))  # Should return song details
    print(database.get_search_history())  # Should show the search history
