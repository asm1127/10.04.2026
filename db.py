import sqlite3 as sql

with sql.connect("baza.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        price INTEGER
        )""")
    
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(1, 'Maqsadbek', 'Qurbonboyev', 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(1, 1, 'Pirashka', 14000)""")

    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(2, 'Bobur', 'Jovliyev', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(2, 2, 'Somsa', 14000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(3, 'Husniddin', 'Urinboyev', 15)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(3, 3, 'Pepsi', 14000)""")

    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(4, 'Maqsadbek', 'Qoziyev', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(4, 4, 'Marojniy', 10000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(5, 'Ganijon', 'Norimov', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(5, 5, 'Pitsa', 14000)""")

    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(6, 'Sobirov', 'Ozodbek', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(6, 6, 'Xot-dog', 5000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(7, 'Amirxon', 'Komuljonov', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(7, 7, 'Coca-cola', 14000)""")

    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(8, 'Ibrohimjon', 'Qalandarov', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(8, 8, 'Pirashka', 14000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(9, 'Mominjon', 'Rustamov', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(9, 9, 'Xot-dog', 5000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(10, 'Marjona', 'Setmamatova', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(10, 10, 'Pirashka', 14000)""")

    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(11, 'Maftuna', 'Ramatova', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(11, 11, 'Pirashka', 14000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(12, 'Zuhra', 'Jumanazarov', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(12, 12, 'Pirashka', 14000)""")
    
    cur.execute("""INSERT OR IGNORE INTO users(id, first_name, last_name, age)
                VALUES(13, 'Ruxshona', 'Jorabekova', 16)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id, user_id, product_name, price)
                VALUES(13, 13, 'Pirashka', 14000)""")
    
    con.commit()
    
    print("=" * 50)
    print(f"Users tablesidagi foydalanuvchilar ro'yxati:")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)
    
    print("=" * 50)
    print(f"Xaridlar tablesidagi foydalanuvchilar ro'yxati:")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)
    