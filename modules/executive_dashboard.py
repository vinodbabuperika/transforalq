import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO
selected_client = st.session_state[
    "selected_client"
]
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from services.db_service import fetch_data

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title(
    f"Executive Dashboard - {selected_client}"
)

st.markdown(
    "AI-Powered ERP Transformation Command Center"
)
st.subheader("Client Transformation Summary")

st.info(
    f"""
Client: {selected_client}

Transformation Program:
AI-Powered ERP Workflow Modernization

Deployment Model:
Multi-Tenant Enterprise SaaS

Current Focus:
Workflow automation, AI governance,
testing acceleration, deployment readiness
"""
)
# ---------------------------------------------------
# FETCH DATA
# ---------------------------------------------------

raid_df = fetch_data(
    f"""
    SELECT * FROM raid_log
    WHERE client_name = '{selected_client}'
    """
)

project_df = fetch_data(
    "SELECT * FROM project_plan"
)

defect_df = fetch_data(
    "SELECT * FROM defect_tracker"
)

# ---------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------

open_risks = 0

if not raid_df.empty:

    open_risks = len(
        raid_df[
            (raid_df["raid_type"] == "Risk") &
            (raid_df["status"] != "Closed")
        ]
    )

open_defects = 0

if not defect_df.empty:

    open_defects = len(
        defect_df[
            defect_df["defect_status"] != "Closed"
        ]
    )

delayed_tasks = 0

if not project_df.empty:

    delayed_tasks = len(
        project_df[
            project_df["status"] == "Delayed"
        ]
    )

go_live_readiness = max(
    0,
    100 - (
        open_risks * 2 +
        open_defects +
        delayed_tasks * 3
    )
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Transformation KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Open Risks",
        open_risks
    )

with k2:

    st.metric(
        "Open Defects",
        open_defects
    )

with k3:

    st.metric(
        "Delayed Tasks",
        delayed_tasks
    )

with k4:

    st.metric(
        "Go-Live Readiness",
        f"{go_live_readiness}%"
    )
# ---------------------------------------------------
# VISUAL ANALYTICS
# ---------------------------------------------------

st.subheader("Transformation Analytics")

c1, c2 = st.columns(2)

# ---------------------------------------------------
# DEFECT STATUS CHART
# ---------------------------------------------------

with c1:

    if not defect_df.empty:

        defect_chart = (
            defect_df["defect_status"]
            .value_counts()
            .reset_index()
        )

        defect_chart.columns = [
            "Status",
            "Count"
        ]

        fig = px.pie(
            defect_chart,
            names="Status",
            values="Count",
            title="Defect Status Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ---------------------------------------------------
# PROJECT STATUS CHART
# ---------------------------------------------------

with c2:

    if not project_df.empty:

        project_chart = (
            project_df["status"]
            .value_counts()
            .reset_index()
        )

        project_chart.columns = [
            "Status",
            "Count"
        ]

        fig2 = px.bar(
            project_chart,
            x="Status",
            y="Count",
            title="Project Task Status"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )
# ---------------------------------------------------
# DELIVERY HEALTH
# ---------------------------------------------------

st.subheader("Delivery Health")

if go_live_readiness >= 85:

    st.success(
        "Program delivery health is stable"
    )

elif go_live_readiness >= 70:

    st.warning(
        "Program risks require attention"
    )

else:

    st.error(
        "Program delivery risk is critical"
    )

# ---------------------------------------------------
# AI INSIGHTS
# ---------------------------------------------------

st.subheader("AI Transformation Insights")

if open_defects > 10:

    st.warning(
        "High defect volume may impact SIT/UAT timelines"
    )

if delayed_tasks > 5:

    st.error(
        "Project delays detected across workstreams"
    )

if open_risks > 3:

    st.warning(
        "Risk exposure increasing before deployment"
    )

if (
    open_risks <= 3 and
    open_defects <= 10 and
    delayed_tasks <= 5
):

    st.success(
        "Transformation program tracking within tolerance"
    )

# ---------------------------------------------------
# DATA TABLES
# ---------------------------------------------------

st.subheader("Recent Risks")

if not raid_df.empty:

    st.dataframe(
        raid_df.tail(5),
        use_container_width=True
    )

st.subheader("Recent Defects")

if not defect_df.empty:

    st.dataframe(
        defect_df.tail(5),
        use_container_width=True
    )

st.subheader("Recent Project Tasks")

if not project_df.empty:

    st.dataframe(
        project_df.tail(5),
        use_container_width=True
    )
    # ---------------------------------------------------
# SAMPLE DATA
# ---------------------------------------------------

project_df = pd.DataFrame({
    "status": [
        "Completed",
        "In Progress",
        "Delayed",
        "Completed",
        "In Progress"
    ]
})

defect_df = pd.DataFrame({
    "defect_status": [
        "Open",
        "Resolved",
        "Closed",
        "Open",
        "Resolved",
        "Open"
    ]
})

# ---------------------------------------------------
# VISUAL ANALYTICS
# ---------------------------------------------------

st.subheader("Transformation Analytics")

c1, c2 = st.columns(2)

# ---------------------------------------------------
# DEFECT STATUS CHART
# ---------------------------------------------------

with c1:

    defect_chart = (
        defect_df["defect_status"]
        .value_counts()
        .reset_index()
    )

    defect_chart.columns = [
        "Status",
        "Count"
    ]

    fig = px.pie(
        defect_chart,
        names="Status",
        values="Count",
        title="Defect Status Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------------
# PROJECT STATUS CHART
# ---------------------------------------------------

with c2:

    project_chart = (
        project_df["status"]
        .value_counts()
        .reset_index()
    )

    project_chart.columns = [
        "Status",
        "Count"
    ]

    fig2 = px.bar(
        project_chart,
        x="Status",
        y="Count",
        title="Project Task Status"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )
    # ---------------------------------------------------
# PDF EXECUTIVE REPORT
# ---------------------------------------------------

st.subheader("Executive Report Export")

if st.button(
    "Generate Executive PDF Report"
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    # ---------------------------------------------------
    # TITLE
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "TransforaIQ Executive Dashboard Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    # ---------------------------------------------------
    # KPI SUMMARY
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            f"Open Risks: {open_risks}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Open Defects: {open_defects}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Delayed Tasks: {delayed_tasks}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Go-Live Readiness: {go_live_readiness}%",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # ---------------------------------------------------
    # AI SUMMARY
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "AI Transformation Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "Program delivery progressing with moderate risk exposure.",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "Focus required on defect stabilization and deployment readiness.",
            styles["BodyText"]
        )
    )

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    st.download_button(
        label="Download Executive PDF",
        data=pdf,
        file_name="executive_dashboard_report.pdf",
        mime="application/pdf"
    )