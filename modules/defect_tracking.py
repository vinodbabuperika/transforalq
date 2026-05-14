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

st.title("Defect Management")

st.markdown(
    "Enterprise SIT/UAT Defect Governance"
)

# =====================================================
# FILE UPLOAD
# =====================================================

st.subheader("Upload Defect Log")

uploaded_file = st.file_uploader(
    "Upload Defect Excel",
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
            "Defect file uploaded successfully"
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
# MANUAL DEFECT ENTRY
# =====================================================

st.markdown("---")

st.subheader("Create Defect")

with st.form("defect_form"):

    c1, c2 = st.columns(2)

    with c1:

        defect_id = st.text_input(
            "Defect ID"
        )

        tool_name = st.text_input(
            "Tool Name"
        )

        defect_type = st.selectbox(

            "Defect Type",

            [
                "Functional",
                "Technical",
                "Integration",
                "Data",
                "Workflow",
                "Security"
            ]
        )

        defect_priority = st.selectbox(

            "Priority",

            [
                "Critical",
                "High",
                "Medium",
                "Low"
            ]
        )

        module_name = st.text_input(
            "Module Name"
        )

        issue_description = st.text_area(
            "Issue Description"
        )

    with c2:

        impacted_data = st.text_input(
            "Impacted URNs/Data"
        )

        reported_by = st.text_input(
            "Reported By"
        )

        issue_status = st.selectbox(

            "Issue Status",

            [
                "Open",
                "In Progress",
                "Resolved",
                "Closed"
            ]
        )

        resolution_owner = st.text_input(
            "Resolution Owner"
        )

        resolution_team = st.text_input(
            "Resolution Team"
        )

        expected_closure_date = (
            st.date_input(
                "Expected Closure Date",
                date.today()
            )
        )

    submitted = st.form_submit_button(
        "Create Defect"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO defects (

                defect_id,
                tool_name,
                defect_type,
                defect_priority,
                module_name,
                issue_description,
                impacted_data,
                reported_by,
                reported_date,
                issue_status,
                resolution_owner,
                resolution_team,
                expected_closure_date

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                defect_id,
                tool_name,
                defect_type,
                defect_priority,
                module_name,
                issue_description,
                impacted_data,
                reported_by,
                str(date.today()),
                issue_status,
                resolution_owner,
                resolution_team,
                str(expected_closure_date)

            )
        )

        st.success(
            "Defect created successfully"
        )

# =====================================================
# DEFECT REGISTER
# =====================================================

st.subheader("Defect Register")

df = fetch_data(
    "SELECT * FROM defects"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("Defect KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Defects",
        len(df)
    )

with k2:

    critical = len(

        df[
            df["defect_priority"] == "Critical"
        ]

    ) if not df.empty else 0

    st.metric(
        "Critical",
        critical
    )

with k3:

    open_defects = len(

        df[
            df["issue_status"] == "Open"
        ]

    ) if not df.empty else 0

    st.metric(
        "Open",
        open_defects
    )

with k4:

    closed = len(

        df[
            df["issue_status"] == "Closed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Closed",
        closed
    )