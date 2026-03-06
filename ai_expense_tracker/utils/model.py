import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st


@st.cache_resource
def load_model():

    data = pd.read_csv("ai_expense_tracker/data/expenses.csv")

    X = data["text"]
    y = data["category"]

    vectorizer = TfidfVectorizer()
    X_vector = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vector, y)

    return model, vectorizer

