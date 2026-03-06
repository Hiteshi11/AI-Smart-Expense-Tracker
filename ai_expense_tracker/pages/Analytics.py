import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("expenses.db", check_same_thread=False)

df = pd.read_sql_query("SELECT * FROM expenses", conn)

st.title("📈 Analytics")

if len(df) > 0:

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    if st.button("Show Pie Chart"):

        category_totals = df.groupby("category")["amount"].sum()

        fig, ax = plt.subplots()

        ax.pie(
            category_totals,
            labels=category_totals.index,
            autopct="%1.1f%%"
        )

        ax.axis("equal")

        st.pyplot(fig)

    if st.button("Show Monthly Chart"):

        df["date"] = pd.to_datetime(df["date"])

        monthly = df.groupby(df["date"].dt.month)["amount"].sum()

        st.line_chart(monthly)

else:
    st.info("No expense data yet.")
