import streamlit as st
import pandas as pd

from database.db import fetch_data

# =====================================================
# PAGE HEADER
# =====================================================

st.title("Executive Dashboard")

st.markdown(
    "Enterprise ERP Transformation "
    "Command Center"
)

# =====================================================
# LOAD DATA
# =====================================================

project_df = fetch_data(
    "SELECT * FROM project_plan"
)

defect_df = fetch_data(
    "SELECT * FROM defects"
)

sit_df = fetch_data(
    "SELECT * FROM sit_scripts"
)

uat_df = fetch_data(
    "SELECT * FROM uat_scripts"
)

resource_df = fetch_data(
    "SELECT * FROM resources"
)

cost_df = fetch_data(
    "SELECT * FROM project_costs"
)

# =====================================================
# EXECUTIVE KPIs
# =====================================================

st.subheader("Transformation KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    total_projects = (
        len(project_df)
        if not project_df.empty else 0
    )

    st.metric(
        "Project Tasks",
        total_projects
    )

with k2:

    open_defects = len(

        defect_df[
            defect_df["issue_status"] == "Open"
        ]

    ) if not defect_df.empty else 0

    st.metric(
        "Open Defects",
        open_defects
    )

with k3:

    sit_failed = len(

        sit_df[
            sit_df["testing_status"] == "Failed"
        ]

    ) if not sit_df.empty else 0

    st.metric(
        "SIT Failed",
        sit_failed
    )

with k4:

    uat_failed = len(

        uat_df[
            uat_df["testing_status"] == "Failed"
        ]

    ) if not uat_df.empty else 0

    st.metric(
        "UAT Failed",
        uat_failed
    )

# =====================================================
# FINANCIAL KPIs
# =====================================================

st.subheader("Financial Health")

f1, f2, f3 = st.columns(3)

with f1:

    total_budget = (
        pd.to_numeric(
            cost_df["budget_amount"],
            errors="coerce"
        ).sum()
        if not cost_df.empty else 0
    )

    st.metric(
        "Budget",
        f"${total_budget:,.0f}"
    )

with f2:

    total_actual = (
        pd.to_numeric(
            cost_df["actual_amount"],
            errors="coerce"
        ).sum()
        if not cost_df.empty else 0
    )

    st.metric(
        "Actual",
        f"${total_actual:,.0f}"
    )

with f3:

    total_forecast = (
        pd.to_numeric(
            cost_df["forecast_amount"],
            errors="coerce"
        ).sum()
        if not cost_df.empty else 0
    )

    st.metric(
        "Forecast",
        f"${total_forecast:,.0f}"
    )

# =====================================================
# RESOURCE HEALTH
# =====================================================

st.subheader("Resource Health")

r1, r2, r3 = st.columns(3)

with r1:

    total_resources = (
        len(resource_df)
        if not resource_df.empty else 0
    )

    st.metric(
        "Resources",
        total_resources
    )

with r2:

    allocated = len(

        resource_df[
            resource_df["availability_status"]
            == "Allocated"
        ]

    ) if not resource_df.empty else 0

    st.metric(
        "Allocated",
        allocated
    )

with r3:

    available = len(

        resource_df[
            resource_df["availability_status"]
            == "Available"
        ]

    ) if not resource_df.empty else 0

    st.metric(
        "Available",
        available
    )

# =====================================================
# AI INSIGHTS
# =====================================================

st.subheader("AI Insights")

if open_defects > 10:

    st.warning(
        "High defect volume detected"
    )

if sit_failed > 5:

    st.error(
        "SIT execution risk identified"
    )

if total_actual > total_budget:

    st.error(
        "Project exceeds approved budget"
    )

if available < 2:

    st.warning(
        "Low resource availability"
    )

st.success(
    "AI Transformation Governance "
    "operational"
)

# =====================================================
# DATA REGISTERS
# =====================================================

st.subheader("Recent Project Tasks")

st.dataframe(
    project_df.head(10),
    use_container_width=True
)

st.subheader("Recent Defects")

st.dataframe(
    defect_df.head(10),
    use_container_width=True
)