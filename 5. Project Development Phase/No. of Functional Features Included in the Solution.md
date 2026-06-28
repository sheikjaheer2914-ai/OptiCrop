# Enumerated Functional Feature Index

The core engine contains **three main functional software layers** built and evaluated for production state:

## 1. Soil Chemistry Diagnostics Module
Captures structural land metrics (Nitrogen, Phosphorous, Potassium densities) alongside an acidity slider spanning pH 0 to 14. Provides baseline checks to ensure input integrity.

## 2. Real-Time Multi-Class Crop Optimization Engine
Packs raw vectors, applies standard scalar transforms, and maps values through a 100-estimator Random Forest framework to output the single highest-yielding crop recommendations.

## 3. Dynamic Precision Confidence Matrix
Exposes internal classification probabilities to output a precision confidence bar chart on the UI, informing farmers of model assertion security.
