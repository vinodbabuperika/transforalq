import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ERP Discovery")

st.success("ERP Discovery Loaded Successfully")
# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("ERP Discovery Studio")

st.markdown(
    """
AI-powered ERP landscape discovery
and workflow transformation analysis
"""
)

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

st.subheader("Upload ERP Extract")

uploaded_file = st.file_uploader(
    "Upload ERP CSV or Excel File",
    type=["csv", "xlsx"]
)

# ---------------------------------------------------
# PROCESS FILE
# ---------------------------------------------------

if uploaded_file:

    # ---------------------------------------------------
    # READ FILE
    # ---------------------------------------------------

    if uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.read_excel(uploaded_file)

    # ---------------------------------------------------
    # SUCCESS MESSAGE
    # ---------------------------------------------------

    st.success(
        "ERP extract uploaded successfully"
    )

    # ---------------------------------------------------
    # DATA PREVIEW
    # ---------------------------------------------------

    st.subheader("ERP Data Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # ---------------------------------------------------
    # COLUMN ANALYSIS
    # ---------------------------------------------------

    st.subheader("AI ERP Discovery")

    columns = [
        col.lower()
        for col in df.columns
    ]

    # ---------------------------------------------------
    # AI ERP CLASSIFICATION ENGINE
    # ---------------------------------------------------

    st.subheader("AI ERP Intelligence Engine")

    detected_processes = []
    automation_opportunities = []
    workflow_findings = []

    column_text = " ".join(columns)

    # ---------------------------------------------------
    # PTP DETECTION
    # ---------------------------------------------------

    if (
        "invoice" in column_text or
        "vendor" in column_text or
        "po" in column_text
    ):

        detected_processes.append(
            "PTP (Procure-to-Pay)"
        )

        automation_opportunities.extend([
            "OCR Automation",
            "Invoice Workflow Automation",
            "PO Matching",
            "Exception Concierge"
        ])

    # ---------------------------------------------------
    # OTC DETECTION
    # ---------------------------------------------------

    if (
        "customer" in column_text or
        "cash" in column_text or
        "collection" in column_text
    ):

        detected_processes.append(
            "OTC (Order-to-Cash)"
        )

        automation_opportunities.extend([
            "Cash Application",
            "Collections Automation",
            "Dispute Management"
        ])

    # ---------------------------------------------------
    # RTR DETECTION
    # ---------------------------------------------------

    if (
        "gl" in column_text or
        "journal" in column_text or
        "close" in column_text
    ):

        detected_processes.append(
            "RTR (Record-to-Report)"
        )

        automation_opportunities.extend([
            "Month-End Close Automation",
            "Journal Validation",
            "AI Reconciliation"
        ])

    # ---------------------------------------------------
    # WORKFLOW DETECTION
    # ---------------------------------------------------

    if (
        "approval" in column_text or
        "status" in column_text
    ):

        workflow_findings.append(
            "Manual approval workflow detected"
        )

    if (
        "exception" in column_text
    ):

        workflow_findings.append(
            "Exception handling process detected"
        )

    if (
        "sla" in column_text
    ):

        workflow_findings.append(
            "Workflow SLA tracking detected"
        )

    # ---------------------------------------------------
    # SHOW AI FINDINGS
    # ---------------------------------------------------

    st.subheader("Detected ERP Processes")

    for process in detected_processes:

        st.success(process)

    # ---------------------------------------------------
    # SHOW AUTOMATION OPPORTUNITIES
    # ---------------------------------------------------

    st.subheader("AI Automation Opportunities")

    for item in automation_opportunities:

        st.info(item)

    # ---------------------------------------------------
    # SHOW WORKFLOW FINDINGS
    # ---------------------------------------------------

    st.subheader("Workflow Intelligence")

    for finding in workflow_findings:

        st.warning(finding)

    # ---------------------------------------------------
    # AI READINESS SCORE
    # ---------------------------------------------------

    st.subheader("Transformation Readiness")

    readiness_score = min(
        95,
        50 + len(automation_opportunities) * 5
    )

    st.progress(readiness_score)

    st.metric(
        "AI Readiness Score",
        f"{readiness_score}%"
    )

    # ---------------------------------------------------
    # AI RECOMMENDATIONS
    # ---------------------------------------------------

    st.subheader("AI Recommendations")

    recommendations = [

        "Implement intelligent workflow automation",

        "Reduce manual ERP interventions",

        "Enable touchless transaction processing",

        "Deploy AI-driven exception handling",

        "Implement enterprise SLA governance"
    ]

    for rec in recommendations:

        st.success(rec)
    # ---------------------------------------------------
    # FOOTER
    # ---------------------------------------------------

    st.success(
        "ERP Discovery Engine Ready"
    )