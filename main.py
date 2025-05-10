import requests
import sqlite3
from tabulate import tabulate

def fetch_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'usd'}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data.")
        return []

def create_database(coins_data):
    conn = sqlite3.connect('crypto.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS coins (
        id TEXT PRIMARY KEY,
        name TEXT,
        symbol TEXT,
        current_price REAL,
        market_cap REAL,
        total_volume REAL
    )
    ''')

    for coin in coins_data:
        cursor.execute('''
        INSERT OR REPLACE INTO coins (id, name, symbol, current_price, market_cap, total_volume)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (coin['id'], coin['name'], coin['symbol'], coin['current_price'], coin['market_cap'], coin['total_volume']))

    conn.commit()
    conn.close()

def analyze_data():
    conn = sqlite3.connect('crypto.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT name, current_price, market_cap, total_volume 
    FROM coins
    ORDER BY market_cap DESC
    LIMIT 5
    ''')
    
    rows = cursor.fetchall()
    headers = ["Name", "Price (USD)", "Market Cap (USD)", "Volume (USD)"]
    
    print("\n🪙 Top 5 coins by Market Cap:")
    print(tabulate(rows, headers=headers, tablefmt="pretty"))

    conn.close()

def main():
    print("📡 Fetching cryptocurrency data...")
    coins_data = fetch_data()
    
    if coins_data:
        print("📦 Creating database and inserting data...")
        create_database(coins_data)
        
        print("📊 Analyzing data...")
        analyze_data()

if __name__ == '__main__':
    main()
