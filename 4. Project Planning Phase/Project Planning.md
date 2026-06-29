# Phase 4: Project Planning, Matrix Schedules & Risk Architecture

## 1. Operational Resource Plan & Tasks
- **Sprint 1 (Scoping Track):** Problem identification, empathy mapping matrices, FRS/NFRS parsing rules.
- **Sprint 2 (Data Track):** Cleaning null cells, outlier handling arrays, StandardScaler transformer scaling.
- **Sprint 3 (ML Track):** Ensemble Random Forest Classifier optimization, validation tracking loops.
- **Sprint 4 (UI Deployment):** App layout state caching integration, performance evaluation logs.

## 2. Formal Evaluation Risk Assessment Matrix

| Target Identified Risk Event | Initial Probability | Impact Score | Contingency Operations Control |
| :--- | :--- | :--- | :--- |
| **Out-of-Bounds User Input Data:** Farmer enters nonsensical metrics (e.g., pH 14, zero rainfall) which breaks model tree logic splits. | Medium | High | Embed min/max parameter limits and dynamic input form validation check barriers directly inside `app.py`. |
| **Model Asset Path Failure:** Serialized weight binaries (`.pkl`) fail to unpickle at runtime, crashing the browser state. | Low | Critical | Implement an automated fallback try-catch conditional loop that re-runs the data cleaning and fitting sequence live if assets are missing. |
| **Local Memory Overload:** Heavy user requests exhaust runtime memory on local web servers. | Low | Medium | Apply Streamlit resource caching annotations (`@st.cache_resource`) to lock the binaries into isolated cache slots. |
