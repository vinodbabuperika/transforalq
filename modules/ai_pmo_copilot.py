import streamlit as st
import pandas as pd

from database.db import fetch_data

# =====================================================
# PAGE HEADER
# =====================================================

st.title("AI PMO Copilot")

st.markdown(
    "AI-powered ERP Transformation "
    "Governance Assistant"
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
# USER QUESTION
# =====================================================

st.subheader("Ask AI PMO Copilot")

question = st.text_input(
    "Ask governance question"
)

# =====================================================
# AI RESPONSE ENGINE
# =====================================================

if question:

    q = question.lower()

    st.markdown("---")

    st.subheader("AI Response")

    # -------------------------------------
    # OPEN DEFECTS
    # -------------------------------------

    if "open defect" in q:

        open_defects = len(

            defect_df[
                defect_df["issue_status"]
                == "Open"
            ]

        ) if not defect_df.empty else 0

        st.write(
            f"There are "
            f"{open_defects} open defects."
        )

    # -------------------------------------
    # SIT FAILURES
    # -------------------------------------

    elif "sit" in q and "fail" in q:

        sit_failed = len(

            sit_df[
                sit_df["testing_status"]
                == "Failed"
            ]

        ) if not sit_df.empty else 0

        st.write(
            f"There are "
            f"{sit_failed} SIT failures."
        )

    # -------------------------------------
    # UAT FAILURES
    # -------------------------------------

    elif "uat" in q and "fail" in q:

        uat_failed = len(

            uat_df[
                uat_df["testing_status"]
                == "Failed"
            ]

        ) if not uat_df.empty else 0

        st.write(
            f"There are "
            f"{uat_failed} UAT failures."
        )

    # -------------------------------------
    # BUDGET STATUS
    # -------------------------------------

    elif "budget" in q:

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

                st.error(
                    "Project exceeds approved budget"
                )

            else:

                st.success(
                    "Project budget healthy"
                )

            st.write(
                f"Budget: ${total_budget:,.0f}"
            )

            st.write(
                f"Actual: ${total_actual:,.0f}"
            )

    # -------------------------------------
    # RESOURCE STATUS
    # -------------------------------------

    elif "resource" in q:

        total_resources = (
            len(resource_df)
            if not resource_df.empty else 0
        )

        available_resources = len(

            resource_df[
                resource_df[
                    "availability_status"
                ] == "Available"
            ]

        ) if not resource_df.empty else 0

        st.write(
            f"Total resources: "
            f"{total_resources}"
        )

        st.write(
            f"Available resources: "
            f"{available_resources}"
        )

    # -------------------------------------
    # GO-LIVE READINESS
    # -------------------------------------

    elif "go live" in q or "readiness" in q:

        open_defects = len(

            defect_df[
                defect_df["issue_status"]
                == "Open"
            ]

        ) if not defect_df.empty else 0

        sit_failed = len(

            sit_df[
                sit_df["testing_status"]
                == "Failed"
            ]

        ) if not sit_df.empty else 0

        readiness = max(
            0,
            100 - (
                open_defects * 2
                + sit_failed * 3
            )
        )

        st.write(
            f"Estimated Go-Live "
            f"Readiness: {readiness}%"
        )

    # -------------------------------------
    # DEFAULT RESPONSE
    # -------------------------------------

    else:

        st.info(
            "AI PMO Copilot could not "
            "understand the request."
        )

        st.write(
            "Try questions like:"
        )

        st.write(
            "- Open defects"
        )

        st.write(
            "- SIT failures"
        )

        st.write(
            "- Budget status"
        )

        st.write(
            "- Resource availability"
        )

        st.write(
            "- Go live readiness"
        )

# =====================================================
# QUICK GOVERNANCE INSIGHTS
# =====================================================

st.markdown("---")

st.subheader("Quick AI Insights")

open_defects = len(

    defect_df[
        defect_df["issue_status"]
        == "Open"
    ]

) if not defect_df.empty else 0

sit_failed = len(

    sit_df[
        sit_df["testing_status"]
        == "Failed"
    ]

) if not sit_df.empty else 0

if open_defects > 10:

    st.warning(
        "Critical defect backlog increasing"
    )

if sit_failed > 5:

    st.error(
        "SIT execution instability detected"
    )

st.success(
    "AI PMO Copilot operational"
)