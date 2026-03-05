import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data/expenses.csv")

X = data["text"]
y = data["category"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vector, y)

# Ask user input
user_input = input("Enter expense description: ")

test = vectorizer.transform([user_input])

prediction = model.predict(test)

print("Predicted Category:", prediction[0])
