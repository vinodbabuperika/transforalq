import streamlit as st
import pandas as pd

from datetime import date

from database.db import (
    execute_query,
    fetch_data
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("Hypercare Governance")

st.markdown(
    "Enterprise Go-Live Stabilization "
    "& Production Support Governance"
)

# =====================================================
# FILE UPLOAD
# =====================================================

st.subheader("Upload Hypercare Tracker")

uploaded_file = st.file_uploader(
    "Upload Hypercare Excel",
    type=["xlsx", "csv"]
)

if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):

            upload_df = pd.read_csv(
                uploaded_file
            )

        else:

            upload_df = pd.read_excel(
                uploaded_file
            )

        st.success(
            "Hypercare tracker uploaded"
        )

        st.dataframe(
            upload_df.head(),
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Upload Error: {e}"
        )

# =====================================================
# MANUAL INCIDENT ENTRY
# =====================================================

st.markdown("---")

st.subheader("Create Hypercare Incident")

with st.form("hypercare_form"):

    c1, c2 = st.columns(2)

    with c1:

        incident_id = st.text_input(
            "Incident ID"
        )

        issue_type = st.selectbox(

            "Issue Type",

            [
                "Production Defect",
                "Performance",
                "Integration",
                "Security",
                "User Access",
                "Data"
            ]
        )

        severity = st.selectbox(

            "Severity",

            [
                "Critical",
                "High",
                "Medium",
                "Low"
            ]
        )

        business_impact = st.text_area(
            "Business Impact"
        )

        reported_by = st.text_input(
            "Reported By"
        )

        assigned_team = st.text_input(
            "Assigned Team"
        )

    with c2:

        issue_status = st.selectbox(

            "Issue Status",

            [
                "Open",
                "In Progress",
                "Resolved",
                "Closed"
            ]
        )

        expected_resolution = st.date_input(
            "Expected Resolution",
            date.today()
        )

        actual_resolution = st.date_input(
            "Actual Resolution",
            date.today()
        )

        sla_status = st.selectbox(

            "SLA Status",

            [
                "Within SLA",
                "SLA Risk",
                "SLA Breached"
            ]
        )

        remarks = st.text_area(
            "Remarks"
        )

    submitted = st.form_submit_button(
        "Create Incident"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO hypercare_issues (

                incident_id,
                issue_type,
                severity,
                business_impact,
                reported_by,
                assigned_team,
                issue_status,
                reported_date,
                expected_resolution,
                actual_resolution,
                sla_status,
                remarks

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                incident_id,
                issue_type,
                severity,
                business_impact,
                reported_by,
                assigned_team,
                issue_status,
                str(date.today()),
                str(expected_resolution),
                str(actual_resolution),
                sla_status,
                remarks

            )
        )

        st.success(
            "Hypercare incident created"
        )

# =====================================================
# INCIDENT REGISTER
# =====================================================

st.subheader("Hypercare Incident Register")

df = fetch_data(
    "SELECT * FROM hypercare_issues"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("Hypercare KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Incidents",
        len(df)
    )

with k2:

    critical = len(

        df[
            df["severity"]
            == "Critical"
        ]

    ) if not df.empty else 0

    st.metric(
        "Critical",
        critical
    )

with k3:

    open_issues = len(

        df[
            df["issue_status"]
            == "Open"
        ]

    ) if not df.empty else 0

    st.metric(
        "Open",
        open_issues
    )

with k4:

    breached = len(

        df[
            df["sla_status"]
            == "SLA Breached"
        ]

    ) if not df.empty else 0

    st.metric(
        "SLA Breached",
        breached
    )

# =====================================================
# AI STABILIZATION INSIGHTS
# =====================================================

st.subheader("AI Stabilization Insights")

if critical > 5:

    st.error(
        "Production stabilization risk HIGH"
    )

elif critical > 2:

    st.warning(
        "Critical incidents increasing"
    )

else:

    st.success(
        "Production stabilization healthy"
    )

if breached > 3:

    st.error(
        "SLA governance breach detected"
    )

st.success(
    "Hypercare governance operational"
)