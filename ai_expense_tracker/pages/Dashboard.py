import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("expenses.db", check_same_thread=False)

df = pd.read_sql_query("SELECT * FROM expenses", conn)

st.title("📊 Dashboard")

if len(df) > 0:

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    total_spent = df["amount"].sum()
    total_transactions = len(df)
    top_category = df.groupby("category")["amount"].sum().idxmax()

else:
    total_spent = 0
    total_transactions = 0
    top_category = "No Data"

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Spending", f"₹{total_spent}")
col2.metric("🧾 Transactions", total_transactions)
col3.metric("🏆 Top Category", top_category)

st.markdown("---")

st.subheader("📜 Expense History")
st.dataframe(df)
