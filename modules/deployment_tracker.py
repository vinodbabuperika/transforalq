import streamlit as st
import pandas as pd
from datetime import date

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("Deployment Tracker")

st.markdown(
    "Enterprise Deployment Governance, Cutover & Go-Live Control Tower"
)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

f1, f2, f3, f4 = st.columns(4)

with f1:
    environment = st.selectbox(
        "Environment",
        ["SIT", "UAT", "Pre-Prod", "Production"],
        key="deploy_environment"
    )

with f2:
    deployment_wave = st.selectbox(
        "Deployment Wave",
        ["Wave 1", "Wave 2", "Wave 3"],
        key="deploy_wave"
    )

with f3:
    status = st.selectbox(
        "Deployment Status",
        ["All", "Open", "In Progress", "Completed", "Blocked"],
        key="deploy_status"
    )

with f4:
    readiness = st.selectbox(
        "Go-Live Readiness",
        ["Green", "Amber", "Red"],
        key="deploy_readiness"
    )

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Deployment KPIs")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric("Deployment Activities", "184")

with k2:
    st.metric("Completed", "132")

with k3:
    st.metric("Blocked", "11")

with k4:
    st.metric("Rollback Risks", "4")

with k5:
    st.metric("Readiness", "82%")

# ---------------------------------------------------
# DEPLOYMENT TABLE
# ---------------------------------------------------

st.subheader("Deployment Activity Tracker")

deploy_df = pd.DataFrame([
    {
        "Activity": "Production Code Migration",
        "Environment": "Production",
        "Owner": "Release Manager",
        "Status": "In Progress",
        "Wave": "Wave 1",
        "Readiness": "Amber"
    },
    {
        "Activity": "Integration Validation",
        "Environment": "Pre-Prod",
        "Owner": "Integration Lead",
        "Status": "Completed",
        "Wave": "Wave 1",
        "Readiness": "Green"
    }
])

st.dataframe(
    deploy_df,
    use_container_width=True
)

# ---------------------------------------------------
# CUTOVER TASK ENTRY
# ---------------------------------------------------

st.subheader("Add Deployment Activity")

c1, c2 = st.columns(2)

with c1:

    activity = st.text_input("Deployment Activity")

    env = st.selectbox(
        "Target Environment",
        ["SIT", "UAT", "Pre-Prod", "Production"],
        key="form_env"
    )

    owner = st.text_input("Activity Owner")

    wave = st.selectbox(
        "Deployment Wave",
        ["Wave 1", "Wave 2", "Wave 3"],
        key="form_wave"
    )

with c2:

    deploy_status = st.selectbox(
        "Activity Status",
        ["Open", "In Progress", "Completed", "Blocked"],
        key="form_deploy_status"
    )

    deploy_date = st.date_input(
        "Deployment Date",
        date.today()
    )

    readiness_status = st.selectbox(
        "Readiness Status",
        ["Green", "Amber", "Red"],
        key="form_readiness"
    )

rollback_plan = st.text_area("Rollback Plan")

deployment_notes = st.text_area("Deployment Notes")

if st.button("Save Deployment Activity"):

    st.success(
        "Deployment activity saved successfully"
    )

# ---------------------------------------------------
# GO-LIVE READINESS
# ---------------------------------------------------

st.subheader("Go-Live Readiness Dashboard")

st.progress(82)

st.success(
    "Overall deployment readiness at 82%"
)

# ---------------------------------------------------
# AI INSIGHTS
# ---------------------------------------------------

st.subheader("AI Deployment Insights")

st.warning(
    "Integration validation delays may impact production cutover"
)

st.error(
    "Rollback risk identified for Finance deployment sequence"
)

st.info(
    "Deployment execution velocity improved across Wave 1"
)

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

st.subheader("Upload Deployment Evidence")

uploaded_file = st.file_uploader(
    "Upload Cutover Plan / Validation Evidence",
    type=["xlsx", "csv", "pdf", "docx"]
)

if uploaded_file:

    st.success(
        "Deployment evidence uploaded successfully"
    )