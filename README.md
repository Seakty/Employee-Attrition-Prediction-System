# Employee Attrition Prediction System 👔

[![Live Demo](https://img.shields.io/badge/demo-streamlit-FF4B4B?style=flat-square)](https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/) [![Repository](https://img.shields.io/badge/repo-github-black?style=flat-square)](https://github.com/Seakty/Employee-Attrition-Prediction-System) [![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square)](https://www.python.org) [![XGBoost](https://img.shields.io/badge/model-XGBoost-green?style=flat-square)](https://xgboost.readthedocs.io/)

An interactive web application that predicts employee attrition risk using machine learning. Identify at-risk employees, analyze retention factors, and estimate financial impact of turnover.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Live Demo](#live-demo)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Troubleshooting](#troubleshooting)

---

## Overview

Employee attrition is costly. This system uses **XGBoost** to predict which employees are at risk of leaving based on company HR data. The interactive Streamlit app allows HR teams to:

- 📊 Predict attrition probability for any employee profile
- 🔍 Explore "what-if" scenarios by adjusting key factors
- 💰 Calculate replacement costs and financial impact
- 📈 Identify the top drivers of employee retention

The model was trained on HR analytics data with advanced feature engineering including incentive ratios and stress-level measurements.

## Features

✅ **Interactive Web Dashboard** — Built with Streamlit for easy scenario analysis  
✅ **XGBoost Classifier** — High-accuracy binary classification model  
✅ **Custom Feature Engineering** — Incentive Ratio, Unjustified Stress, and more  
✅ **Gauge Visualization** — Real-time attrition probability display  
✅ **ROI Calculator** — Estimate replacement costs based on salary data  
✅ **Live Deployment** — No installation required, accessible from any browser  
✅ **Configurable Inputs** — Adjust income, tenure, incentives, and stress levels in the sidebar

## Live Demo

**[🚀 Try the Live Application](https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/)**

No setup needed. Visit the link above and start analyzing attrition risk immediately!

## Getting Started

### Quickest Way: Use the Live App 🌐

Visit **[https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/](https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/)** and start analyzing immediately. No installation required.

### Run Locally

If you prefer to run the app on your own machine:

**Prerequisites:**
- Python 3.10 or higher
- Git

**Installation:**

```bash
# Clone the repository
git clone https://github.com/Seakty/Employee-Attrition-Prediction-System.git
cd Employee-Attrition-Prediction-System/"Final Competition"

# Create a virtual environment
python -m venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Usage Guide

1. **Adjust Employee Profile** — Use the sidebar to input employee details:
   - Monthly Income
   - Incentive/Bonus Amount
   - Job Level & Stock Options
   - Stress Rating & Environment Satisfaction
   - Work Schedule (Overtime Yes/No)
   - Age & Tenure Information

2. **Run Prediction** — Click the "Run Prediction Analysis" button

3. **View Results**:
   - **Attrition Gauge** — Shows probability (0–100%) with color zones
   - **Prediction Label** — "High Risk" (red) or "Safe" (green)
   - **Financial Analysis** — Estimated replacement cost at 1.5× annual salary

4. **Iterate** — Try different scenarios to understand which factors impact retention most

## Project Structure

```
Final Competition/
├── app.py                      # Streamlit application (main entry point)
├── 25ITC_SSeakty.ipynb        # Training notebook with EDA, model building, and export
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
├── dataset/
│   └── data.csv               # Sample HR dataset (for reference)
└── reports/
    └── 25ITC_SSeakty.pdf      # Project report with analysis and methodology
```

**Key Files:**
- **`app.py`** — Streamlit web app; handles user input, predictions, and visualization
- **`25ITC_SSeakty.ipynb`** — Jupyter notebook containing data analysis, model training, and feature engineering
- **`reports/25ITC_SSeakty.pdf`** — Detailed project report documenting the analysis approach, model performance, and recommendations
- **`dataset/data.csv`** — Example HR data (structure reference only)
- **Model artifacts** — `champion_model.pkl` and `model_columns.pkl` must be present in the same directory as `app.py` for the app to run

## Model Details

### Algorithm
- **Model Type:** XGBoost Binary Classifier
- **Target:** Employee Attrition (Yes/No)
- **Reported Accuracy:** 89%

### Key Features Used
- **Compensation:** Monthly Income, Incentive/Bonus
- **Role:** Job Level, Stock Option Level
- **Work Environment:** Stress Rating, Environment Satisfaction, Overtime Status
- **Tenure:** Years at Company, Years with Current Manager
- **Demographics:** Age

### Custom Engineering
- **Incentive_Ratio** = Incentive / (Monthly Income + 1)
- **Unjustified_Stress** = Stress Rating / Job Level

These engineered features capture the relationship between compensation adequacy and employee stress levels.

### Model Files
For the app to run, the following model artifacts must be present:
- `champion_model.pkl` — Serialized XGBoost model
- `model_columns.pkl` — Feature list in correct order

If missing, the app displays an error with regeneration instructions.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Model files not found** | Ensure `champion_model.pkl` and `model_columns.pkl` are in the same directory as `app.py`. Generate them by running the Jupyter notebook. |
| **Module import errors** | Create a fresh virtual environment and run `pip install -r requirements.txt` |
| **Streamlit connection issues** | Clear browser cache or restart the Streamlit server with `streamlit run app.py --logger.level=debug` |
| **Slow predictions** | Check system resources (RAM, CPU). First prediction may be slower due to model loading. |

## About This Project

This system was developed as a data science project to demonstrate:
- **Machine Learning** — Classification with XGBoost
- **Feature Engineering** — Creating meaningful predictors from HR data
- **Web Application Development** — Interactive UI with Streamlit
- **Data Analysis** — Exploratory analysis and model interpretation

**Developed by:** Seakty  
**Dataset:** HR Analytics Sample Data  
**Deployment Platform:** Streamlit Cloud

---

## License & Usage

This project is provided for educational and demonstration purposes. The model should be validated with your own HR data before production use. Ensure compliance with employment laws and data privacy regulations when analyzing employee information.

## Feedback & Improvements

Found a bug? Have a suggestion? Feel free to:
- Open an issue on [GitHub](https://github.com/Seakty/Employee-Attrition-Prediction-System/issues)
- Submit a pull request with improvements
- Contact the developer for collaboration

---

**Repository:** [github.com/Seakty/Employee-Attrition-Prediction-System](https://github.com/Seakty/Employee-Attrition-Prediction-System)  
**Live App:** [employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app](https://employee-attrition-prediction-system-bbpmbigdiufpffkzwv5gbk.streamlit.app/)
