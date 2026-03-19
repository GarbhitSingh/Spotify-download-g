import sqlite3
import requests
from random import choice

# SQLite database setup
DB_NAME = 'proxy_manager.db'

def create_connection():
    connection = sqlite3.connect(DB_NAME)
    return connection

# Create table
def create_table():
    connection = create_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS proxies (
                              id INTEGER PRIMARY KEY,
                              proxy TEXT NOT NULL UNIQUE,
                              verified INTEGER NOT NULL)
                          ''')

# Add proxy
def add_proxy(proxy):
    connection = create_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute('INSERT OR IGNORE INTO proxies (proxy, verified) VALUES (?, ?)', (proxy, 0))

# Verify proxy
def verify_proxy(proxy):
    try:
        response = requests.get('http://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=5)
        return response.status_code == 200
    except:
        return False

# Filter verified proxies
def filter_verified_proxies():
    connection = create_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT proxy FROM proxies WHERE verified = 1')
        return [row[0] for row in cursor.fetchall()]

# Rotate proxy
def rotate_proxy():
    verified_proxies = filter_verified_proxies()
    if verified_proxies:
        return choice(verified_proxies)
    else:
        return None

# Main functionality
if __name__ == '__main__':
    create_table()
    # Example proxies
    proxies_list = ['http://123.45.67.89:8080', 'http://98.76.54.32:9000']
    for proxy in proxies_list:
        add_proxy(proxy)
        if verify_proxy(proxy):
            with create_connection() as conn:
                conn.execute('UPDATE proxies SET verified = 1 WHERE proxy = ?' , (proxy,))
        
    print('Rotated to proxy:', rotate_proxy())