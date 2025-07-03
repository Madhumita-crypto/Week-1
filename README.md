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
- **Streamlit** — Web-based model deployment

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
  - BSK5 (Biochemical Oxygen Demand over 5 days)  
  - Suspended Solids  
  - Year  
  - Station ID (encoded via one-hot encoding)

- **Processing Steps**:
  - Handled missing values using **median imputation**
  - Extracted date-related features (`year`, `month`)
  - Sorted by `id` and `date`
  - Applied one-hot encoding for station IDs
  - Used **train-test split (80-20%)**

- **Evaluation Metrics**:  
  - **R² Score** – Goodness of fit  
  - **Mean Squared Error (MSE)** – Prediction accuracy  

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

> *Note: Replace these values with your actual results once the model is finalized.*

---

## 🖥 Web App Interface

A minimal `Streamlit` app (`app.py`) is provided to run the model interactively in your browser.

### How to Launch:
```bash
streamlit run app.py
Author
Madhumita Ash
B.Tech IT, GGSIPU
Shell-Edunet AI/ML Internship 2025
