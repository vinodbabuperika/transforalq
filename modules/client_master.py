import streamlit as st
import pandas as pd

from database.db import (
    execute_query,
    fetch_data
)

# =========================================
# PAGE TITLE
# =========================================

st.title("Client Master")

st.markdown(
    "Enterprise client registry and "
    "ERP transformation portfolio"
)

# =========================================
# ADD CLIENT
# =========================================

st.subheader("Add New Client")

with st.form("client_form"):

    client_name = st.text_input(
        "Client Name"
    )

    industry = st.selectbox(

        "Industry",

        [
            "Banking",
            "Manufacturing",
            "Retail",
            "Healthcare",
            "Telecom",
            "Energy"
        ]
    )

    region = st.selectbox(

        "Region",

        [
            "North America",
            "Europe",
            "India",
            "Middle East",
            "APAC"
        ]
    )

    erp_platform = st.selectbox(

        "ERP Platform",

        [
            "SAP S/4HANA",
            "Oracle Fusion",
            "MS Dynamics",
            "Workday",
            "PeopleSoft"
        ]
    )

    status = st.selectbox(

        "Status",

        [
            "Active",
            "On Hold",
            "Completed"
        ]
    )

    submitted = st.form_submit_button(
        "Add Client"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO clients (

                client_name,
                industry,
                region,
                erp_platform,
                status

            )

            VALUES (?, ?, ?, ?, ?)

            """,

            (
                client_name,
                industry,
                region,
                erp_platform,
                status
            )
        )

        st.success(
            "Client added successfully"
        )

# =========================================
# CLIENT LIST
# =========================================

st.subheader("Client Portfolio")

df = fetch_data(
    "SELECT * FROM clients"
)

st.dataframe(
    df,
    use_container_width=True
)