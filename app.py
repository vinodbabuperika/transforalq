import streamlit as st

from initialize_db import initialize_database

from authentication.login import login_page

from navigation.sidebar import render_sidebar

initialize_database()

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

# =====================================================
# LOGIN CONTROL
# =====================================================

if not st.session_state.logged_in:

    login_page()

    st.stop()

# =====================================================
# DATABASE INITIALIZATION
# =====================================================

initialize_database()

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="TransforaIQ Enterprise",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "role" not in st.session_state:
    st.session_state.role = "Admin"

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Executive Dashboard"

# =====================================================
# SIDEBAR
# =====================================================
selected_page = render_sidebar(

    st.session_state.role

)

# =====================================================
# PAGE ROUTING
# =====================================================

if selected_page == "Executive Dashboard":

    exec(
        open(
            "modules/executive_dashboard.py"
        ).read()
    )

elif selected_page == "Project Plan":

    exec(
        open(
            "modules/project_plan.py"
        ).read()
    )

elif selected_page == "RAID Management":

    exec(
        open(
            "modules/raid_management.py"
        ).read()
    )

elif selected_page == "Stakeholder Governance":

    exec(
        open(
            "modules/stakeholder_governance.py"
        ).read()
    )

elif selected_page == "Cost Management":

    st.title("Cost Management")

    exec(
        open(
            "modules/cost_management.py"
        ).read()
    )

elif selected_page == "Resource Management":

    st.title("Resource Management")

    exec(
        open(
            "modules/resource_management.py"
        ).read()
    )

elif selected_page == "Client Master":

    exec(
        open(
            "modules/client_master.py"
        ).read()
    )

elif selected_page == "SIT Planning & Execution":

    exec(
        open(
            "modules/sit_planning.py"
        ).read()
    )

elif selected_page == "UAT Governance":

    exec(
        open(
            "modules/uat_governance.py"
        ).read()
    )

elif selected_page == "Defect Tracking":

    exec(
        open(
            "modules/defect_tracking.py"
        ).read()
    )
elif selected_page == "AI ERP Delivery Accelerator":

    exec(
        open(
            "modules/ai_delivery_accelerator.py"
        ).read()
    )
        
if selected_page:
    st.session_state.selected_page = selected_page

# =====================================================
# PAGE ROUTING
# =====================================================

page = st.session_state.selected_page

# -----------------------------------------------------
# GOVERNANCE
# -----------------------------------------------------

if page == "Executive Dashboard":

    exec(
        open(
            "modules/executive_dashboard.py"
        ).read()
    )

elif page == "Project Plan":

    exec(
        open(
            "modules/project_plan.py"
        ).read()
    )

elif page == "RAID Management":
    exec(
        open(
            "modules/raid_management.py"
        ).read()
    )
elif selected_page == "AI Delivery Accelerator":

    exec(
        open(
            "modules/ai_delivery_accelerator.py"
        ).read()
    )
elif selected_page == "FDD Workspace":

    exec(
        open(
            "modules/fdd_workspace.py"
        ).read()
    )
elif selected_page == "AS-IS Transformation Summary":

    exec(
        open(
            "modules/asis_transformation.py"
        ).read()
    )

elif selected_page == "TO-BE Process Summary":

    exec(
        open(
            "modules/tobe_process.py"
        ).read()
    )

elif selected_page == "FDD Workspace":

    exec(
        open(
            "modules/fdd_workspace.py"
        ).read()
    )

elif selected_page == "TDD Workspace":

    exec(
        open(
            "modules/tdd_workspace.py"
        ).read()
    )

elif selected_page == "Configuration Workspace":

    exec(
        open(
            "modules/config_workspace.py"
        ).read()
    )

elif selected_page == "Integration Workspace":

    exec(
        open(
            "modules/integration_workspace.py"
        ).read()
    )
