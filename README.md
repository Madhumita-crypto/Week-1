
# 🌊 Water Quality Prediction Using Machine Learning

### *Week 2 – Shell–Edunet Skills4Future AI-ML Internship (June–July 2025)*

> **“From numbers in rivers to narratives of health — decoding water’s silent signals through AI.”**

---

## 📌 Project Overview

This project focuses on **predicting key water quality parameters** using historical chemical data collected across 22 water monitoring stations in Punjab from 2000 to 2021. It was developed as part of the **Shell–Edunet AI-ML Internship** and serves as my **first hands-on machine learning project**.

By leveraging data-driven models, the goal is to **estimate pollution levels** and enable proactive **environmental monitoring**, helping authorities ensure safer, cleaner, and more sustainable water bodies.

---

## 💡 Motivation

With increasing industrialization and environmental stressors, access to clean water is no longer a guarantee. **Data science and machine learning** can empower decision-makers by offering timely insights into **chemical pollution trends**, enabling both **early warning systems** and **policy-oriented responses**.

---

## ⚙️ Technologies & Tools

| Category          | Tools Used                                                     |
| ----------------- | -------------------------------------------------------------- |
| Programming       | Python                                                         |
| Data Wrangling    | Pandas, NumPy                                                  |
| Visualization     | Matplotlib, Seaborn                                            |
| Machine Learning  | Scikit-learn (`RandomForestRegressor`, `MultiOutputRegressor`) |
| Model Persistence | Joblib (`.pkl` files for model & column structure)             |

---

## 💧 Predicted Water Quality Parameters

The machine learning model predicts the concentration of the following key water pollutants:

* **O₂** (Dissolved Oxygen)
* **NO₃** (Nitrates)
* **NO₂** (Nitrites)
* **SO₄** (Sulfates)
* **PO₄** (Phosphates)
* **Cl⁻** (Chlorides)

These indicators are critical for assessing water quality for **drinking, agriculture, aquatic health, and ecosystem balance**.

---

## 📊 Dataset Overview

* 📍 **Region**: Punjab, India
* 🗓️ **Duration**: 2000–2021
* 🧪 **Parameters**: 13 columns (Date, Station ID, Chemical Attributes)
* 📉 **Target Columns**: O₂, NO₃, NO₂, SO₄, PO₄, CL
* 🔄 **Handling Missing Data**: Median Imputation or Dropping (based on target presence)

---

## 🤖 Machine Learning Pipeline

| Step                      | Description                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------- |
| **1. Data Cleaning**      | Converted `date` column to datetime; extracted `year` & `month`; sorted by station    |
| **2. Feature Selection**  | Used: `NH₄`, `BSK5`, `Suspended`, `year`, `month` as features                         |
| **3. Target Selection**   | `O₂`, `NO₃`, `NO₂`, `SO₄`, `PO₄`, `CL`                                                |
| **4. Model Architecture** | MultiOutput Random Forest Regressor                                                   |
| **5. Evaluation Metrics** | R² Score and Mean Squared Error (MSE)                                                 |
| **6. Serialization**      | Saved trained model as `pollution_model.pkl`, column structure as `model_columns.pkl` |

---

## 📈 Sample Model Performance (Hypothetical)

> Replace these with your actual values from evaluation step.

| Pollutant | R² Score | MSE   |
| --------- | -------- | ----- |
| O₂        | 0.83     | 3.01  |
| NO₃       | 0.84     | 2.17  |
| NO₂       | 0.75     | 0.11  |
| SO₄       | 0.89     | 114.8 |
| PO₄       | 0.82     | 0.06  |
| CL        | 0.92     | 132.4 |

---

## 📦 Files Generated

| File                            | Purpose                         |
| ------------------------------- | ------------------------------- |
| `pollution_model.pkl`           | Saved trained model for reuse   |
| `model_columns.pkl`             | Stores feature column structure |
| `Water_Quality_Predictor.ipynb` | Main Jupyter Notebook with code |
| `PB_All_2000_2021.csv`          | Original dataset                |

---

## 🚀 Key Learnings

* Understood how real-world data can be noisy and sparse.
* Learned to implement MultiOutput regressors and deal with missing values.
* Practiced model serialization for deployment readiness.
* Experienced the end-to-end lifecycle of an ML regression project.

---

## 🔮 Future Scope

* Include **external environmental data** like rainfall, industrial zones, river discharge.
* Apply **time-series modeling** for temporal trend analysis.
* Deploy the model using **Streamlit** or a Flask web app for real-time predictions.
* Incorporate **alert thresholds** to flag dangerous pollution levels.

---
