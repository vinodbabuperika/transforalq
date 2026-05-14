import streamlit as st
import pandas as pd
selected_client = st.session_state[
    "selected_client"
]
from io import BytesIO
from datetime import date
from services.db_service import fetch_data, execute_query

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("RAID Management")

st.markdown("Enterprise Risk, Action, Issue & Dependency Tracking")

# ---------------------------------------------------
# RAID ENTRY FORM
# ---------------------------------------------------

st.subheader("Create RAID Entry")

col1, col2 = st.columns(2)

with col1:

    title = st.text_input("Title")

    raid_date = st.date_input(
        "RAID Date",
        date.today()
    )

    raised_by = st.text_input("Raised By")

    raid_type = st.selectbox(
        "RAID Type",
        ["Risk", "Action", "Issue", "Dependency"]
    )

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

with col2:

    status = st.selectbox(
        "Status",
        ["Open", "In Progress", "Closed"]
    )

    owner = st.text_input("Owner")

    due_date = st.date_input(
        "Due Date",
        date.today()
    )

description = st.text_area("Description")

mitigation_plan = st.text_area("Mitigation Plan")

# ---------------------------------------------------
# SAVE BUTTON
# ---------------------------------------------------

if st.button("Save RAID Entry"):

    # Mandatory mitigation for Risk items

    if raid_type == "Risk" and mitigation_plan.strip() == "":

        st.error(
            "Mitigation Plan is mandatory for Risk items"
        )

    else:

        execute_query(
            """
            INSERT INTO raid_log (

                client_name,
                title,
                raid_date,
                raised_by,
                raid_type,
                priority,
                status,
                owner,
                due_date,
                mitigation_plan,
                description
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                
                selected_client,
                title,
                str(raid_date),
                raised_by,
                raid_type,
                priority,
                status,
                owner,
                str(due_date),
                mitigation_plan,
                description
            )
        )

        st.success("RAID Entry Saved Successfully")

# ---------------------------------------------------
# RAID TABLE
# ---------------------------------------------------

st.subheader("RAID Register")

df = fetch_data(
    f"""
SELECT * FROM raid_log
WHERE client_name = '{selected_client}'
"""
)

st.dataframe(
    df,
    use_container_width=True
)
# ---------------------------------------------------
# EXPORT TO EXCEL
# ---------------------------------------------------

st.subheader("Export RAID Report")

output = BytesIO()

with pd.ExcelWriter(
    output,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False,
        sheet_name="RAID Report"
    )

excel_data = output.getvalue()

st.download_button(
    label="Download RAID Report",
    data=excel_data,
    file_name="raid_report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
# ---------------------------------------------------
# FILE UPLOAD SECTION
# ---------------------------------------------------

st.subheader("Upload Evidence")

uploaded_file = st.file_uploader(
    "Upload File",
    type=["xlsx", "csv", "pdf", "docx"]
)

if uploaded_file:

    st.success("File uploaded successfully")