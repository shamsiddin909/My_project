import sqlite3

from datetime import datetime
DB = 'data.db'

connection = sqlite3.connect(DB)
sql = connection.cursor()


sql.execute(
    """
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    first_name TEXT,
    phone_number TEXT,
    reg_date DATETIME);
    """
)


def register_user(telegram_id, first_name, phone_button):
    connection = sqlite3.connect(DB)
    sql = connection.cursor()

    sql.execute(" INSERT INTO users (telegram_id, first_name, phone_number, reg_date) VALUES (?,?,?,?); ",
                (telegram_id, first_name, phone_button, datetime.now()))

    connection.commit()
    connection.close()


sql.execute(
    """
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    desc TEXT,
    photo TEXT,
    video TEXT,
    price REAL,
    category TEXT,
    added_date DATETIME);
    """
)


def add_product(name, desc, photo, video, price, category):
    connection = sqlite3.connect(DB)
    sql = connection.cursor()

    sql.execute(" INSERT INTO products (name, desc, photo, video, price, category, added_date) VALUES (?,?,?,?,?,?,?); ",
                (name, desc, photo, video, price, category, datetime.now()))

    connection.commit()
    connection.close()


