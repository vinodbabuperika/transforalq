import streamlit as st
import pandas as pd
from datetime import date

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("Migration Validation")

st.markdown(
    "Enterprise Data Migration Validation & Reconciliation Governance"
)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

f1, f2, f3, f4 = st.columns(4)

with f1:
    migration_wave = st.selectbox(
        "Migration Wave",
        ["Wave 1", "Wave 2", "Wave 3"],
        key="migration_wave"
    )

with f2:
    object_type = st.selectbox(
        "Object Type",
        ["Customer", "Vendor", "GL Balance", "Inventory"],
        key="migration_object"
    )

with f3:
    migration_status = st.selectbox(
        "Migration Status",
        ["All", "Completed", "In Progress", "Failed"],
        key="migration_status"
    )

with f4:
    reconciliation = st.selectbox(
        "Reconciliation Status",
        ["Matched", "Mismatch", "Pending"],
        key="reconciliation_status"
    )

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Migration KPIs")

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric("Objects Migrated", "18,420")

with k2:
    st.metric("Validated", "16,980")

with k3:
    st.metric("Mismatches", "214")

with k4:
    st.metric("Failed Loads", "18")

with k5:
    st.metric("Migration Readiness", "88%")

# ---------------------------------------------------
# MIGRATION TABLE
# ---------------------------------------------------

st.subheader("Migration Validation Tracker")

migration_df = pd.DataFrame([
    {
        "Object": "Customer Master",
        "Wave": "Wave 1",
        "Status": "Completed",
        "Records": "12,450",
        "Reconciliation": "Matched",
        "Owner": "Data Lead"
    },
    {
        "Object": "GL Balances",
        "Wave": "Wave 1",
        "Status": "Failed",
        "Records": "1,280",
        "Reconciliation": "Mismatch",
        "Owner": "Finance Lead"
    }
])

st.dataframe(
    migration_df,
    use_container_width=True
)

# ---------------------------------------------------
# VALIDATION ENTRY
# ---------------------------------------------------

st.subheader("Add Migration Validation")

c1, c2 = st.columns(2)

with c1:

    migration_object_name = st.text_input("Migration Object")

    wave = st.selectbox(
        "Migration Wave",
        ["Wave 1", "Wave 2", "Wave 3"],
        key="form_wave"
    )

    record_count = st.number_input(
        "Record Count",
        min_value=0
    )

    owner = st.text_input("Migration Owner")

with c2:

    migration_result = st.selectbox(
        "Migration Result",
        ["Completed", "In Progress", "Failed"],
        key="form_result"
    )

    reconciliation_status = st.selectbox(
        "Reconciliation Status",
        ["Matched", "Mismatch", "Pending"],
        key="form_reconciliation"
    )

    validation_date = st.date_input(
        "Validation Date",
        date.today()
    )

mismatch_reason = st.text_area("Mismatch Reason")

correction_plan = st.text_area("Correction Plan")

if st.button("Save Migration Validation"):

    st.success(
        "Migration validation saved successfully"
    )

# ---------------------------------------------------
# AI INSIGHTS
# ---------------------------------------------------

st.subheader("AI Migration Insights")

st.warning(
    "GL balance reconciliation mismatches trending above threshold"
)

st.error(
    "Failed inventory migration loads may impact cutover readiness"
)

st.info(
    "Customer master migration accuracy improved to 98.7%"
)

# ---------------------------------------------------
# MIGRATION READINESS
# ---------------------------------------------------

st.subheader("Migration Readiness Dashboard")

st.progress(88)

st.success(
    "Overall migration readiness at 88%"
)

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

st.subheader("Upload Migration Evidence")

uploaded_file = st.file_uploader(
    "Upload Reconciliation / Validation Evidence",
    type=["xlsx", "csv", "pdf", "docx"]
)

if uploaded_file:

    st.success(
        "Migration evidence uploaded successfully"
    )