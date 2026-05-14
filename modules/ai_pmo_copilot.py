import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("AI PMO Copilot")

st.markdown(
    "AI-Powered Enterprise Transformation Intelligence & Executive Advisory"
)

# ---------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------

st.subheader("AI Executive Summary")

st.success("""
Overall ERP transformation health remains stable.

Key observations:
• Finance SIT defects increased by 8%
• UAT completion currently at 80%
• Migration readiness improved to 88%
• Deployment risks identified for Wave 1 cutover
• Critical dependencies impacting SCM workstream
""")

# ---------------------------------------------------
# AI RISK INSIGHTS
# ---------------------------------------------------

st.subheader("AI Risk Intelligence")

risk_df = pd.DataFrame([
    {
        "Risk": "SIT Delay",
        "Probability": "High",
        "Impact": "High",
        "Recommendation": "Increase testing resources"
    },
    {
        "Risk": "Migration Failure",
        "Probability": "Medium",
        "Impact": "Critical",
        "Recommendation": "Run reconciliation validation"
    },
    {
        "Risk": "Deployment Rollback",
        "Probability": "Low",
        "Impact": "High",
        "Recommendation": "Validate rollback scripts"
    }
])

st.dataframe(
    risk_df,
    use_container_width=True
)

# ---------------------------------------------------
# GO-LIVE READINESS
# ---------------------------------------------------

st.subheader("AI Go-Live Readiness")

st.progress(82)

st.info(
    "AI predicts go-live readiness currently at 82%"
)

# ---------------------------------------------------
# AI RECOMMENDATIONS
# ---------------------------------------------------

st.subheader("AI Recommended Actions")

st.warning(
    "Prioritize closure of critical Finance SIT defects"
)

st.warning(
    "Accelerate SCM UAT execution to avoid schedule slippage"
)

st.warning(
    "Perform additional migration reconciliation before cutover"
)

# ---------------------------------------------------
# EXECUTIVE Q&A
# ---------------------------------------------------

st.subheader("Ask AI PMO Copilot")

question = st.text_input(
    "Ask a transformation question"
)

if st.button("Generate AI Insight"):

    if question:

        st.info(f"""
AI Insight for:
'{question}'

Current transformation indicators suggest moderate deployment risk.

Recommended focus areas:
• SIT stabilization
• Migration reconciliation
• UAT acceleration
• Deployment sequencing validation
""")

# ---------------------------------------------------
# AI TRANSFORMATION METRICS
# ---------------------------------------------------

st.subheader("AI Transformation Metrics")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Transformation Health", "Green")

with m2:
    st.metric("AI Risk Score", "72")

with m3:
    st.metric("Go-Live Confidence", "82%")

with m4:
    st.metric("Delay Probability", "18%")

# ---------------------------------------------------
# AI TREND INSIGHTS
# ---------------------------------------------------

st.subheader("AI Trend Analysis")

trend_df = pd.DataFrame([
    {
        "Area": "SIT Defects",
        "Trend": "Increasing",
        "Observation": "8% increase this week"
    },
    {
        "Area": "UAT Execution",
        "Trend": "Improving",
        "Observation": "15% faster execution"
    },
    {
        "Area": "Migration Accuracy",
        "Trend": "Stable",
        "Observation": "98.7% reconciliation accuracy"
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
    "AI PMO Copilot operational successfully"
)