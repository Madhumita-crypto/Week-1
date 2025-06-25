# 🌊 Water Quality Prediction Using Machine Learning

> **“Turning chemical signals into clarity — one prediction at a time.”**

---

## 📅 Internship: Shell-Edunet Skills4Future (June–July 2025)

This project predicts whether water is safe to drink using machine learning based on chemical parameters. Developed as part of the Shell-Edunet AI-ML Internship, it marks my **first AI/ML project** and a step toward data-driven sustainability.

---

## 📌 Project Overview

This notebook-based project predicts **key water quality indicators** from historical chemical data collected across **22 stations in Punjab (2000–2021)**. The system uses supervised machine learning to estimate the concentration of pollutants that affect water safety, public health, and environmental balance.

With climate change and urbanization pressing hard, this predictive model is a humble yet firm stride toward **proactive environmental monitoring**.

---

## ⚙️ Technologies Used

- **Python** — Core programming language  
- **Pandas** — Data preprocessing  
- **NumPy** — Numerical operations  
- **Matplotlib & Seaborn** — Visualization  
- **Scikit-learn** — ML modeling and evaluation  
- **Joblib** — Model serialization  

---

## 💧 Pollutants Predicted

The following **6 parameters** were selected for multi-output regression:

| Parameter | Description                              |
|-----------|------------------------------------------|
| **O₂**    | Dissolved Oxygen (mg/L)                  |
| **NO₃**   | Nitrates (mg/L)                          |
| **NO₂**   | Nitrites (mg/L)                          |
| **SO₄**   | Sulfates (mg/L)                          |
| **PO₄**   | Phosphates (mg/L)                        |
| **Cl⁻**   | Chlorides (mg/L)                         |

---

## 🤖 Model & Methodology

- **Model Used**:  
  `RandomForestRegressor` wrapped inside a `MultiOutputRegressor` for simultaneous multi-target regression.

- **Features Used**:  
  - NH₄ (Ammonium)  
  - BSK5 (BOD over 5 days)  
  - Suspended Solids  
  - Year  
  - Month  

- **Processing Steps**:
  - Handled missing values via **median imputation**
  - Extracted **temporal features** from the date (`year`, `month`)
  - Sorted by `id` and `date`
  - Used **train-test split (80-20%)**

- **Evaluation Metrics**:  
  - R² Score – Goodness of fit  
  - Mean Squared Error – Prediction accuracy  

---

## 📊 Model Performance Snapshot

| Parameter | R² Score | Mean Squared Error |
|-----------|----------|--------------------|
| O₂        | 0.82     | 3.12               |
| NO₃       | 0.85     | 2.45               |
| NO₂       | 0.78     | 0.09               |
| SO₄       | 0.87     | 120.55             |
| PO₄       | 0.80     | 0.07               |
| CL        | 0.91     | 140.34             |

> ⚠️ *Note: These values are placeholders. Replace them with your actual test results from `model.predict()` evaluation.*

---

## 📦 Files Generated

| File                          | Purpose                                      |
|-------------------------------|----------------------------------------------|
| [`pollution_model.pkl`](https://drive.google.com/file/d/18RJzu35vyuMgpcAE590u1IaDvHY3-SWq/view?usp=sharing) | 🔗 **Download Model** – Trained ML model |
| `model_columns.pkl`           | Stores the feature column structure          |
| `Water_Quality_Predictor.ipynb` | Main Jupyter Notebook with complete code     |
| `PB_All_2000_2021.csv`        | Original dataset used for training           |

> 📥 You can directly download the trained model file (`pollution_model.pkl`) from [this link](https://drive.google.com/file/d/18RJzu35vyuMgpcAE590u1IaDvHY3-SWq/view?usp=sharing).

---

## ✅ Final Notes

This project proves how machine learning can bridge the gap between raw environmental data and actionable insight. With more features (like rainfall, temperature, or proximity to industrial zones), this model could scale to national-level water quality prediction systems.

---

