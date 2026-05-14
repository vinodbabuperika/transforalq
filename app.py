import streamlit as st
from core.metadata_engine import *
from core.rbac import has_access
from core.navigation import NAVIGATION_STRUCTURE
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
    # CLIENT SELECTOR
    # ---------------------------------------------------

    selected_client = st.selectbox(
        "Select Client",
        CLIENTS
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

    # ---------------------------------------------------
    # DEFAULT PAGE
    # ---------------------------------------------------

    if "selected_page" not in st.session_state:

        st.session_state["selected_page"] = (
            "Executive Dashboard"
        )

    # ---------------------------------------------------
    # DYNAMIC NAVIGATION ENGINE
    # ---------------------------------------------------

    for domain, pages in NAVIGATION_STRUCTURE.items():

        with st.expander(domain):

            for page in pages:

                if has_access(role, page):

                    if st.button(
                        page,
                        key=f"nav_{page}"
                    ):

                        st.session_state[
                            "selected_page"
                        ] = page

# ---------------------------------------------------
# ACTIVE PAGE
# ---------------------------------------------------

selected_page = st.session_state[
    "selected_page"
]

# ---------------------------------------------------
# RBAC SECURITY
# ---------------------------------------------------

allowed_pages = ROLE_PERMISSIONS.get(role, [])

if (
    selected_page is not None and
    selected_page not in allowed_pages
):

    #st.error(
        #"Access Denied: Insufficient permissions"
    

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

    tab1, tab2 = st.tabs(
        [
            "Resource Management",
            "Cost Management"
        ]
    )

    with tab1:

        exec(
            open(
                "modules/resource_management.py"
            ).read()
        )

    with tab2:

        exec(
            open(
                "modules/cost_management.py"
            ).read()
        )

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

elif selected_page == "ERP Discovery":
    exec(open("modules/erp_discovery.py").read())

elif selected_page == "Gap Analysis":
    exec(open("modules/gap_analysis.py").read())

elif selected_page == "AI Recommendations":
    exec(open("modules/ai_recommendations.py").read())

elif selected_page == "FDD Generator":
    exec(open("modules/fdd_generator.py").read())

elif selected_page == "Client Master":

    exec(
        open(
            "modules/client_master.py"
        ).read()
    )
elif selected_page == "Stakeholder Governance":

    exec(
        open(
            "modules/stakeholder_governance.py"
        ).read()
    )

elif selected_page == "Project Plan":

    exec(
        open(
            "modules/project_plan_engine.py"
        ).read()
    )        
elif selected_page == "RAID Management":

    exec(
        open(
            "modules/raid_management.py"
        ).read()
    )
elif selected_page == "SIT Planning & Execution":

    exec(
        open(
            "modules/sit_governance.py"
        ).read()
    )
elif selected_page == "UAT Governance":

    exec(
        open(
            "modules/uat_governance.py"
        ).read()
    )
elif selected_page == "Cost & Resource Tracking":

    exec(
        open(
            "modules/resource_management.py"
        ).read()
    )
elif selected_page == "Executive Dashboard":

    exec(
        open(
            "modules/executive_dashboard.py"
        ).read()
    )
elif selected_page == "AI Risk Prediction":

    exec(
        open(
            "modules/ai_risk_prediction.py"
        ).read()
    )
elif selected_page == "AI PMO Copilot":

    exec(
        open(
            "modules/ai_pmo_copilot.py"
        ).read()
    )
elif selected_page == "Deployment Tracker":

    exec(
        open(
            "modules/deployment_governance.py"
        ).read()
    )
elif selected_page == "Cutover & Hypercare":

    exec(
        open(
            "modules/hypercare_governance.py"
        ).read()
    )
elif selected_page == "Cutover & Hypercare":

    tab1, tab2 = st.tabs(
        [
            "Hypercare Governance",
            "Go-Live Command Center"
        ]
    )

    with tab1:

        exec(
            open(
                "modules/hypercare_governance.py"
            ).read()
        )

    with tab2:

        exec(
            open(
                "modules/go_live_command_center.py"
            ).read()
        )                                