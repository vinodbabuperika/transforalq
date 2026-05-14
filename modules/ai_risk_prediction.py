import streamlit as st
import pandas as pd

from database.db import fetch_data

# =====================================================
# PAGE HEADER
# =====================================================

st.title("AI Risk Prediction")

st.markdown(
    "AI-powered Transformation "
    "Risk Intelligence Engine"
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
# AI RISK CALCULATION
# =====================================================

risk_score = 0

# -------------------------------------
# OPEN DEFECT RISK
# -------------------------------------

open_defects = len(

    defect_df[
        defect_df["issue_status"] == "Open"
    ]

) if not defect_df.empty else 0

if open_defects > 10:
    risk_score += 25

elif open_defects > 5:
    risk_score += 15

# -------------------------------------
# SIT FAILURE RISK
# -------------------------------------

sit_failed = len(

    sit_df[
        sit_df["testing_status"] == "Failed"
    ]

) if not sit_df.empty else 0

if sit_failed > 10:
    risk_score += 25

elif sit_failed > 5:
    risk_score += 15

# -------------------------------------
# UAT FAILURE RISK
# -------------------------------------

uat_failed = len(

    uat_df[
        uat_df["testing_status"] == "Failed"
    ]

) if not uat_df.empty else 0

if uat_failed > 5:
    risk_score += 20

elif uat_failed > 2:
    risk_score += 10

# -------------------------------------
# RESOURCE RISK
# -------------------------------------

allocated_resources = len(

    resource_df[
        resource_df["availability_status"]
        == "Allocated"
    ]

) if not resource_df.empty else 0

available_resources = len(

    resource_df[
        resource_df["availability_status"]
        == "Available"
    ]

) if not resource_df.empty else 0

if available_resources < 2:
    risk_score += 15

# -------------------------------------
# COST RISK
# -------------------------------------

if not cost_df.empty:

    total_budget = pd.to_numeric(

        cost_df["budget_amount"],
        errors="coerce"

    ).sum()

    total_actual = pd.to_numeric(

        cost_df["actual_amount"],
        errors="coerce"

    ).sum()

    if total_actual > total_budget:
        risk_score += 25

# =====================================================
# RISK LEVEL
# =====================================================

if risk_score >= 70:

    risk_level = "HIGH"

elif risk_score >= 40:

    risk_level = "MEDIUM"

else:

    risk_level = "LOW"

# =====================================================
# EXECUTIVE RISK DASHBOARD
# =====================================================

st.subheader("Transformation Risk Score")

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Risk Score",
        f"{risk_score}%"
    )

with k2:

    st.metric(
        "Risk Level",
        risk_level
    )

with k3:

    go_live_readiness = max(
        0,
        100 - risk_score
    )

    st.metric(
        "Go-Live Readiness",
        f"{go_live_readiness}%"
    )

# =====================================================
# AI GOVERNANCE INSIGHTS
# =====================================================

st.subheader("AI Governance Insights")

# -------------------------------------
# DEFECT ALERTS
# -------------------------------------

if open_defects > 10:

    st.error(
        "Critical defect volume detected"
    )

elif open_defects > 5:

    st.warning(
        "Defect trend increasing"
    )

else:

    st.success(
        "Defect levels stable"
    )

# -------------------------------------
# SIT ALERTS
# -------------------------------------

if sit_failed > 10:

    st.error(
        "SIT execution instability identified"
    )

elif sit_failed > 5:

    st.warning(
        "SIT failures increasing"
    )

else:

    st.success(
        "SIT execution stable"
    )

# -------------------------------------
# UAT ALERTS
# -------------------------------------

if uat_failed > 5:

    st.error(
        "Business validation risk identified"
    )

elif uat_failed > 2:

    st.warning(
        "UAT issues require governance attention"
    )

else:

    st.success(
        "UAT execution healthy"
    )

# -------------------------------------
# RESOURCE ALERTS
# -------------------------------------

if available_resources < 2:

    st.warning(
        "Critical resource bandwidth issue"
    )

else:

    st.success(
        "Resource availability healthy"
    )

# -------------------------------------
# COST ALERTS
# -------------------------------------

if not cost_df.empty:

    if total_actual > total_budget:

        st.error(
            "Project exceeds approved budget"
        )

    else:

        st.success(
            "Financial governance stable"
        )

# =====================================================
# AI HEATMAP
# =====================================================

st.subheader("AI Risk Heatmap")

heatmap_data = pd.DataFrame({

    "Governance Area": [

        "Defects",
        "SIT",
        "UAT",
        "Resources",
        "Cost"

    ],

    "Risk Score": [

        open_defects,
        sit_failed,
        uat_failed,
        allocated_resources,
        risk_score

    ]
})

st.dataframe(
    heatmap_data,
    use_container_width=True
)

# =====================================================
# EXECUTIVE RECOMMENDATIONS
# =====================================================

st.subheader("AI Recommendations")

if risk_level == "HIGH":

    st.error(
        "Immediate governance intervention required"
    )

    st.write(
        "- Launch executive war room"
    )

    st.write(
        "- Freeze non-critical CRs"
    )

    st.write(
        "- Increase SIT/UAT governance"
    )

    st.write(
        "- Deploy additional SMEs"
    )

elif risk_level == "MEDIUM":

    st.warning(
        "Controlled governance action recommended"
    )

    st.write(
        "- Increase testing reviews"
    )

    st.write(
        "- Track milestone slippage"
    )

    st.write(
        "- Monitor resource utilization"
    )

else:

    st.success(
        "Transformation governance healthy"
    )

    st.write(
        "- Continue current governance model"
    )

    st.write(
        "- Maintain delivery cadence"
    )

# =====================================================
# FINAL STATUS
# =====================================================

st.markdown("---")

st.success(
    "AI Risk Prediction Engine Operational"
)