import streamlit as st
import pandas as pd

from database.db import fetch_data

# =====================================================
# PAGE HEADER
# =====================================================

st.title("Go-Live Readiness Command Center")

st.markdown(
    "Enterprise ERP Go-Live "
    "Governance & Readiness"
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

deployment_df = fetch_data(
    "SELECT * FROM deployment_tracker"
)

hypercare_df = fetch_data(
    "SELECT * FROM hypercare_issues"
)

raid_df = fetch_data(
    "SELECT * FROM raid_log"
)

# =====================================================
# READINESS SCORING ENGINE
# =====================================================

score = 100

# -------------------------------------
# OPEN DEFECTS
# -------------------------------------

open_defects = len(

    defect_df[
        defect_df["issue_status"] == "Open"
    ]

) if not defect_df.empty else 0

score -= open_defects * 2

# -------------------------------------
# FAILED SIT
# -------------------------------------

sit_failed = len(

    sit_df[
        sit_df["testing_status"] == "Failed"
    ]

) if not sit_df.empty else 0

score -= sit_failed * 3

# -------------------------------------
# FAILED UAT
# -------------------------------------

uat_failed = len(

    uat_df[
        uat_df["testing_status"] == "Failed"
    ]

) if not uat_df.empty else 0

score -= uat_failed * 4

# -------------------------------------
# RAID OPEN ITEMS
# -------------------------------------

open_raid = len(

    raid_df[
        raid_df["status"] == "Open"
    ]

) if not raid_df.empty else 0

score -= open_raid * 2

# -------------------------------------
# DEPLOYMENT BLOCKERS
# -------------------------------------

blocked_deployments = len(

    deployment_df[
        deployment_df["deployment_status"]
        == "Blocked"
    ]

) if not deployment_df.empty else 0

score -= blocked_deployments * 5

# -------------------------------------
# HYPERCARE CRITICALS
# -------------------------------------

critical_incidents = len(

    hypercare_df[
        hypercare_df["severity"]
        == "Critical"
    ]

) if not hypercare_df.empty else 0

score -= critical_incidents * 4

# -------------------------------------
# RESOURCE AVAILABILITY
# -------------------------------------

available_resources = len(

    resource_df[
        resource_df["availability_status"]
        == "Available"
    ]

) if not resource_df.empty else 0

if available_resources < 2:
    score -= 10

# -------------------------------------
# COST HEALTH
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
        score -= 15

# -------------------------------------
# FINAL SCORE NORMALIZATION
# -------------------------------------

score = max(0, min(100, score))

# =====================================================
# GO-LIVE STATUS
# =====================================================

if score >= 90:

    readiness = "READY"

elif score >= 70:

    readiness = "AT RISK"

else:

    readiness = "NOT READY"

# =====================================================
# EXECUTIVE KPI DASHBOARD
# =====================================================

st.subheader("Go-Live Readiness")

k1, k2, k3 = st.columns(3)

with k1:

    st.metric(
        "Readiness Score",
        f"{score}%"
    )

with k2:

    st.metric(
        "Go-Live Status",
        readiness
    )

with k3:

    confidence = max(
        0,
        score - 5
    )

    st.metric(
        "Deployment Confidence",
        f"{confidence}%"
    )

# =====================================================
# GOVERNANCE HEALTH
# =====================================================

st.subheader("Transformation Health")

g1, g2, g3, g4 = st.columns(4)

with g1:

    st.metric(
        "Open Defects",
        open_defects
    )

with g2:

    st.metric(
        "SIT Failures",
        sit_failed
    )

with g3:

    st.metric(
        "UAT Failures",
        uat_failed
    )

with g4:

    st.metric(
        "Deployment Blockers",
        blocked_deployments
    )

# =====================================================
# AI READINESS INSIGHTS
# =====================================================

st.subheader("AI Readiness Insights")

# -------------------------------------
# GO-LIVE DECISION
# -------------------------------------

if readiness == "READY":

    st.success(
        "Program ready for go-live"
    )

elif readiness == "AT RISK":

    st.warning(
        "Controlled go-live risk identified"
    )

else:

    st.error(
        "Go-live NOT recommended"
    )

# -------------------------------------
# DEFECT RISK
# -------------------------------------

if open_defects > 10:

    st.error(
        "Critical defect backlog unresolved"
    )

elif open_defects > 5:

    st.warning(
        "Defect closure velocity low"
    )

else:

    st.success(
        "Defect governance healthy"
    )

# -------------------------------------
# TESTING RISK
# -------------------------------------

if sit_failed > 5 or uat_failed > 5:

    st.error(
        "Testing instability detected"
    )

else:

    st.success(
        "Testing readiness healthy"
    )

# -------------------------------------
# DEPLOYMENT RISK
# -------------------------------------

if blocked_deployments > 2:

    st.error(
        "Deployment blockers unresolved"
    )

else:

    st.success(
        "Deployment readiness stable"
    )

# -------------------------------------
# RESOURCE RISK
# -------------------------------------

if available_resources < 2:

    st.warning(
        "Critical resource bandwidth risk"
    )

else:

    st.success(
        "Resource readiness healthy"
    )

# =====================================================
# AI EXECUTIVE RECOMMENDATIONS
# =====================================================

st.subheader("AI Executive Recommendations")

if readiness == "NOT READY":

    st.error(
        "Executive intervention required"
    )

    st.write(
        "- Delay go-live approval"
    )

    st.write(
        "- Resolve critical defects"
    )

    st.write(
        "- Increase command center governance"
    )

    st.write(
        "- Add deployment support coverage"
    )

elif readiness == "AT RISK":

    st.warning(
        "Controlled deployment recommended"
    )

    st.write(
        "- Increase hypercare staffing"
    )

    st.write(
        "- Monitor deployment waves closely"
    )

    st.write(
        "- Conduct daily executive governance"
    )

else:

    st.success(
        "Go-live recommended"
    )

    st.write(
        "- Proceed with deployment plan"
    )

    st.write(
        "- Activate hypercare support"
    )

    st.write(
        "- Continue governance cadence"
    )

# =====================================================
# EXECUTIVE DATA VIEW
# =====================================================

st.subheader("Recent Critical Defects")

critical_df = defect_df[
    defect_df["defect_priority"]
    == "Critical"
] if not defect_df.empty else pd.DataFrame()

st.dataframe(
    critical_df.head(10),
    use_container_width=True
)

# =====================================================
# FINAL STATUS
# =====================================================

st.markdown("---")

st.success(
    "Go-Live Command Center Operational"
)