import sqlite3
import pandas as pd

DB_NAME = "transforaiq.db"

# CONNECTION

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

# GENERIC SELECT

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# GENERIC INSERT

def execute_query(query, values):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, values)

    conn.commit()
    conn.close()