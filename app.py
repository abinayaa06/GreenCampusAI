import streamlit as st

from ml_model import predict_risk

from agents import (
    energy_agent,
    water_agent,
    waste_agent,
    carbon_agent,
    planning_agent
)

from sustainability import (
    calculate_sustainability_score
)

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="GreenCampus AI",
    page_icon="🌱",
    layout="wide"
)

# =====================================
# CUSTOM STYLING
# =====================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    color: #2E8B57;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.title("🌱 GreenCampus AI")

st.markdown("""
### Agentic AI Sustainability Auditor

Analyze campus resource consumption and receive AI-powered sustainability insights, risk predictions, and action plans.
""")

st.divider()

# =====================================
# SDG ALIGNMENT
# =====================================

st.info("""
### 🌍 Supported Sustainable Development Goals

✅ SDG 7 – Affordable and Clean Energy

✅ SDG 11 – Sustainable Cities and Communities

✅ SDG 12 – Responsible Consumption and Production

✅ SDG 13 – Climate Action
""")

# =====================================
# INPUT SECTION
# =====================================

st.subheader("📋 Campus Resource Information")

col1, col2 = st.columns(2)

with col1:

    students = st.number_input(
        "Number of Students",
        min_value=1,
        value=500
    )

    electricity = st.number_input(
        "Monthly Electricity Usage (kWh)",
        min_value=0,
        value=3000
    )

with col2:

    water = st.number_input(
        "Monthly Water Usage (Liters)",
        min_value=0,
        value=100000
    )

    waste = st.number_input(
        "Monthly Waste Generated (kg)",
        min_value=0,
        value=500
    )

# =====================================
# ANALYSIS BUTTON
# =====================================

if st.button("🔍 Analyze Sustainability"):

    # =================================
    # AGENT EXECUTION
    # =================================

    energy_risk, energy_tips = energy_agent(
        electricity,
        students
    )

    water_risk, water_tips = water_agent(
        water,
        students
    )

    waste_risk, waste_tips = waste_agent(
        waste,
        students
    )

    carbon_emission = carbon_agent(
        electricity
    )

    action_plan = planning_agent(
        energy_risk,
        water_risk,
        waste_risk
    )

    sustainability_score = (
        calculate_sustainability_score(
            energy_risk,
            water_risk,
            waste_risk
        )
    )

    # =================================
    # MACHINE LEARNING PREDICTION
    # =================================

    predicted_risk = predict_risk(
        electricity,
        water,
        waste,
        students
    )

    # =================================
    # RESULTS
    # =================================

    st.success("✅ Sustainability Analysis Completed")

    st.subheader("🌱 Overall Sustainability Score")

    st.progress(sustainability_score)

    st.metric(
        "Sustainability Score",
        f"{sustainability_score}/100"
    )

    st.divider()

    # =================================
    # DASHBOARD
    # =================================

    st.subheader("📊 Sustainability Dashboard")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Energy Risk",
        energy_risk
    )

    c2.metric(
        "Water Risk",
        water_risk
    )

    c3.metric(
        "Waste Risk",
        waste_risk
    )

    c4.metric(
        "Carbon Emissions",
        f"{carbon_emission} kg"
    )

    c5.metric(
        "ML Prediction",
        predicted_risk
    )

    st.divider()

    # =================================
    # ML PREDICTION RESULT
    # =================================

    st.subheader("🤖 Machine Learning Risk Prediction")

    if predicted_risk == "High":

        st.error(
            "The ML model predicts a HIGH sustainability risk."
        )

    elif predicted_risk == "Medium":

        st.warning(
            "The ML model predicts a MEDIUM sustainability risk."
        )

    else:

        st.success(
            "The ML model predicts a LOW sustainability risk."
        )

    st.divider()

    # =================================
    # RECOMMENDATIONS
    # =================================

    st.subheader("💡 AI Recommendations")

    tab1, tab2, tab3 = st.tabs(
        [
            "⚡ Energy",
            "💧 Water",
            "♻ Waste"
        ]
    )

    with tab1:

        for tip in energy_tips:
            st.write("•", tip)

    with tab2:

        for tip in water_tips:
            st.write("•", tip)

    with tab3:

        for tip in waste_tips:
            st.write("•", tip)

    st.divider()

    # =================================
    # ACTION PLAN
    # =================================

    st.subheader("📝 Agentic AI Action Plan")

    for item in action_plan:
        st.write("✅", item)

    st.divider()

    # =================================
    # SUMMARY
    # =================================

    st.subheader("📌 Sustainability Summary")

    if sustainability_score >= 80:

        st.success(
            "Campus sustainability performance is excellent."
        )

    elif sustainability_score >= 60:

        st.warning(
            "Moderate sustainability performance detected."
        )

    else:

        st.error(
            "Immediate sustainability improvements are recommended."
        )

# =====================================
# AI WORKFLOW
# =====================================

with st.expander("🤖 How GreenCampus AI Works"):

    st.write("""
1. User enters campus resource consumption data.

2. Energy Agent analyzes electricity usage.

3. Water Agent analyzes water consumption.

4. Waste Agent analyzes waste generation.

5. Carbon Agent estimates environmental impact.

6. Machine Learning model predicts sustainability risk.

7. Planning Agent generates recommendations.

8. Sustainability report is displayed.
""")

# =====================================
# TECHNOLOGIES USED
# =====================================

with st.expander("🛠 AI Technologies Used"):

    st.write("""
• Agentic AI

• Multi-Agent System

• Machine Learning (Decision Tree Classifier)

• Sustainability Recommendation Engine

• Python

• Streamlit

• Scikit-Learn

• Pandas
""")

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "🌱 GreenCampus AI | Developed for the 1M1B AI for Sustainability Internship"
)

st.caption(
    "Technology Stack: Agentic AI | Machine Learning | Python | Streamlit | Scikit-Learn"
)