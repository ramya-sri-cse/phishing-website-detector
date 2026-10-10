import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from feature_extraction import extract_features


# Load dataset
df = pd.read_csv("phiUSIIL_Phishing_URL_dataset.csv")

print("Dataset loaded successfully!")
print("Total rows:", len(df))


# Extract URL features
X = []
y = []

for i, row in df.iterrows():

    try:
        features = extract_features(row["URL"])

        X.append(features)
        y.append(int(row["label"]))

    except Exception:
        continue


print("Features extracted:", len(X))


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


# Calculate accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully!")
print("Accuracy:", round(accuracy * 100, 2), "%")


# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")