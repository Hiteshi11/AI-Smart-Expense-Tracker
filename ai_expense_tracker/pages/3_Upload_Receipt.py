import streamlit as st
import easyocr
import numpy as np
import cv2
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

st.title("📷 Upload Receipt")

uploaded_file = st.file_uploader("Upload receipt image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)

    text_list = [detection[1] for detection in results]

    total_amount = None

    for i in range(len(text_list)):
        if "TOTAL" in text_list[i].upper():
            if i + 1 < len(text_list):
                total_amount = text_list[i+1]
                break

    if total_amount:

        amount = float(total_amount.replace("₹","").replace(",",""))

        st.success(f"Detected Total: ₹{amount}")

        if st.button("Save Receipt Expense"):

            date = datetime.today().strftime('%Y-%m-%d')

            cursor.execute(
                "INSERT INTO expenses VALUES (?, ?, ?)",
                (date, amount, "Other")
            )

            conn.commit()

            st.success("Receipt expense saved!")
