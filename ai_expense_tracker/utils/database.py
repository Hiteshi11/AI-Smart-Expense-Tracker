import sqlite3
import pandas as pd


def get_connection():
    conn = sqlite3.connect("expenses.db", check_same_thread=False)
    return conn


def load_expenses():

    conn = get_connection()

    df = pd.read_sql_query("SELECT * FROM expenses", conn)

    return df
