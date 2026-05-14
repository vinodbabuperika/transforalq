import sqlite3
import pandas as pd

DB_NAME = "transforaiq.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def execute_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df