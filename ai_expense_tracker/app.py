import streamlit as st
import pandas as pd
import easyocr
import numpy as np
import cv2
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="AI Smart Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Smart Expense Tracker")
st.write("Track your expenses with AI-powered receipt scanning.")

# -------- TRAIN CATEGORY MODEL --------
data = pd.read_csv("ai_expense_tracker/data/expenses.csv")

X = data["text"]
y = data["category"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vector, y)

# -------- RECEIPT SCANNER --------
st.header("Upload Receipt")

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
        st.success(f"Detected Total: {total_amount}")

# -------- EXPENSE INPUT --------
st.header("Add Expense")

description = st.text_input("Expense description")

if description:
    test = vectorizer.transform([description])
    predicted_category = model.predict(test)[0]
    st.write("Predicted Category:", predicted_category)

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Enter Amount")

with col2:
    category = st.selectbox(
        "Select Category",
        ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Other"]
    )

file_path = "ai_expense_tracker/data/expense_log.csv"

# create file if it doesn't exist
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["date","amount","category"])
    df.to_csv(file_path, index=False)

# -------- SAVE EXPENSE --------
if st.button("Save Expense"):

    date = datetime.today().strftime('%Y-%m-%d')

    new_expense = pd.DataFrame(
        [[date, amount, category]],
        columns=["date", "amount", "category"]
    )

    df = pd.read_csv(file_path)

    df = pd.concat([df, new_expense], ignore_index=True)

    df.to_csv(file_path, index=False)

    st.success("Expense Saved!")

# -------- LOAD DATA --------
df = pd.read_csv(file_path)

# -------- EXPENSE HISTORY --------
st.header("📜 Expense History")
st.dataframe(df)

# -------- PIE CHART --------
st.header("📊 Expense Distribution")

if len(df) > 0:

    category_totals = df.groupby("category")["amount"].sum()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.pie(
        category_totals,
        labels=category_totals.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.axis("equal")

    st.pyplot(fig)

else:
    st.info("No expenses recorded yet.")


