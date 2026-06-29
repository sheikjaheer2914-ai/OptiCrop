import os, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

def train_pipeline():
    df = pd.read_csv("5. Project Development Phase/code/data/crop_recommendation.csv")
    df.columns = df.columns.str.strip().str.lower()
    X = df.drop(columns=['label'])
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train_scaled, y_train)
    joblib.dump(model, "5. Project Development Phase/code/models/opticrop_model.pkl")
    joblib.dump(scaler, "5. Project Development Phase/code/models/scaler.pkl")

if __name__ == '__main__':
    train_pipeline()
