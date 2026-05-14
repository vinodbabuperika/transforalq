import streamlit as st
import pandas as pd

from datetime import date

from database.db import (
    execute_query,
    fetch_data
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("Cost Management")

st.markdown(
    "Enterprise Financial Governance "
    "& Budget Tracking"
)

# =====================================================
# FILE UPLOAD
# =====================================================

st.subheader("Upload Cost Tracker")

uploaded_file = st.file_uploader(
    "Upload Cost Excel",
    type=["xlsx", "csv"]
)

if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):

            upload_df = pd.read_csv(
                uploaded_file
            )

        else:

            upload_df = pd.read_excel(
                uploaded_file
            )

        st.success(
            "Cost file uploaded successfully"
        )

        st.dataframe(
            upload_df.head(),
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Upload Error: {e}"
        )

# =====================================================
# MANUAL COST ENTRY
# =====================================================

st.markdown("---")

st.subheader("Add Project Cost")

with st.form("cost_form"):

    c1, c2 = st.columns(2)

    with c1:

        cost_category = st.selectbox(

            "Cost Category",

            [
                "Implementation",
                "Testing",
                "Infrastructure",
                "License",
                "Support",
                "Hypercare",
                "Change Request"
            ]
        )

        project_name = st.text_input(
            "Project Name"
        )

        vendor_name = st.text_input(
            "Vendor Name"
        )

        budget_amount = st.number_input(
            "Budget Amount",
            min_value=0.0
        )

        actual_amount = st.number_input(
            "Actual Amount",
            min_value=0.0
        )

    with c2:

        forecast_amount = st.number_input(
            "Forecast Amount",
            min_value=0.0
        )

        variance_amount = (
            forecast_amount - actual_amount
        )

        cost_status = st.selectbox(

            "Cost Status",

            [
                "Within Budget",
                "At Risk",
                "Over Budget"
            ]
        )

        invoice_reference = st.text_input(
            "Invoice Reference"
        )

        approved_by = st.text_input(
            "Approved By"
        )

        remarks = st.text_area(
            "Remarks"
        )

    submitted = st.form_submit_button(
        "Add Cost"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO project_costs (

                cost_category,
                project_name,
                vendor_name,
                budget_amount,
                actual_amount,
                forecast_amount,
                variance_amount,
                cost_status,
                invoice_reference,
                approved_by,
                cost_date,
                remarks

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                cost_category,
                project_name,
                vendor_name,
                str(budget_amount),
                str(actual_amount),
                str(forecast_amount),
                str(variance_amount),
                cost_status,
                invoice_reference,
                approved_by,
                str(date.today()),
                remarks

            )
        )

        st.success(
            "Project cost added successfully"
        )

# =====================================================
# COST REGISTER
# =====================================================

st.subheader("Cost Register")

df = fetch_data(
    "SELECT * FROM project_costs"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("Financial KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Cost Records",
        len(df)
    )

with k2:

    total_budget = (
        pd.to_numeric(
            df["budget_amount"],
            errors="coerce"
        ).sum()
        if not df.empty else 0
    )

    st.metric(
        "Budget",
        f"${total_budget:,.0f}"
    )

with k3:

    total_actual = (
        pd.to_numeric(
            df["actual_amount"],
            errors="coerce"
        ).sum()
        if not df.empty else 0
    )

    st.metric(
        "Actual",
        f"${total_actual:,.0f}"
    )

with k4:

    total_forecast = (
        pd.to_numeric(
            df["forecast_amount"],
            errors="coerce"
        ).sum()
        if not df.empty else 0
    )

    st.metric(
        "Forecast",
        f"${total_forecast:,.0f}"
    )