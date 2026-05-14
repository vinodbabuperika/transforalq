import streamlit as st
from services.rbac import ROLE_PERMISSIONS
# ---------------------------------------------------
# LOGIN SYSTEM
# ---------------------------------------------------

if "logged_in" not in st.session_state:

    st.set_page_config(
        page_title="TransforaIQ Login",
        layout="centered"
    )

    st.title("TransforaIQ")

    st.markdown(
        "Enterprise ERP Transformation Operating System"
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "Admin",
            "PMO",
            "Testing Lead",
            "SI Partner",
            "Business User"
        ]
    )

    if st.button("Login"):

        if username and password:

            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role

            st.rerun()

        else:

            st.error(
                "Please enter username and password"
            )

    st.stop()
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="TransforaIQ",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ---------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------

with st.sidebar:

    st.title("TransforaIQ")

    # ---------------------------------------------------
    # GLOBAL CLIENT SELECTOR
    # ---------------------------------------------------

    client_list = [
        "Client A",
        "Client B",
        "Client C",
        "Client D",
        "Client E"
    ]

    selected_client = st.selectbox(
        "Select Client",
        client_list
    )

    st.session_state["selected_client"] = (
        selected_client
    )

    st.success(
        f"Logged in as: {st.session_state['role']}"
    )

    # ---------------------------------------------------
    # LOGOUT
    # ---------------------------------------------------

    if st.button(
        "Logout",
        key="logout_btn"
    ):

        st.session_state.clear()

        st.rerun()

    st.markdown("---")

    role = st.session_state["role"]

    selected_page = None

    # ---------------------------------------------------
    # GOVERNANCE DOMAIN
    # ---------------------------------------------------

    if role in ["Admin", "PMO"]:

        with st.expander(
            "Governance Domain",
            expanded=True
        ):

            if st.button("Executive Dashboard"):
                selected_page = "Executive Dashboard"

            if st.button("Project Plan"):
                selected_page = "Project Plan"

            if st.button("RAID Management"):
                selected_page = "RAID Management"

            if st.button("RACI Matrix"):
                selected_page = "RACI Matrix"

            if st.button("Stakeholder Governance"):
                selected_page = "Stakeholder Governance"

            if st.button("Cost & Resource Tracking"):
                selected_page = "Cost & Resource Tracking"

            if st.button("Client Master"):
                selected_page = "Client Master"

    # ---------------------------------------------------
    # DELIVERY DOMAIN
    # ---------------------------------------------------

    if role in ["Admin", "PMO", "SI Partner"]:

        with st.expander("Delivery Domain"):

            if st.button("Statement of Work"):
                selected_page = "Statement of Work"

            if st.button("Fit-Gap Analysis"):
                selected_page = "Fit-Gap Analysis"

            if st.button("Configuration Tracking"):
                selected_page = "Configuration Tracking"

            if st.button("Integration Tracking"):
                selected_page = "Integration Tracking"

    # ---------------------------------------------------
    # TESTING DOMAIN
    # ---------------------------------------------------

    if role in ["Admin", "Testing Lead", "PMO"]:

        with st.expander("Testing Domain"):

            if st.button("SIT Planning & Execution"):
                selected_page = "SIT Planning & Execution"

            if st.button("UAT Governance"):
                selected_page = "UAT Governance"

            if st.button("Defect Tracking"):
                selected_page = "Defect Tracking"

    # ---------------------------------------------------
    # DEPLOYMENT DOMAIN
    # ---------------------------------------------------

    if role in ["Admin", "PMO", "SI Partner"]:

        with st.expander("Deployment Domain"):

            if st.button("Deployment Tracker"):
                selected_page = "Deployment Tracker"

            if st.button("Cutover & Hypercare"):
                selected_page = "Cutover & Hypercare"

    # ---------------------------------------------------
    # MIGRATION DOMAIN
    # ---------------------------------------------------

    if role in ["Admin", "PMO", "SI Partner"]:

        with st.expander("Migration Domain"):

            if st.button("Migration Validation"):
                selected_page = "Migration Validation"

    # ---------------------------------------------------
    # AI DOMAIN
    # ---------------------------------------------------

    if role in ["Admin", "PMO"]:

        with st.expander(
            "AI & Agentic Intelligence"
        ):

            if st.button("AI PMO Copilot"):
                selected_page = "AI PMO Copilot"

            if st.button("AI Risk Prediction"):
                selected_page = "AI Risk Prediction"

            if st.button("AI Mapping Assistant"):
                selected_page = "AI Mapping Assistant"

            if st.button("Agentic Workflow Automation"):
                selected_page = "Agentic Workflow Automation"
# ---------------------------------------------------
# RBAC SECURITY
# ---------------------------------------------------

allowed_pages = ROLE_PERMISSIONS.get(role, [])

if (
    selected_page is not None and
    selected_page not in allowed_pages
):

    st.error(
        "Access Denied: Insufficient permissions"
    )

    st.stop()

if selected_page is None:

    selected_page = "Executive Dashboard"
# ---------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------

if selected_page == "Executive Dashboard":

    st.title("Executive Dashboard")

    st.success("Executive dashboard cloud deployment in progress")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Go-Live Readiness", "82%")

    with col2:
        st.metric("Open Risks", "12")

    with col3:
        st.metric("Open Defects", "5")

elif selected_page == "Project Plan":
    exec(open("modules/project_plan.py").read())

elif selected_page == "RAID Management":
    exec(open("modules/raid_management.py").read())

elif selected_page == "RACI Matrix":
    exec(open("modules/raci_matrix.py").read())

elif selected_page == "Stakeholder Governance":
    exec(open("modules/stakeholder_governance.py").read())

elif selected_page == "Cost & Resource Tracking":
    exec(open("modules/cost_resource_tracking.py").read())

elif selected_page == "Client Master":
    exec(open("modules/client_master.py").read())

elif selected_page == "Statement of Work":
    exec(open("modules/statement_of_work.py").read())

elif selected_page == "Fit-Gap Analysis":
    exec(open("modules/fit_gap_analysis.py").read())

elif selected_page == "Configuration Tracking":
    exec(open("modules/configuration_tracking.py").read())

elif selected_page == "Integration Tracking":
    exec(open("modules/integration_tracking.py").read())

elif selected_page == "SIT Planning & Execution":
    exec(open("modules/sit_planning.py").read())

elif selected_page == "UAT Governance":
    exec(open("modules/uat_governance.py").read())

elif selected_page == "Defect Tracking":
    exec(open("modules/defect_tracking.py").read())

elif selected_page == "Deployment Tracker":
    exec(open("modules/deployment_tracker.py").read())

elif selected_page == "Cutover & Hypercare":
    exec(open("modules/cutover_hypercare.py").read())

elif selected_page == "Migration Validation":
    exec(open("modules/migration_validation.py").read())

elif selected_page == "AI PMO Copilot":
    exec(open("modules/ai_pmo_copilot.py").read())

elif selected_page == "AI Risk Prediction":
    exec(open("modules/ai_risk_prediction.py").read())

elif selected_page == "AI Mapping Assistant":
    exec(open("modules/ai_mapping_assistant.py").read())

elif selected_page == "Agentic Workflow Automation":
    exec(open("modules/agentic_workflow_automation.py").read())
    