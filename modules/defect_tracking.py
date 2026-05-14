import streamlit as st
import pandas as pd
from datetime import date

from services.db_service import (
    fetch_data,
    execute_query
)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("Defect Tracking")

st.markdown(
    "Enterprise SIT/UAT Defect Governance & Resolution Tracking"
)

# ---------------------------------------------------
# CREATE DEFECT
# ---------------------------------------------------

st.subheader("Log New Defect")

c1, c2 = st.columns(2)

with c1:

    defect_title = st.text_input(
        "Defect Title"
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

    owner = st.text_input(
        "Assigned Owner"
    )

    environment = st.selectbox(
        "Environment",
        [
            "SIT",
            "UAT",
            "Pre-Prod"
        ]
    )

with c2:

    defect_status = st.selectbox(
        "Defect Status",
        [
            "Open",
            "In Progress",
            "Resolved",
            "Closed"
        ]
    )

    defect_date = st.date_input(
        "Raised Date",
        date.today()
    )

    workstream = st.selectbox(
        "Workstream",
        [
            "Finance",
            "SCM",
            "HCM"
        ]
    )

root_cause = st.text_area(
    "Root Cause"
)

resolution = st.text_area(
    "Resolution"
)

# ---------------------------------------------------
# SAVE DEFECT
# ---------------------------------------------------

if st.button(
    "Save Defect",
    key="save_defect"
):

    execute_query(
        """
        INSERT INTO defect_tracker (
            defect_title,
            severity,
            owner,
            environment,
            defect_status,
            workstream,
            defect_date,
            root_cause,
            resolution
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            defect_title,
            severity,
            owner,
            environment,
            defect_status,
            workstream,
            str(defect_date),
            root_cause,
            resolution
        )
    )

    st.success(
        "Defect logged successfully"
    )

# ---------------------------------------------------
# DEFECT TABLE
# ---------------------------------------------------

st.subheader("Defect Register")

df = fetch_data(
    "SELECT * FROM defect_tracker"
)

st.dataframe(
    df,
    use_container_width=True
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Defect KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Defects",
        len(df)
    )

with k2:

    critical = len(
        df[df["severity"] == "Critical"]
    ) if not df.empty else 0

    st.metric(
        "Critical",
        critical
    )

with k3:

    open_defects = len(
        df[df["defect_status"] == "Open"]
    ) if not df.empty else 0

    st.metric(
        "Open",
        open_defects
    )

with k4:

    closed = len(
        df[df["defect_status"] == "Closed"]
    ) if not df.empty else 0

    st.metric(
        "Closed",
        closed
    )

# ---------------------------------------------------
# AI INSIGHTS
# ---------------------------------------------------

st.subheader("AI Defect Insights")

st.warning(
    "Critical Finance defects impacting SIT closure"
)

st.error(
    "Open integration defects may delay UAT readiness"
)

st.info(
    "Defect closure velocity improved this week"
)

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

st.subheader("Upload Defect Evidence")

uploaded_file = st.file_uploader(
    "Upload Logs / Screenshots / Evidence",
    type=["xlsx", "csv", "pdf", "png", "jpg"]
)

if uploaded_file:

    st.success(
        "Evidence uploaded successfully"
    )