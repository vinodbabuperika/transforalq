import streamlit as st
import pandas as pd

from services.ai_service import (
    generate_document
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("AI ERP Delivery Accelerator")

st.markdown(
    "AI-Assisted ERP Transformation "
    "Discovery & Document Engineering"
)

# =====================================================
# PROJECT DETAILS
# =====================================================

st.subheader("Project Metadata")

c1, c2 = st.columns(2)

with c1:

    client_name = st.text_input(
        "Client Name"
    )

    project_name = st.text_input(
        "Project Name"
    )

    erp_system = st.selectbox(

        "ERP System",

        [
            "SAP ECC",
            "SAP S/4HANA",
            "Oracle",
            "Dynamics"
        ]
    )

with c2:

    country = st.text_input(
        "Country"
    )

    invoice_volume = st.number_input(
        "Monthly Invoice Volume",
        value=1000
    )

    automation_target = st.slider(
        "Target Automation %",
        0,
        100,
        85
    )

# =====================================================
# FILE UPLOADS
# =====================================================

st.subheader("Upload Enterprise Assets")

questionnaire = st.file_uploader(
    "Upload Discovery Questionnaire",
    type=["xlsx", "csv"]
)

sap_data = st.file_uploader(
    "Upload Historic SAP Data",
    type=["xlsx", "csv"]
)

fdd_sample = st.file_uploader(
    "Upload FDD Sample",
    type=["docx", "pdf", "txt"]
)

tdd_sample = st.file_uploader(
    "Upload TDD Sample",
    type=["docx", "pdf", "txt"]
)

config_sample = st.file_uploader(
    "Upload Configuration Workbook",
    type=["xlsx"]
)

# =====================================================
# GENERATE BUTTON
# =====================================================

st.markdown("---")

if st.button("Generate AI ERP Deliverables"):

    st.success(
        "AI Transformation Analysis Started"
    )

    # =================================================
    # QUESTIONNAIRE ANALYSIS
    # =================================================

    detected_company_codes = []

    detected_countries = []

    detected_invoice_sources = []

    detected_document_types = []

    if questionnaire is not None:

        try:

            if questionnaire.name.endswith(".csv"):

                q_df = pd.read_csv(
                    questionnaire
                )

            else:

                q_df = pd.read_excel(
                    questionnaire
                )

            st.success(
                "Questionnaire analyzed"
            )

            columns = [
                str(col).lower()
                for col in q_df.columns
            ]

            # Company Codes

            if "company code" in columns:

                detected_company_codes = (

                    q_df[
                        q_df.columns[
                            columns.index(
                                "company code"
                            )
                        ]
                    ]

                    .dropna()

                    .astype(str)

                    .unique()

                    .tolist()

                )

            # Countries

            if "country" in columns:

                detected_countries = (

                    q_df[
                        q_df.columns[
                            columns.index(
                                "country"
                            )
                        ]
                    ]

                    .dropna()

                    .astype(str)

                    .unique()

                    .tolist()

                )

            # Invoice Sources

            if "invoice source" in columns:

                detected_invoice_sources = (

                    q_df[
                        q_df.columns[
                            columns.index(
                                "invoice source"
                            )
                        ]
                    ]

                    .dropna()

                    .astype(str)

                    .unique()

                    .tolist()

                )

            # Document Types

            if "document type" in columns:

                detected_document_types = (

                    q_df[
                        q_df.columns[
                            columns.index(
                                "document type"
                            )
                        ]
                    ]

                    .dropna()

                    .astype(str)

                    .unique()

                    .tolist()

                )

        except Exception as e:

            st.error(
                f"Questionnaire analysis failed: {e}"
            )

    # =================================================
    # AS-IS SUMMARY
    # =================================================

    asis_summary = f'''

Client: {client_name}

ERP Landscape: {erp_system}

Current Invoice Volume:
{invoice_volume}

Current-State Observations:

- Manual invoice processing dependency
- Multiple validation touchpoints
- ERP integration dependencies
- Workflow escalations
- Limited automation

Transformation Opportunities:

- Intelligent invoice ingestion
- Touchless invoice processing
- Workflow automation
- AI-assisted exception handling
- ERP optimization

'''

    st.session_state.asis_summary = (
        asis_summary
    )

    # =================================================
    # AS-IS PROCESS SUMMARY
    # =================================================

    asis_process_summary = f'''

AS-IS PROCESS SUMMARY

Current ERP Landscape:
{erp_system}

Current State Activities:

- Manual invoice ingestion
- Email approvals
- ERP validation dependencies
- Exception handling
- Workflow escalations

'''

    st.session_state.asis_process_summary = (
        asis_process_summary
    )

    # =================================================
    # TO-BE SUMMARY
    # =================================================

    tobe_summary = f'''

TO-BE PROCESS SUMMARY

Target Automation:
{automation_target}%

Future State:

- Touchless invoice processing
- AI validations
- Automated workflows
- Faster approvals
- Better governance

'''

    st.session_state.tobe_summary = (
        tobe_summary
    )
    # =================================================
    # AI DOCUMENT PROMPTS
    # =================================================

    fdd_prompt = f"""

Create a Functional Design Document.

Client:
{client_name}

Project:
{project_name}

ERP:
{erp_system}

Company Codes:
{detected_company_codes}

Countries:
{detected_countries}

Invoice Sources:
{detected_invoice_sources}

Document Types:
{detected_document_types}

"""

    tdd_prompt = f"""

Create a Technical Design Document.

ERP:
{erp_system}

Include:
- Interfaces
- APIs
- Integrations
- Validation Rules
- Error Handling

"""

    config_prompt = f"""

Create ERP Configuration Workbook.

ERP:
{erp_system}

Include:
- Workflow setup
- Company codes
- Validation rules
- Approval hierarchy
- Posting rules

"""

    # =================================================
    # GENERATE DOCUMENTS
    # =================================================

    fdd_output = generate_document(
        fdd_prompt
    )

    st.session_state.fdd_output = (
        fdd_output
    )

    tdd_output = generate_document(
        tdd_prompt
    )

    st.session_state.tdd_output = (
        tdd_output
    )

    config_output = generate_document(
        config_prompt
    )

    st.session_state.config_output = (
        config_output
    )

    # =================================================
    # FINAL STATUS
    # =================================================

    st.success(
        "AI ERP Deliverables Generated Successfully"
    )