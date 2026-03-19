import requests
import sqlite3
import random

class ProxyManager:
    def __init__(self, db_name='proxies.db'):
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS proxies (id INTEGER PRIMARY KEY, proxy TEXT UNIQUE, is_working INTEGER)''')
        conn.commit()
        conn.close()

    def add_proxy(self, proxy):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute('INSERT INTO proxies (proxy, is_working) VALUES (?, ?)', (proxy, 1))
            conn.commit()
        except sqlite3.IntegrityError:
            pass  # Proxy already exists
        finally:
            conn.close()

    def verify_proxies(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT proxy FROM proxies WHERE is_working = 1')
        proxies = c.fetchall()
        for proxy in proxies:
            if self.test_proxy(proxy[0]):
                print(f'{proxy[0]} is working.')
            else:
                print(f'{proxy[0]} is not working. Marking as not working.')
                c.execute('UPDATE proxies SET is_working = 0 WHERE proxy = ?', (proxy[0],))
        conn.commit()
        conn.close()

    def test_proxy(self, proxy):
        try:
            response = requests.get('http://example.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
            return response.status_code == 200
        except:
            return False

    def get_random_proxy(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT proxy FROM proxies WHERE is_working = 1')
        proxies = c.fetchall()
        conn.close()
        return random.choice(proxies)[0] if proxies else None

    def rotate_proxy(self):
        return self.get_random_proxy()