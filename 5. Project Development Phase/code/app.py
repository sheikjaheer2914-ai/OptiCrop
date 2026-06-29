import streamlit as st, numpy as np, joblib
st.set_page_config(page_title="OptiCrop UI", page_icon="🌾", layout="wide")
st.title("🌾 OptiCrop: Smart Production Engine")
st.write("AIML Track Group Project Dashboard")

@st.cache_resource
def load_assets():
    try:
        model = joblib.load("5. Project Development Phase/code/models/opticrop_model.pkl")
        scaler = joblib.load("5. Project Development Phase/code/models/scaler.pkl")
        return model, scaler
    except Exception: return None, None

model, scaler = load_assets()

if model is None:
    st.error("⚠️ Model weights missing! Run the training script in your terminal first.")
else:
    st.success("✅ Engine Operational! Ready for live predictions.")
    col1, col2 = st.columns(2)
    with col1:
        n = st.number_input("Nitrogen (N)", 0, 150, 70)
        p = st.number_input("Phosphorus (P)", 0, 150, 50)
        k = st.number_input("Potassium (K)", 0, 150, 40)
        ph = st.slider("Soil pH", 0.0, 14.0, 6.5)
    with col2:
        temp = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
        hum = st.slider("Humidity (%)", 0.0, 100.0, 65.0)
        rain = st.number_input("Annual Rainfall (mm)", 0.0, 3000.0, 1200.0)
        
    if st.button("🚀 Run Live Crop Recommendation", use_container_width=True):
        user_data = np.array([[n, p, k, temp, hum, ph, rain]])
        scaled_data = scaler.transform(user_data)
        prediction = model.predict(scaled_data)[0]
        
        st.markdown("--- ")
        st.success(f"### 🎉 Recommended Optimal Crop Target: **{prediction.upper()}**")
        
        st.markdown("### 🤖 Embedded AI Agronomic Advisory Report")
        advice = f"Our local model has evaluated your field vectors. For cultivating **{prediction.title()}**, your soil pH of {ph} is stable. "
        if n < 50: advice += "However, Nitrogen levels are low; consider adding organic compost. "
        if rain < 100: advice += "Rainfall thresholds are minimal for this cycle; ensure proper drip-irrigation scheduling. "
        if rain > 200: advice += "High rainfall expected; monitor soil drainage parameters closely to prevent root rot. "
        
        st.info(advice)
