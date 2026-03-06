import streamlit as st
import sqlite3
from datetime import datetime

conn = sqlite3.connect("expenses.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    date TEXT,
    amount REAL,
    category TEXT
)
""")

conn.commit()

st.title("➕ Add Expense")

amount = st.number_input("Enter Amount")

category = st.selectbox(
    "Select Category",
    ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Other"]
)

if st.button("Save Expense"):

    date = datetime.today().strftime('%Y-%m-%d')

    cursor.execute(
        "INSERT INTO expenses VALUES (?, ?, ?)",
        (date, amount, category)
    )

    conn.commit()

    st.success("Expense Saved!")
