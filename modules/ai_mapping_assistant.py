import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------

st.title("AI Mapping Assistant")

st.markdown(
    "AI-Assisted ERP Field Mapping & Data Transformation Intelligence"
)

# ---------------------------------------------------
# FILTERS
# ---------------------------------------------------

f1, f2, f3 = st.columns(3)

with f1:
    source_system = st.selectbox(
        "Source System",
        ["Legacy ERP", "SAP ECC", "Oracle EBS"],
        key="source_system"
    )

with f2:
    target_system = st.selectbox(
        "Target ERP",
        ["Oracle ERP Cloud", "SAP S/4HANA", "Dynamics 365"],
        key="target_system"
    )

with f3:
    object_type = st.selectbox(
        "Object Type",
        ["Customer", "Vendor", "GL", "Inventory"],
        key="mapping_object"
    )

# ---------------------------------------------------
# AI MAPPING SCORECARDS
# ---------------------------------------------------

st.subheader("AI Mapping Metrics")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric("Mapped Fields", "1,248")

with k2:
    st.metric("AI Match Accuracy", "96%")

with k3:
    st.metric("Manual Reviews", "42")

with k4:
    st.metric("Transformation Readiness", "89%")

# ---------------------------------------------------
# FIELD MAPPING TABLE
# ---------------------------------------------------

st.subheader("AI Field Mapping Recommendations")

mapping_df = pd.DataFrame([
    {
        "Source Field": "VENDOR_NAME",
        "Target Field": "SUPPLIER_NAME",
        "AI Confidence": "98%",
        "Transformation Rule": "Direct Mapping",
        "Status": "Approved"
    },
    {
        "Source Field": "GL_ACCOUNT",
        "Target Field": "ACCOUNT_SEGMENT",
        "AI Confidence": "92%",
        "Transformation Rule": "Segment Conversion",
        "Status": "Review Required"
    }
])

st.dataframe(
    mapping_df,
    use_container_width=True
)

# ---------------------------------------------------
# MAPPING ENTRY
# ---------------------------------------------------

st.subheader("Add Mapping Rule")

c1, c2 = st.columns(2)

with c1:

    source_field = st.text_input("Source Field")

    target_field = st.text_input("Target Field")

    transformation_rule = st.selectbox(
        "Transformation Rule",
        [
            "Direct Mapping",
            "Lookup Conversion",
            "Segment Transformation",
            "Derived Logic"
        ],
        key="mapping_rule"
    )

with c2:

    mapping_status = st.selectbox(
        "Mapping Status",
        [
            "Draft",
            "Review Required",
            "Approved"
        ],
        key="mapping_status"
    )

    confidence = st.slider(
        "AI Confidence %",
        0,
        100,
        90
    )

comments = st.text_area("Mapping Comments")

if st.button("Save Mapping Rule"):

    st.success(
        "Mapping rule saved successfully"
    )

# ---------------------------------------------------
# AI MAPPING INSIGHTS
# ---------------------------------------------------

st.subheader("AI Mapping Insights")

st.warning(
    "GL segment transformation complexity detected"
)

st.error(
    "Potential reconciliation mismatch identified for supplier conversions"
)

st.info(
    "Customer master mapping accuracy exceeds 98%"
)

st.success(
    "AI mapping engine optimized transformation sequencing"
)

# ---------------------------------------------------
# RECONCILIATION READINESS
# ---------------------------------------------------

st.subheader("AI Reconciliation Readiness")

st.progress(89)

st.info(
    "Overall mapping reconciliation readiness at 89%"
)

# ---------------------------------------------------
# AI QUERY ASSISTANT
# ---------------------------------------------------

st.subheader("Ask AI Mapping Assistant")

question = st.text_input(
    "Ask mapping transformation question"
)

if st.button("Generate Mapping Insight"):

    if question:

        st.info(f"""
AI Mapping Insight for:
'{question}'

Recommended transformation guidance:
• Validate source-to-target relationships
• Perform reconciliation sampling
• Review derived transformation logic
• Execute additional conversion testing
""")

# ---------------------------------------------------
# FILE UPLOADS
# ---------------------------------------------------

st.subheader("Upload Mapping Sheets")

uploaded_file = st.file_uploader(
    "Upload Source-to-Target Mapping",
    type=["xlsx", "csv", "pdf"]
)

if uploaded_file:

    st.success(
        "Mapping document uploaded successfully"
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.success(
    "AI Mapping Assistant operational successfully"
)