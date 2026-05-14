import streamlit as st
import pandas as pd

from services.db_service import (
    fetch_data,
    execute_query
)

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("Client Master")

st.markdown(
    "Enterprise Multi-Tenant Client Governance"
)

# ---------------------------------------------------
# CLIENT DETAILS
# ---------------------------------------------------

st.subheader("Create Client")

c1, c2 = st.columns(2)

with c1:

    client_name = st.text_input(
        "Client Name"
    )

    erp_system = st.selectbox(
        "ERP System",
        [
            "SAP S/4HANA",
            "SAP ECC",
            "Oracle Fusion",
            "NetSuite",
            "Dynamics 365"
        ]
    )

    workflow = st.selectbox(
        "Workflow",
        [
            "PTP",
            "OTC",
            "RTR"
        ]
    )

    project_manager = st.text_input(
        "Project Manager"
    )

with c2:

    si_partner = st.selectbox(
        "SI Partner",
        [
            "Genpact",
            "Accenture",
            "IBM",
            "Infosys",
            "TCS"
        ]
    )

    deployment_type = st.selectbox(
        "Deployment Type",
        [
            "Multi-Tenant",
            "Dedicated"
        ]
    )

    status = st.selectbox(
        "Program Status",
        [
            "Green",
            "Amber",
            "Red"
        ]
    )

    go_live_readiness = st.slider(
        "Go-Live Readiness %",
        0,
        100,
        75
    )

# ---------------------------------------------------
# SCOPE MANAGEMENT
# ---------------------------------------------------

st.subheader("In-Scope Capabilities")

ocr_scope = st.checkbox("OCR")

exception_scope = st.checkbox(
    "Exception Concierge"
)

approval_scope = st.checkbox(
    "Approval Process"
)

threeway_scope = st.checkbox(
    "PO Three-Way Match"
)

twoway_scope = st.checkbox(
    "PO Two-Way Match"
)

# ---------------------------------------------------
# SAVE CLIENT
# ---------------------------------------------------

if st.button(
    "Save Client",
    key="save_client"
):

    execute_query(
        """
        INSERT INTO client_master (

            client_name,
            erp_system,
            workflow,
            project_manager,
            si_partner,
            deployment_type,
            status,
            go_live_readiness,
            ocr_scope,
            exception_concierge_scope,
            approval_process_scope,
            po_threeway_match_scope,
            po_twoway_match_scope

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            client_name,
            erp_system,
            workflow,
            project_manager,
            si_partner,
            deployment_type,
            status,
            go_live_readiness,
            str(ocr_scope),
            str(exception_scope),
            str(approval_scope),
            str(threeway_scope),
            str(twoway_scope)
        )
    )

    st.success(
        "Client created successfully"
    )

# ---------------------------------------------------
# CLIENT REGISTER
# ---------------------------------------------------

st.subheader("Client Portfolio")

df = fetch_data(
    "SELECT * FROM client_master"
)

st.dataframe(
    df,
    use_container_width=True
)