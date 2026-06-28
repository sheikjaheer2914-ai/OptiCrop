# Coding & Solution Report

## 1. Project Implementation Scripts
Our full functional solution is written in Python and split into clean, modular files. You can access the working code directly in the repository paths below:
- **Data Pipeline Layer:** [preprocessing.py](./code/preprocessing.py) - Handles dataset scaling and test-train matrix creation.
- **Machine Learning Core:** [train.py](./code/train.py) - Trains the Random Forest algorithm and saves model binaries.
- **Web Dashboard GUI:** [app.py](./code/app.py) - Runs the interactive user interface using Streamlit.

## 2. Core Machine Learning Logic
Our system utilizes the **Random Forest Classifier** model to execute multi-class crop recommendations. The pipeline normalizes 7 primary environmental and soil chemistry metrics through a standard scaling transformer layer before calculating final class assignment probabilities.
