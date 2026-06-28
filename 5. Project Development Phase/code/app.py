import os
import joblib
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# --- FILE PATH CONFIGURATIONS ---
# We store datasets and output models right here inside the Phase 5 folder path
DATA_FILE = "5. Project Development Phase/code/data/crop_recommendation.csv"
MODEL_FILE = "5. Project Development Phase/code/models/opticrop_model.pkl"
SCALER_FILE = "5. Project Development Phase/code/models/scaler.pkl"

def run_model_training():
    """
    Team training routine. If the picker files don't exist locally yet, 
    this script reads the CSV, cleans up column spaces, builds a 
    Random Forest tree, and saves the weights so the UI can read it.
    """
    if not os.path.exists(DATA_FILE):
        st.error(f"Missing data! Put 'crop_recommendation.csv' inside: {os.path.dirname(DATA_FILE)}")
        return None, None, "Failed - Missing CSV"

    # Read data and strip trailing spaces from text columns
    df = pd.read_csv(DATA_FILE)
    df.columns = df.columns.str.strip().str.lower()
    
    # Separate input properties from the target crop label
    X = df.drop(columns=['label'])
    y = df['label']
    
    # Standard 80/20 train-test split for verification
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale inputs so features don't skew our random forest splits
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize classifier (Using 100 trees for optimal split speeds)
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train_scaled, y_train)
    
    # Calculate simple accuracy to show on the dashboard sidebar
    test_preds = model.predict(X_test_scaled)
    score = model.score(X_test_scaled, y_test)
    
    # Make directories if they are missing and dump our objects
    os.makedirs(os.path.dirname(MODEL_FILE), exist_ok=True)
    joblib.dump(model, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    
    return model, scaler, f"Trained Live ({score * 100:.1f}% Acc)"

@st.cache_resource
def load_cached_project_files():
    """Keeps the app fast by saving weights in memory so it doesn't load from disk on every click."""
    try:
        model = joblib.load(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
        return model, scaler, "Pre-trained Weights Loaded"
    except Exception:
        # If running for the first time, fallback to train it right now
        return run_model_training()

# --- STREAMLIT DASHBOARD LAYOUT ---
st.set_page_config(page_title="OptiCrop Advisor", page_icon="🌾", layout="wide")

st.title("🌾 OptiCrop: Smart Production Engine")
st.write("Welcome to our AIML Track Group Project dashboard. Enter field statistics below to get an optimized recommendation.")
st.markdown("---")

# Load model weights
model, scaler, engine_status = load_cached_project_files()

# Simple Sidebar status read-outs
st.sidebar.header("System Logs")
st.sidebar.info(f"Engine Status: {engine_status}")

if "Failed" in engine_status:
    st.sidebar.error("Fix step: Make sure to run your dataset download step in the terminal panel below!")
else:
    # Navigation controls
    mode = st.sidebar.radio("Project Features:", ["Scenario 1: Crop Advisor", "Scenario 2: Field Suitability Matrix"])

    if mode == "Scenario 1: Crop Advisor":
        st.subheader("📋 Enter Current Land & Environment Telemetry")
        
        # Grid columns look clean and human-made
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Soil Nutrient Metrics (mg/kg)**")
            n = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=70)
            p = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=50)
            k = st.number_input("Potassium (K)", min_value=0, max_value=150, value=40)
            ph = st.slider("Soil pH Scale", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
        with col2:
            st.markdown("**Atmospheric Weather Statistics**")
            temp = st.number_input("Average Temperature (°C)", min_value=0.0, max_value=50.0, value=25.5)
            hum = st.slider("Humidity Level (%)", min_value=0.0, max_value=100.0, value=65.0)
            rain = st.number_input("Annual Rainfall Volume (mm)", min_value=0.0, max_value=3000.0, value=1200.0)

        if st.button("🚀 Calculate Optimized Crop Match", use_container_width=True):
            # Format inputs exactly like the trained shape array
            user_data = np.array([[n, p, k, temp, hum, ph, rain]])
            scaled_data = scaler.transform(user_data)
            
            # Predict and find confidence probability
            prediction = model.predict(scaled_data)[0]
            probs = model.predict_proba(scaled_data)
            max_conf = np.max(probs) * 100
            
            st.markdown("---")
            st.success(f"### 🎉 Recommended Crop Choice: **{prediction.upper()}**")
            
            m1, m2 = st.columns(2)
            m1.metric("Model Prediction Confidence", f"{max_conf:.1f}%")
            m2.metric("Soil Balance Check", "NORMAL" if 6.0 <= ph <= 7.5 else "REMEDIATION NEEDED")

    elif mode == "Scenario 2: Field Suitability Matrix":
        st.subheader("🔍 Target Crop Compatibility Analysis")
        st.write("Type a specific crop to see if your field parameters match its threshold requirements.")
        
        wanted_crop = st.text_input("Target Crop Name (e.g. rice, maize, banana, grapes, coffee):").strip().lower()
        
        c1, c2, c3 = st.columns(3)
        with c1:
            in_n = st.number_input("Soil Nitrogen", value=60)
            in_temp = st.number_input("Current Temperature", value=27.0)
        with c2:
            in_p = st.number_input("Soil Phosphorus", value=45)
            in_hum = st.slider("Air Humidity (%)", 0, 100, 70)
        with c3:
            in_k = st.number_input("Soil Potassium", value=35)
            in_rain = st.number_input("Expected Rain (mm)", value=1150.0)
            in_ph = st.number_input("Soil pH", value=6.2)

        if st.button("📊 Evaluate Match Probability", use_container_width=True):
            if not wanted_crop:
                st.warning("Please write a crop name in the textbox first.")
            else:
                crop_classes = list(model.classes_)
                if wanted_crop in crop_classes:
                    check_vec = np.array([[in_n, in_p, in_k, in_temp, in_hum, in_ph, in_rain]])
                    scaled_check = scaler.transform(check_vec)
                    
                    crop_idx = crop_classes.index(wanted_crop)
                    score_pct = model.predict_proba(scaled_check)[0][crop_idx] * 100
                    
                    st.markdown("---")
                    st.write(f"### Compatibility Score for **{wanted_crop.upper()}**: `{score_pct:.1f}%`")
                    
                    if score_pct >= 65.0:
                        st.success("🟢 Highly Feasible: Your soil configuration is a strong match for this crop profile.")
                    elif score_pct >= 30.0:
                        st.warning("🟡 Moderate Risk: Growth is possible, but you will need soil nutrient interventions.")
                    else:
                        st.error("🔴 High Risk Profile: Environmental parameters are an unstable match. Choose a different crop target.")
                else:
                    st.error(f"Crop '{wanted_crop}' is not supported by our current model dataset baseline.")

