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

st.title("Enterprise Project Plan")

st.markdown(
    "ERP Transformation Delivery "
    "Planning & Governance"
)

# =====================================================
# EXCEL TEMPLATE FORMAT
# =====================================================

st.info(
    """
Upload Excel with columns:

Phase
Task Name
Deliverables
Status
% Completion
Start Date
End Date
Owner
Teams Involved
"""
)

# =====================================================
# FILE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "Upload Project Plan",
    type=["xlsx", "csv"]
)

# =====================================================
# PROCESS FILE
# =====================================================

if uploaded_file is not None:

    try:

        # ---------------------------------------------
        # READ FILE
        # ---------------------------------------------

        if uploaded_file.name.endswith(".csv"):

            upload_df = pd.read_csv(
                uploaded_file
            )

        else:

            upload_df = pd.read_excel(
                uploaded_file
            )

        st.success(
            "File uploaded successfully"
        )

        st.subheader(
            "Preview Uploaded Data"
        )

        st.dataframe(
            upload_df.head(),
            use_container_width=True
        )

        # ---------------------------------------------
        # LOAD TO DATABASE
        # ---------------------------------------------

        if st.button(
            "Load Project Plan to Database"
        ):

            for _, row in upload_df.iterrows():

                phase = str(
                    row.get("Phase", "")
                )

                task_name = str(
                    row.get("Task Name", "")
                )

                deliverable = str(
                    row.get("Deliverables", "")
                )

                status = str(
                    row.get("Status", "")
                )

                owner = str(
                    row.get("Owner", "")
                )

                start_date = str(
                    row.get("Start Date", "")
                )

                end_date = str(
                    row.get("End Date", "")
                )

                dependency = ""

                remarks = ""

                execute_query(

                    """

                    INSERT INTO project_plan (

                        client_name,
                        phase,
                        task_name,
                        deliverable,
                        owner,
                        status,
                        planned_start_date,
                        planned_end_date,
                        dependency,
                        remarks

                    )

                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

                    """,

                    (

                        "Enterprise Client",
                        phase,
                        task_name,
                        deliverable,
                        owner,
                        status,
                        start_date,
                        end_date,
                        dependency,
                        remarks

                    )
                )

            st.success(
                "Project plan loaded successfully"
            )

    except Exception as e:

        st.error(
            f"Error processing file: {e}"
        )

# =====================================================
# PROJECT PLAN TABLE
# =====================================================

st.subheader("Project Plan Register")

df = fetch_data(
    "SELECT * FROM project_plan"
)

st.dataframe(
    df,
    use_container_width=True
)
# =====================================================
# DELETE TASK
# =====================================================

st.markdown("---")

st.subheader("Delete Task")

if not df.empty:

    delete_id = st.selectbox(
        "Select Task ID to Delete",
        df["id"]
    )

    if st.button("Delete Task"):

        execute_query(

            f"""

            DELETE FROM project_plan
            WHERE id = {delete_id}

            """

        )

        st.success(
            "Task deleted successfully"
        )

        st.rerun()
# =====================================================
# KPI SECTION
# =====================================================

st.subheader("Project KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Tasks",
        len(df)
    )

with k2:

    completed = len(

        df[
            df["status"] == "Completed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Completed",
        completed
    )

with k3:

    in_progress = len(

        df[
            df["status"] == "In Progress"
        ]

    ) if not df.empty else 0

    st.metric(
        "In Progress",
        in_progress
    )

with k4:

    delayed = len(

        df[
            df["status"] == "Delayed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Delayed",
        delayed
    )

# =====================================================
# PHASE SUMMARY
# =====================================================

st.subheader("Phase Summary")

if not df.empty:

    phase_summary = (

        df.groupby("phase")
        .size()
        .reset_index(name="Task Count")

    )

    st.dataframe(
        phase_summary,
        use_container_width=True
    )

else:

    st.warning(
        "No project tasks available"
    )
    # =====================================================
# MANUAL TASK ENTRY
# =====================================================

st.markdown("---")

st.subheader("Add Manual Project Task")

with st.form("manual_project_task"):

    c1, c2 = st.columns(2)

    with c1:

        phase = st.text_input(
            "Phase"
        )

        task_name = st.text_input(
            "Task Name"
        )

        deliverable = st.text_input(
            "Deliverable"
        )

        owner = st.text_input(
            "Owner"
        )

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

        planned_start = st.date_input(
            "Planned Start Date"
        )

        planned_end = st.date_input(
            "Planned End Date"
        )

        remarks = st.text_area(
            "Remarks"
        )

    submitted = st.form_submit_button(
        "Add Task"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO project_plan (

                client_name,
                phase,
                task_name,
                deliverable,
                owner,
                status,
                planned_start_date,
                planned_end_date,
                dependency,
                remarks

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                "Enterprise Client",
                phase,
                task_name,
                deliverable,
                owner,
                status,
                str(planned_start),
                str(planned_end),
                "",
                remarks

            )
        )

        st.success(
            "Manual task added successfully"
        )