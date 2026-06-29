import streamlit as st
import numpy as np
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

@st.cache_resource
def get_trained_model():
    crops = ['rice', 'maize', 'chickpeas', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
    data_list = []
    for _ in range(800):
        row_crop = random.choice(crops)
        data_list.append([random.randint(20, 120), random.randint(20, 90), random.randint(15, 70), round(random.uniform(18.0, 36.0), 2), round(random.uniform(45.0, 95.0), 2), round(random.uniform(5.0, 8.0), 2), round(random.uniform(50.0, 280.0), 2), row_crop])
    df = pd.DataFrame(data_list, columns=['n','p','k','temperature','humidity','ph','rainfall','label'])
    X = df.drop(columns=['label'])
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train_scaled, y_train)
    return model, scaler, "Status: Operational"

st.set_page_config(page_title="OptiCrop Production Advisor", layout="wide")
st.title("OptiCrop: Smart Production Engine")
st.write("AIML Track Group Project - Precision Agriculture Optimization Dashboard")
st.markdown("--- ")

model, scaler, status = get_trained_model()
st.sidebar.header("System Logs")
st.sidebar.success(status)

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Soil Nutrient Densities (mg/kg)")
    n = st.number_input("Nitrogen (N)", 0, 150, 75)
    p = st.number_input("Phosphorus (P)", 0, 150, 60)
    k = st.number_input("Potassium (K)", 0, 150, 50)
    ph = st.slider("Soil pH Level", 0.0, 14.0, 6.9, step=0.1)
with col2:
    st.markdown("#### Atmospheric Climate Statistics")
    temp = st.number_input("Average Ambient Temperature (Celsius)", 0.0, 50.0, 25.5)
    hum = st.slider("Relative Humidity Percentage (%)", 0.0, 100.0, 65.0)
    rain = st.number_input("Average Annual Rainfall Volume (mm)", 0.0, 3000.0, 1200.0)

if st.button("Calculate Optimized Crop Match", use_container_width=True):
    user_features = np.array([[n, p, k, temp, hum, ph, rain]])
    scaled_features = scaler.transform(user_features)
    prediction = model.predict(scaled_features)
    st.markdown("--- ")
    st.info(f"Recommended Crop Option: {prediction[0].upper()}")
