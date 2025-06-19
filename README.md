# Week-1
This project predicts whether water is safe to drink using machine learning based on chemical parameters. Developed as part of the Shell-Edunet Skills4Future Internship (June–July 2025), it marks my first AI/ML project and a step toward data-driven sustainability.

# 🌊 Water Quality Prediction Using Machine Learning

> **“Turning chemical signals into clarity — one prediction at a time.”**

---

## 📌 Project Overview

This project is a part of the Edunet Foundation AI-ML Internship and focuses on predicting key water quality parameters using historical water sample data from Punjab (2000–2021). By leveraging machine learning, the goal is to estimate the levels of critical pollutants and chemical indicators, enabling proactive environmental management and safer water monitoring systems.

With growing environmental concerns and public health risks due to polluted water bodies, accurate prediction of water quality plays a crucial role in early warning systems and sustainable resource management.

---

## ⚙️ Technologies Used

- **Python** — Core programming language  
- **Pandas** — Data handling and preprocessing  
- **NumPy** — Numerical operations  
- **Matplotlib & Seaborn** — Data visualization  
- **Scikit-learn** — Machine learning (model training & evaluation)

---

## 💧 Predicted Water Quality Parameters

The following pollutants and indicators are predicted using the model:

- **O₂** (Dissolved Oxygen)  
- **NO₃** (Nitrates)  
- **NO₂** (Nitrites)  
- **SO₄** (Sulfates)  
- **PO₄** (Phosphates)  
- **Cl⁻** (Chlorides)

These parameters are essential in assessing water safety for human consumption, agriculture, and aquatic life.

---

## 🤖 Model & Methodology

- **Model Used**: Random Forest Regressor wrapped in a `MultiOutputRegressor` to handle multiple outputs simultaneously  
- **Input Features**:  
  - NH₄ (Ammonium)  
  - BSK5 (Biochemical Oxygen Demand over 5 days)  
  - Suspended Solids  
  - Year  
  - Month  

- **Handling Missing Data**: Median imputation  
- **Data Split**: 80% training, 20% testing  
- **Evaluation Metrics**:  
  - R² Score (Goodness of fit)  
  - Mean Squared Error (Prediction error)

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

> *(Note: Values are hypothetical placeholders — replace with your actual results from model evaluation)*

---

## ✅ Final Notes

This project demonstrates the effectiveness of machine learning in environmental applications, especially in water quality assessment. With further feature engineering and external data (e.g., rainfall, industrial zones, etc.), the model can be scaled and refined for larger systems.

---

**Built with 💻, ☕, and a splash of clean water by Madhumita Ash**
