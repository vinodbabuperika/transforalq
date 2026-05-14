import streamlit as st
import pandas as pd
selected_client = st.session_state[
    "selected_client"
]
from datetime import date

from services.db_service import (
    fetch_data,
    execute_query
)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("Project Plan")

st.markdown(
    "Enterprise ERP Transformation Plan & Milestone Tracking"
)

# ---------------------------------------------------
# CREATE TASK
# ---------------------------------------------------

st.subheader("Create Project Task")

c1, c2 = st.columns(2)

with c1:

    phase = st.selectbox(
        "Project Phase",
        [
            "Design",
            "Build",
            "SIT",
            "UAT",
            "Deployment",
            "Hypercare"
        ]
    )

    task = st.text_input("Task Name")

    owner = st.text_input("Task Owner")

with c2:

    status = st.selectbox(
        "Status",
        [
            "Not Started",
            "In Progress",
            "Completed",
            "Delayed"
        ]
    )

    due_date = st.date_input(
        "Due Date",
        date.today()
    )

# ---------------------------------------------------
# SAVE BUTTON
# ---------------------------------------------------

if st.button(
    "Save Project Task",
    key="save_project_task"
):

    execute_query(
        """
        INSERT INTO project_plan (

            client_name,

            phase,

            task,

            owner,

            status,

            due_date

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            selected_client,
            phase,
            task,
            owner,
            status,
            str(due_date)
        )
    )

    st.success(
        "Project task saved successfully"
    )
# ---------------------------------------------------
# PROJECT PLAN TABLE
# ---------------------------------------------------

st.subheader("Project Plan Register")

df = fetch_data(
    f"""
    SELECT * FROM project_plan
    WHERE client_name = '{selected_client}'
    """
)
st.dataframe(
    df,
    use_container_width=True
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Project KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Total Tasks",
        len(df)
    )

with k2:
    completed = len(
        df[df["status"] == "Completed"]
    ) if not df.empty else 0

    st.metric(
        "Completed",
        completed
    )

with k3:
    in_progress = len(
        df[df["status"] == "In Progress"]
    ) if not df.empty else 0

    st.metric(
        "In Progress",
        in_progress
    )

with k4:
    delayed = len(
        df[df["status"] == "Delayed"]
    ) if not df.empty else 0

    st.metric(
        "Delayed",
        delayed
    )