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

st.title("Deployment Governance")

st.markdown(
    "Enterprise Deployment & "
    "Cutover Command Center"
)

# =====================================================
# FILE UPLOAD
# =====================================================

st.subheader("Upload Deployment Plan")

uploaded_file = st.file_uploader(
    "Upload Deployment Excel",
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
            "Deployment plan uploaded successfully"
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
# MANUAL DEPLOYMENT ENTRY
# =====================================================

st.markdown("---")

st.subheader("Create Deployment Activity")

with st.form("deployment_form"):

    c1, c2 = st.columns(2)

    with c1:

        deployment_id = st.text_input(
            "Deployment ID"
        )

        wave_name = st.text_input(
            "Wave Name"
        )

        deployment_task = st.text_area(
            "Deployment Task"
        )

        environment_name = st.text_input(
            "Environment"
        )

        deployment_owner = st.text_input(
            "Deployment Owner"
        )

        dependency = st.text_input(
            "Dependency"
        )

    with c2:

        deployment_status = st.selectbox(

            "Deployment Status",

            [
                "Not Started",
                "In Progress",
                "Completed",
                "Blocked"
            ]
        )

        planned_start = st.date_input(
            "Planned Start",
            date.today()
        )

        planned_end = st.date_input(
            "Planned End",
            date.today()
        )

        rollback_plan = st.text_area(
            "Rollback Plan"
        )

        remarks = st.text_area(
            "Remarks"
        )

    submitted = st.form_submit_button(
        "Create Deployment Task"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO deployment_tracker (

                deployment_id,
                wave_name,
                deployment_task,
                environment_name,
                deployment_owner,
                planned_start,
                planned_end,
                deployment_status,
                dependency,
                rollback_plan,
                remarks

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                deployment_id,
                wave_name,
                deployment_task,
                environment_name,
                deployment_owner,
                str(planned_start),
                str(planned_end),
                deployment_status,
                dependency,
                rollback_plan,
                remarks

            )
        )

        st.success(
            "Deployment activity created"
        )

# =====================================================
# DEPLOYMENT REGISTER
# =====================================================

st.subheader("Deployment Register")

df = fetch_data(
    "SELECT * FROM deployment_tracker"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("Deployment KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Activities",
        len(df)
    )

with k2:

    completed = len(

        df[
            df["deployment_status"]
            == "Completed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Completed",
        completed
    )

with k3:

    inprogress = len(

        df[
            df["deployment_status"]
            == "In Progress"
        ]

    ) if not df.empty else 0

    st.metric(
        "In Progress",
        inprogress
    )

with k4:

    blocked = len(

        df[
            df["deployment_status"]
            == "Blocked"
        ]

    ) if not df.empty else 0

    st.metric(
        "Blocked",
        blocked
    )

# =====================================================
# AI CUTOVER INSIGHTS
# =====================================================

st.subheader("AI Deployment Insights")

if blocked > 5:

    st.error(
        "Deployment execution risk detected"
    )

elif blocked > 2:

    st.warning(
        "Deployment blockers increasing"
    )

else:

    st.success(
        "Deployment governance healthy"
    )

st.success(
    "Cutover governance operational"
)