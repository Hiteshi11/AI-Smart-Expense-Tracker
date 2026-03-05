import streamlit as st
import pandas as pd
import easyocr
import numpy as np
import cv2
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

data = pd.read_csv("ai_expense_tracker/data/expenses.csv")

X = data["text"]
y = data["category"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vector, y)

st.title("AI Smart Expense Tracker")


st.header("Upload Receipt")

uploaded_file = st.file_uploader("Upload receipt image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    # convert uploaded file to image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    reader = easyocr.Reader(['en'])

    results = reader.readtext(image)

    text_list = []

    for detection in results:
        text_list.append(detection[1])

    total_amount = None

    for i in range(len(text_list)):
        if "TOTAL" in text_list[i].upper():
            if i + 1 < len(text_list):
                total_amount = text_list[i+1]
                break

    if total_amount:
        st.success(f"Detected Total: {total_amount}")

st.header("Add Expense")

description = st.text_input("Expense description")
if description:
    
    test = vectorizer.transform([description])
    
    predicted_category = model.predict(test)[0]
    
    st.write("Predicted Category:", predicted_category)

amount = st.number_input("Enter amount", min_value=0.0)

category = st.selectbox(
    "Select category",
    ["food", "transport", "shopping", "entertainment"]
)

if st.button("Save Expense"):

    date = datetime.today().strftime('%Y-%m-%d')

    new_expense = pd.DataFrame(
        [[date, amount, category]],
        columns=["date", "amount", "category"]
    )

    import os
    file_path = "ai_expense_tracker/data/expense_log.csv"

    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["date", "amount", "category"])
        df.to_csv(file_path, index=False)

    df = pd.read_csv(file_path)

    df = pd.concat([df, new_expense], ignore_index=True)

    df.to_csv(file_path, index=False)

    st.success("Expense Saved!")

st.header("Expense History")

df = pd.read_csv("ai_expense_tracker/data/expense_log.csv")
st.header("Expense Analysis")

# spending by category
category_sum = df.groupby("category")["amount"].sum()

st.subheader("Spending by Category")
st.bar_chart(category_sum)

# pie chart
st.subheader("Category Distribution")
st.write(category_sum.plot.pie(autopct='%1.1f%%'))

st.dataframe(df)







