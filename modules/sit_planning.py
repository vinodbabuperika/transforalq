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

st.title("SIT Governance")

st.markdown(
    "Enterprise System Integration "
    "Testing Governance"
)

# =====================================================
# UPLOAD SIT SCRIPTS
# =====================================================

st.subheader("Upload SIT Scripts")

uploaded_file = st.file_uploader(
    "Upload SIT Script Excel",
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
            "SIT scripts uploaded successfully"
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
# MANUAL SIT SCRIPT ENTRY
# =====================================================

st.markdown("---")

st.subheader("Create SIT Test Scenario")

with st.form("sit_form"):

    c1, c2 = st.columns(2)

    with c1:

        scenario_id = st.text_input(
            "Scenario ID"
        )

        scenario_type = st.text_input(
            "Scenario Type"
        )

        execution_day = st.text_input(
            "Execution Day"
        )

        master_data = st.text_input(
            "Master Data"
        )

        entity_details = st.text_input(
            "Entity Details"
        )

        test_scenario = st.text_area(
            "Test Scenario"
        )

        test_steps = st.text_area(
            "Test Steps"
        )

    with c2:

        expected_outcome = st.text_area(
            "Expected Outcome"
        )

        testing_status = st.selectbox(

            "Testing Status",

            [
                "Not Started",
                "Passed",
                "Failed",
                "Blocked"
            ]
        )

        tester_name = st.text_input(
            "Tester Name"
        )

        test_data = st.text_input(
            "Test Data"
        )

        defect_id = st.text_input(
            "Defect ID"
        )

        action_owner = st.text_input(
            "Action Owner"
        )

    submitted = st.form_submit_button(
        "Create SIT Scenario"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO sit_scripts (

                scenario_id,
                scenario_type,
                execution_day,
                master_data,
                entity_details,
                test_scenario,
                test_steps,
                expected_outcome,
                testing_status,
                tester_name,
                executed_date,
                test_data,
                defect_id,
                action_owner

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                scenario_id,
                scenario_type,
                execution_day,
                master_data,
                entity_details,
                test_scenario,
                test_steps,
                expected_outcome,
                testing_status,
                tester_name,
                str(date.today()),
                test_data,
                defect_id,
                action_owner

            )
        )

        st.success(
            "SIT scenario created successfully"
        )

# =====================================================
# SIT REGISTER
# =====================================================

st.subheader("SIT Scenario Register")

df = fetch_data(
    "SELECT * FROM sit_scripts"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("SIT KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Scenarios",
        len(df)
    )

with k2:

    passed = len(

        df[
            df["testing_status"] == "Passed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Passed",
        passed
    )

with k3:

    failed = len(

        df[
            df["testing_status"] == "Failed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Failed",
        failed
    )

with k4:

    blocked = len(

        df[
            df["testing_status"] == "Blocked"
        ]

    ) if not df.empty else 0

    st.metric(
        "Blocked",
        blocked
    )