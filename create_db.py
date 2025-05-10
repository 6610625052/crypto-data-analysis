import sqlite3

conn = sqlite3.connect("crypto.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS coins (
        id TEXT PRIMARY KEY,
        symbol TEXT,
        name TEXT,
        current_price REAL,
        market_cap INTEGER,
        total_volume REAL
    )
''')

conn.commit()
conn.close()

print("✅ สร้างฐานข้อมูล crypto.db และตาราง coins เรียบร้อยแล้ว")
