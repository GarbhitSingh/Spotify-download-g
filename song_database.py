import sqlite3

class SongDatabase:
    def __init__(self, db_name='songs.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            album TEXT,
            year INTEGER,
            popularity INTEGER
        )''')

    def add_song(self, title, artist, album, year, popularity):
        self.cursor.execute('''INSERT INTO songs (title, artist, album, year, popularity)
                             VALUES (?, ?, ?, ?, ?)''',
                             (title, artist, album, year, popularity))
        self.connection.commit()

    def search_song(self, title):
        self.cursor.execute('''SELECT * FROM songs WHERE title LIKE ?''', ('%' + title + '%',))
        return self.cursor.fetchall()

    def update_song_popularity(self, song_id, popularity):
        self.cursor.execute('''UPDATE songs SET popularity = ? WHERE id = ?''', (popularity, song_id))
        self.connection.commit()

    def get_statistics(self):
        self.cursor.execute('''SELECT COUNT(*), AVG(popularity) FROM songs''')
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()