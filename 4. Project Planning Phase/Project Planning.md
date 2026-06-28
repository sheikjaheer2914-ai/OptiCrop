# Phase 4: Project Planning & Execution Roadmap

## 1. Project Milestone Schedule (Gantt-Style Timeline)
Our group project spans a 4-week structured development sprints cycle distributed as follows:

- **Week 1: Foundations & Architecture (Phases 1-3)**
  - Problem scoping, empathy mapping, requirement analysis, and architectural system diagrams.
- **Week 2: Data Engineering & Preprocessing (Phase 5 Starter)**
  - Ingesting raw precision datasets, clean null values, handling feature distribution outliers, and engineering standard scaling arrays.
- **Week 3: Model Inferences & Validation (Phase 5 Validation)**
  - Initializing Random Forest configurations, training tree layer branches, hyperparameter optimization, and evaluating accuracy score matrices.
- **Week 4: Front-End UI Assembly & Testing (Phases 5-8)**
  - Injecting predictive states into Streamlit UI view components, compiling unit test verification cases, and pushing deployment repositories.

## 2. Resource & Task Allocation Matrix

| Team Group Member Role | Assigned Technical Project Deliverables |
| :--- | :--- |
| **Project Lead / Data Engineer** | Dataset acquisition, cleaning scripts, vector transformer pipeline development, and data tracking files. |
| **Machine Learning Engineer** | Random Forest model construction, hyperparameter tuning, model performance reports, and model binary serialization (). |
| **UI Developer / QA Lead** | Streamlit front-end form layout building, predictive output routing, application testing cases, and profile synchronization. |

## 3. Risk Mitigation & Contingency Framework
- **Identified Technical Risk:** Inputting extreme out-of-bounds soil values (e.g., pH > 14) crashes or breaks the backend model decision path.
- **Applied Contingency Control:** Embedded validation thresholds and min/max slider constraints directly into the Streamlit input forms to force data consistency before parsing array matrices.
