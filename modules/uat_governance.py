import streamlit as st
import pandas as pd
from datetime import date

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("UAT Governance")

st.markdown(
    "Enterprise User Acceptance Testing Governance & Signoff Management"
)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

f1, f2, f3, f4 = st.columns(4)

with f1:
    cycle = st.selectbox(
        "UAT Cycle",
        ["Cycle 1", "Cycle 2", "Cycle 3"],
        key="uat_cycle"
    )

with f2:
    workstream = st.selectbox(
        "Workstream",
        ["Finance", "SCM", "HCM"],
        key="uat_workstream"
    )

with f3:
    status = st.selectbox(
        "Status",
        ["All", "Open", "In Progress", "Completed"],
        key="uat_status"
    )

with f4:
    signoff = st.selectbox(
        "Signoff Status",
        ["Pending", "Approved", "Rejected"],
        key="uat_signoff"
    )

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("UAT KPIs")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric("Total Test Cases", "2,460")

with k2:
    st.metric("Executed", "1,980")

with k3:
    st.metric("Passed", "1,742")

with k4:
    st.metric("Failed", "238")

with k5:
    st.metric("Completion", "80%")

# ---------------------------------------------------
# TEST EXECUTION TABLE
# ---------------------------------------------------

st.subheader("UAT Execution Tracker")

uat_df = pd.DataFrame([
    {
        "Test Case": "AP Invoice Processing",
        "Workstream": "Finance",
        "Status": "Passed",
        "Executed By": "Business User",
        "Cycle": "Cycle 1",
        "Signoff": "Approved"
    },
    {
        "Test Case": "PO Approval Workflow",
        "Workstream": "SCM",
        "Status": "Failed",
        "Executed By": "SCM Lead",
        "Cycle": "Cycle 1",
        "Signoff": "Pending"
    }
])

st.dataframe(
    uat_df,
    use_container_width=True
)

# ---------------------------------------------------
# LOG TEST RESULT
# ---------------------------------------------------

st.subheader("Log UAT Result")

c1, c2 = st.columns(2)

with c1:

    test_case = st.text_input("Test Case")

    cycle_name = st.selectbox(
        "Cycle",
        ["Cycle 1", "Cycle 2", "Cycle 3"],
        key="form_cycle"
    )

    executed_by = st.text_input("Executed By")

    workstream_name = st.selectbox(
        "Workstream",
        ["Finance", "SCM", "HCM"],
        key="form_workstream"
    )

with c2:

    execution_status = st.selectbox(
        "Execution Status",
        ["Passed", "Failed", "Blocked"],
        key="form_execution_status"
    )

    execution_date = st.date_input(
        "Execution Date",
        date.today()
    )

    signoff_status = st.selectbox(
        "Signoff Status",
        ["Pending", "Approved", "Rejected"],
        key="form_signoff_status"
    )

comments = st.text_area("Business Comments")

if st.button("Save UAT Result"):

    st.success(
        "UAT result saved successfully"
    )

# ---------------------------------------------------
# AI INSIGHTS
# ---------------------------------------------------

st.subheader("AI UAT Insights")

st.warning(
    "Finance UAT completion trending below target"
)

st.error(
    "Critical SCM defects may delay business signoff"
)

st.info(
    "UAT execution velocity improved by 15%"
)

# ---------------------------------------------------
# GO-LIVE READINESS
# ---------------------------------------------------

st.subheader("Go-Live Readiness")

st.progress(78)

st.info(
    "Overall UAT readiness currently at 78%"
)

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

st.subheader("Upload UAT Evidence")

uploaded_file = st.file_uploader(
    "Upload Signoff / Evidence",
    type=["xlsx", "csv", "pdf", "docx"]
)

if uploaded_file:

    st.success(
        "UAT evidence uploaded successfully"
    )