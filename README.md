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
```

You’ll be able to:
- Input year, station ID, and chemical indicators (NH₄, BSK5, Suspended solids)
- Instantly view predicted pollutant levels for that station and year

Great for quick demonstrations or scaling to a web dashboard!

---

## 📦 Files Generated

| File                          | Purpose                                      |
|-------------------------------|----------------------------------------------|
| [`pollution_model.pkl`](https://drive.google.com/file/d/18RJzu35vyuMgpcAE590u1IaDvHY3-SWq/view?usp=sharing) | 🔗 **Download Trained Model** |
| `model_columns.pkl`           | Stores the one-hot encoded feature columns   |
| `Water_Quality_Predictor.ipynb` | Main Jupyter Notebook with full code        |
| `PB_All_2000_2021.csv`        | Raw dataset used for model training          |
| `app.py`                      | Streamlit app to interact with predictions   |

---

##  Author

**Madhumita Ash**  
B.Tech IT, GGSIPU  
Shell-Edunet AI/ML Internship 2025

---

## ✅ Final Notes

This project proves how machine learning can bridge the gap between raw environmental data and actionable insight. With additional features (like rainfall, temperature, or proximity to industrial zones), this model could scale to national-level water quality prediction systems.
