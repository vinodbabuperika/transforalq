import streamlit as st
import pandas as pd

from database.db import (
    execute_query,
    fetch_data
)

# =========================================
# PAGE TITLE
# =========================================

st.title("Stakeholder Governance")

st.markdown(
    "Enterprise stakeholder governance "
    "and transformation ownership"
)

# =========================================
# ADD STAKEHOLDER
# =========================================

st.subheader("Add Stakeholder")

with st.form("stakeholder_form"):

    stakeholder_name = st.text_input(
        "Stakeholder Name"
    )

    role = st.selectbox(

        "Role",

        [
            "Program Sponsor",
            "Steering Committee",
            "PMO Lead",
            "Business Lead",
            "ERP Architect",
            "Testing Lead",
            "SI Partner",
            "Operations Lead"
        ]
    )

    email = st.text_input(
        "Email"
    )

    client_name = st.text_input(
        "Client Name"
    )

    workstream = st.selectbox(

        "Workstream",

        [
            "Finance",
            "Procurement",
            "Supply Chain",
            "HR",
            "Manufacturing",
            "Testing",
            "Deployment",
            "Governance"
        ]
    )

    submitted = st.form_submit_button(
        "Add Stakeholder"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO stakeholders (

                stakeholder_name,
                role,
                email,
                client_name,
                workstream

            )

            VALUES (?, ?, ?, ?, ?)

            """,

            (
                stakeholder_name,
                role,
                email,
                client_name,
                workstream
            )
        )

        st.success(
            "Stakeholder added successfully"
        )

# =========================================
# STAKEHOLDER LIST
# =========================================

st.subheader("Stakeholder Registry")

df = fetch_data(
    "SELECT * FROM stakeholders"
)

st.dataframe(
    df,
    use_container_width=True
)