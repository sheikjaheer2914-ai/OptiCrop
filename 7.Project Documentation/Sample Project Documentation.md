# OptiCrop Smart Engine - Comprehensive System Documentation

## 1. Project Abstract & Motivation
OptiCrop is a specialized Smart Agricultural Production Optimization Engine designed to minimize seasonal crop failure risks. By mapping dynamic soil property matrices (Nitrogen, Phosphorous, Potassium, and active topsoil pH scales) alongside immediate regional weather data records, the system guides small-scale agricultural producers to cultivate optimal, high-yield seed profiles.

## 2. Operational System Architecture
The platform is engineered using a decoupled execution strategy:
- **Presentation Layer Component:** Streamlit framework generates form fields to collect data variables.
- **Normalization Transformer Layer:** Re-aligns user input feature distributions using standard scaling array values.
- **Inference Layer Core Node:** An ensemble Random Forest classification structure that evaluates 100 decision split nodes to map input statistics to one of 22 optimized crop outputs.

## 3. Core Software Execution Guidelines
1. Install project dependencies from the main configuration directory file: `pip install -r requirements.txt`
2. Execute the live back-end array training pipeline loop script to serialize machine learning parameters: `python3 "5. Project Development Phase/code/train.py"`
3. Boot up the user interface dashboard mapping nodes to interact via local web browsers: `streamlit run "5. Project Development Phase/code/app.py"`
