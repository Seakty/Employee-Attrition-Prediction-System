import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="HR Analytics: Attrition Predictor",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOAD MODEL ASSETS ---
@st.cache_resource
def load_assets():
    try:
        model = joblib.load('champion_model.pkl')
        model_cols = joblib.load('model_columns.pkl')
        return model, model_cols
    except FileNotFoundError:
        st.error("⚠️ Model files not found! Please run the notebook script to save 'champion_model.pkl' and 'model_columns.pkl'.")
        return None, None

model, model_cols = load_assets()

# --- SIDEBAR: KEY DRIVERS ---
st.sidebar.header("🔧 Employee Scenario Settings")
st.sidebar.markdown("Adjust key factors to see how they impact retention risk.")

# Group 1: The "High Impact" Variables (Based on your Feature Importance)
st.sidebar.subheader("💰 Incentives & Level")
monthly_income = st.sidebar.number_input("Monthly Income ($)", min_value=1000, max_value=20000, value=5000, step=500)
incentive_amount = st.sidebar.number_input("Incentive/Bonus Amount ($)", min_value=0, max_value=5000, value=200, step=100)
job_level = st.sidebar.slider("Job Level (1-5)", 1, 5, 2)
stock_option = st.sidebar.slider("Stock Option Level (0-3)", 0, 3, 1)

st.sidebar.subheader("😰 Stress & Environment")
stress_rating = st.sidebar.slider("Stress Rating (1-4)", 1, 4, 3)
env_satisfaction = st.sidebar.slider("Environment Satisfaction (1-4)", 1, 4, 3)
overtime = st.sidebar.selectbox("Works Overtime?", ["No", "Yes"])

st.sidebar.subheader("👤 Demographics & Tenure")
age = st.sidebar.slider("Age", 18, 60, 30)
years_at_company = st.sidebar.slider("Years at Company", 0, 40, 5)
years_with_manager = st.sidebar.slider("Years with Current Manager", 0, 20, 3)

# --- MAIN DASHBOARD ---
st.title("📊 Employee Attrition Prediction System")
st.markdown("""
This tool uses an **XGBoost Classifier** to predict employee turnover. 
It incorporates advanced feature engineering including **Incentive Ratio** and **Stress-to-Level Ratio**.
""")

st.markdown("---")

# --- PRE-PROCESSING & FEATURE ENGINEERING ---
if st.button("🚀 Run Prediction Analysis", type="primary"):
    if model:
        # 1. Create Dictionary of Inputs (Defaulting 'average' values for the hidden 30+ columns)
        # NOTE: In a real app, you might want more inputs, but for a demo, we fill the rest with averages/modes.
        input_data = {col: 0 for col in model_cols} # Initialize all with 0
        
        # 2. Update with User Inputs
        input_data['MonthlyIncome'] = monthly_income
        input_data['Incentive'] = incentive_amount
        input_data['JobLevel'] = job_level
        input_data['StockOptionLevel'] = stock_option
        input_data['StressRating'] = stress_rating
        input_data['EnvironmentSatisfaction'] = env_satisfaction
        input_data['OverTime'] = 1 if overtime == "Yes" else 0
        input_data['Age'] = age
        input_data['YearsAtCompany'] = years_at_company
        input_data['YearsWithCurrManager'] = years_with_manager
        
        # 3. APPLY YOUR FEATURE ENGINEERING (Crucial Step!)
        # Recreating the logic from your notebook:
        input_data['Incentive_Ratio'] = input_data['Incentive'] / (input_data['MonthlyIncome'] + 1)
        input_data['Unjustified_Stress'] = input_data['StressRating'] / input_data['JobLevel']

        # 4. Convert to DataFrame and Ensure Column Order
        df_input = pd.DataFrame([input_data])
        df_input = df_input[model_cols] # Enforce order

        # 5. Prediction
        prediction = model.predict(df_input)[0]
        probability = model.predict_proba(df_input)[0][1] # Probability of Class 1 (Yes)

        # --- VISUALIZATION SECTION ---
        col1, col2 = st.columns([1, 2])

        with col1:
            # Gauge Chart for Risk
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = probability * 100,
                title = {'text': "Attrition Probability"},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 40], 'color': "lightgreen"},
                        {'range': [40, 70], 'color': "orange"},
                        {'range': [70, 100], 'color': "red"}],
                }
            ))
            fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📋 Prediction Result")
            if prediction == 1:
                st.error(f"⚠️ **High Risk:** This employee is likely to leave.")
                st.markdown(f"**Key Risk Factor:** The calculated **Incentive Ratio** is `{input_data['Incentive_Ratio']:.3f}`.")
                if input_data['Incentive_Ratio'] < 0.05:
                    st.caption("ℹ️ *Insight: The bonus is too small relative to their salary.*")
            else:
                st.success(f"✅ **Safe:** This employee is likely to stay.")
            
            # ROI Calculator Logic
            st.subheader("💰 Financial Impact Analysis")
            # SHRM standard: Cost to replace is ~150% of annual salary
            annual_salary = monthly_income * 12
            replacement_cost = annual_salary * 1.5
            
            st.info(f"""
            If this employee leaves, the estimated replacement cost is **${replacement_cost:,.2f}**.
            *(Based on SHRM standard of 1.5x Annual Salary)*
            """)

    else:
        st.warning("Please ensure model files are in the same directory.")

# --- FOOTER ---
st.markdown("---")
st.caption("Developed by Seakty | Data Science Major | Model: XGBoost (Accuracy: 89%)")