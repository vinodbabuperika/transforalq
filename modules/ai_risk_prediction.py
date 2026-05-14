import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("AI Risk Prediction")

st.markdown(
    "Predictive ERP Transformation Risk Intelligence & Forecasting"
)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

f1, f2, f3 = st.columns(3)

with f1:
    workstream = st.selectbox(
        "Workstream",
        ["Finance", "SCM", "HCM"],
        key="risk_workstream"
    )

with f2:
    phase = st.selectbox(
        "Project Phase",
        ["Design", "Build", "SIT", "UAT", "Deployment"],
        key="risk_phase"
    )

with f3:
    risk_window = st.selectbox(
        "Prediction Window",
        ["7 Days", "14 Days", "30 Days"],
        key="risk_window"
    )

# ---------------------------------------------------
# AI RISK SCORECARDS
# ---------------------------------------------------

st.subheader("AI Risk Forecast")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric("Overall Risk Score", "72")

with k2:
    st.metric("Delay Probability", "18%")

with k3:
    st.metric("Deployment Risk", "Medium")

with k4:
    st.metric("Go-Live Confidence", "82%")

# ---------------------------------------------------
# RISK PREDICTION TABLE
# ---------------------------------------------------

st.subheader("Predicted Transformation Risks")

risk_df = pd.DataFrame([
    {
        "Risk Area": "Finance SIT",
        "Probability": "High",
        "Impact": "High",
        "Prediction": "UAT entry delay likely",
        "Recommended Action": "Increase SIT closure capacity"
    },
    {
        "Risk Area": "Migration Validation",
        "Probability": "Medium",
        "Impact": "Critical",
        "Prediction": "Reconciliation mismatches possible",
        "Recommended Action": "Perform additional validation cycles"
    },
    {
        "Risk Area": "Deployment Readiness",
        "Probability": "Low",
        "Impact": "High",
        "Prediction": "Rollback dependency identified",
        "Recommended Action": "Validate rollback sequencing"
    }
])

st.dataframe(
    risk_df,
    use_container_width=True
)

# ---------------------------------------------------
# AI HEATMAP INSIGHTS
# ---------------------------------------------------

st.subheader("AI Risk Heatmap")

heatmap_df = pd.DataFrame([
    {
        "Workstream": "Finance",
        "Risk": "High",
        "Trend": "Increasing"
    },
    {
        "Workstream": "SCM",
        "Risk": "Medium",
        "Trend": "Stable"
    },
    {
        "Workstream": "HCM",
        "Risk": "Low",
        "Trend": "Improving"
    }
])

st.dataframe(
    heatmap_df,
    use_container_width=True
)

# ---------------------------------------------------
# AI RECOMMENDATIONS
# ---------------------------------------------------

st.subheader("AI Mitigation Recommendations")

st.warning(
    "Accelerate Finance SIT defect triage immediately"
)

st.warning(
    "Increase migration reconciliation validation coverage"
)

st.info(
    "Deployment readiness improving across Wave 1"
)

st.success(
    "HCM workstream stabilization achieved"
)

# ---------------------------------------------------
# EXECUTIVE FORECAST
# ---------------------------------------------------

st.subheader("Executive Forecast Summary")

st.error("""
AI forecast indicates moderate risk to deployment timelines.

Key prediction indicators:
• SIT stabilization needed within 2 weeks
• Migration reconciliation risk remains elevated
• UAT completion improving steadily
• Deployment readiness projected to reach 90%
""")

# ---------------------------------------------------
# AI PREDICTION QUERY
# ---------------------------------------------------

st.subheader("Ask AI Risk Predictor")

question = st.text_input(
    "Ask predictive risk question"
)

if st.button("Generate Prediction"):

    if question:

        st.info(f"""
AI Prediction for:
'{question}'

Forecast Summary:
• Moderate delivery risk detected
• SIT completion trending behind baseline
• UAT execution improving gradually
• Deployment stabilization achievable with mitigation actions
""")

# ---------------------------------------------------
# TREND ANALYTICS
# ---------------------------------------------------

st.subheader("AI Trend Analytics")

trend_df = pd.DataFrame([
    {
        "Area": "Defect Closure",
        "Trend": "Improving",
        "Observation": "12% improvement this week"
    },
    {
        "Area": "Migration Accuracy",
        "Trend": "Stable",
        "Observation": "98.7% accuracy maintained"
    },
    {
        "Area": "UAT Completion",
        "Trend": "Increasing",
        "Observation": "15% acceleration observed"
    }
])

st.dataframe(
    trend_df,
    use_container_width=True
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.success(
    "AI Risk Prediction Engine operational successfully"
)