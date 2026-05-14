import streamlit as st
import pandas as pd

from datetime import date

from database.db import (
    execute_query,
    fetch_data
)

# =========================================
# PAGE TITLE
# =========================================

st.title("RAID Management")

st.markdown(
    "Enterprise Risk, Assumption, "
    "Issue & Dependency Governance"
)

# =========================================
# CREATE RAID ITEM
# =========================================

st.subheader("Create RAID Item")

with st.form("raid_form"):

    c1, c2 = st.columns(2)

    with c1:

        raid_type = st.selectbox(

            "RAID Type",

            [
                "Risk",
                "Assumption",
                "Issue",
                "Dependency"
            ]
        )

        title = st.text_input(
            "Title"
        )

        description = st.text_area(
            "Description"
        )

        owner = st.text_input(
            "Owner"
        )

    with c2:

        status = st.selectbox(

            "Status",

            [
                "Open",
                "In Progress",
                "Mitigated",
                "Closed"
            ]
        )

        priority = st.selectbox(

            "Priority",

            [
                "Critical",
                "High",
                "Medium",
                "Low"
            ]
        )

        due_date = st.date_input(
            "Due Date",
            date.today()
        )

        mitigation_plan = st.text_area(
            "Mitigation Plan"
        )

    submitted = st.form_submit_button(
        "Create RAID Item"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO raid_log (

                raid_type,
                title,
                description,
                owner,
                status,
                due_date

            )

            VALUES (?, ?, ?, ?, ?, ?)

            """,

            (

                raid_type,
                title,
                description,
                owner,
                status,
                str(due_date)

            )
        )

        st.success(
            "RAID item created successfully"
        )

# =========================================
# RAID TABLE
# =========================================

st.subheader("RAID Register")

df = fetch_data(
    "SELECT * FROM raid_log"
)

st.dataframe(
    df,
    use_container_width=True
)

# =========================================
# KPI DASHBOARD
# =========================================

st.subheader("RAID KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Items",
        len(df)
    )

with k2:

    open_items = len(

        df[
            df["status"] == "Open"
        ]

    ) if not df.empty else 0

    st.metric(
        "Open",
        open_items
    )

with k3:

    progress_items = len(

        df[
            df["status"] == "In Progress"
        ]

    ) if not df.empty else 0

    st.metric(
        "In Progress",
        progress_items
    )

with k4:

    closed_items = len(

        df[
            df["status"] == "Closed"
        ]

    ) if not df.empty else 0

    st.metric(
        "Closed",
        closed_items
    )

# =========================================
# RAID SUMMARY
# =========================================

st.subheader("RAID Type Summary")

summary = (

    df.groupby("raid_type")
    .size()
    .reset_index(name="Count")

    if not df.empty

    else pd.DataFrame()
)

st.dataframe(
    summary,
    use_container_width=True
)