import sqlite3


def create_connection():
    conn = sqlite3.connect("db/nifty100.db")
    return conn