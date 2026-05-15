import streamlit as st

from services.rbac import ROLE_PERMISSIONS


# =====================================================
# SIDEBAR
# =====================================================

def render_sidebar(role):

    st.sidebar.title(
        "TransforaIQ Enterprise"
    )

    st.sidebar.markdown(
        "AI-Native ERP Governance Platform"
    )

    # =================================================
    # ROLE ACCESS
    # =================================================

    allowed_pages = ROLE_PERMISSIONS.get(
        role,
        []
    )

    selected_page = None

    # =================================================
    # GOVERNANCE
    # =================================================

    with st.sidebar.expander(
        "Governance Command Center",
        expanded=False
    ):

        governance_pages = [

            "Executive Dashboard",
            "Project Plan",
            "RAID Management",
            "Stakeholder Governance",
            "Cost Management",
            "Resource Management",
            "Client Master"

        ]

        for page in governance_pages:

            if page in allowed_pages:

                if st.button(
                    page,
                    key=page
                ):

                    selected_page = page

    # =================================================
    # AI & AGENTIC
    # =================================================

    with st.sidebar.expander(
        "AI & Agentic Intelligence",
        expanded=False
    ):

        ai_pages = [

            "AI ERP Delivery Accelerator",
            "AS-IS Transformation Summary",
            "TO-BE Process Summary",
            "FDD Workspace",
            "TDD Workspace",
            "Configuration Workspace",
            "Integration Workspace"

        ]

        for page in ai_pages:

            if page in allowed_pages:

                if st.button(
                    page,
                    key=page
                ):

                    selected_page = page

    # =================================================
    # BUILD & RELEASE
    # =================================================

    with st.sidebar.expander(
        "Build & Release Intelligence",
        expanded=False
    ):

        st.caption(
            "Coming Soon"
        )

    # =================================================
    # QUALITY ENGINEERING
    # =================================================

    with st.sidebar.expander(
        "Quality Engineering Intelligence",
        expanded=False
    ):

        testing_pages = [

            "SIT Planning & Execution",
            "UAT Governance",
            "Defect Tracking"

        ]

        for page in testing_pages:

            if page in allowed_pages:

                if st.button(
                    page,
                    key=page
                ):

                    selected_page = page

    # =================================================
    # LEARNING
    # =================================================

    with st.sidebar.expander(
        "Learning & Adoption Intelligence",
        expanded=False
    ):

        st.caption(
            "Coming Soon"
        )

    # =================================================
    # PRODUCTION
    # =================================================

    with st.sidebar.expander(
        "Production Readiness Intelligence",
        expanded=False
    ):

        st.caption(
            "Coming Soon"
        )

    # =================================================
    # HYPERCARE
    # =================================================

    with st.sidebar.expander(
        "Hypercare & Support Intelligence",
        expanded=False
    ):

        st.caption(
            "Coming Soon"
        )

    # =================================================
    # DEFAULT PAGE
    # =================================================

    if selected_page is None:

        selected_page = st.session_state.get(
            "selected_page",
            "Executive Dashboard"
        )

    st.session_state.selected_page = (
        selected_page
    )

    return selected_page