# Solution Architecture & System Diagrams

## 1. High-Level System Workflow
The flowchart below maps out the system's runtime architecture from the frontend interface down to the backend model:



## 2. Data Entity Mapping
Our structural variables map directly into three primary evaluation entities:



## 3. Deployment Topology
- **Frontend App Server:** Managed via a lightweight Python Streamlit web engine context.
- **Model Processing Node:** Runs isolated multi-class decision trees using optimized Random Forest estimators.
- **Portfolio Integration Interface:** Hosted on a cloud tracking system and linked directly to your Skill Wallet dashboard profile.
