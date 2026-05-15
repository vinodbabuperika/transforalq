import streamlit as st
from datetime import datetime

st.title("FDD Workspace")

st.markdown(
    "Enterprise Functional Design Review Portal"
)

# =====================================================
# LOAD GENERATED FDD
# =====================================================

fdd_content = st.session_state.get(

    "fdd_output",

    "No FDD generated yet."

)

# =====================================================
# DOCUMENT HEADER
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Version",
        "1.0"
    )

with c2:

    st.metric(
        "Status",
        "In Review"
    )

with c3:

    st.metric(
        "Review Date",
        datetime.now().strftime("%d-%b-%Y")
    )

st.markdown("---")

# =====================================================
# APPROVAL DETAILS
# =====================================================

c1, c2 = st.columns(2)

with c1:

    approver = st.text_input(
        "Approver ID"
    )

with c2:

    approval_date = st.date_input(
        "Approval Date"
    )

review_comments = st.text_area(

    "Reviewer Comments",

    height=120

)

# =====================================================
# FDD CONTENT
# =====================================================

st.subheader("FDD Document")

edited_fdd = st.text_area(

    "Functional Design Document",

    value=fdd_content,

    height=700

)

# =====================================================
# ACTIONS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("Approve FDD"):

        st.success(
            "FDD Approved Successfully"
        )

with c2:

    if st.button("Request Changes"):

        st.warning(
            "Changes Requested"
        )

with c3:

    if st.button("Save Version"):

        st.success(
            "Version Saved"
        )