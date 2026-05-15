import streamlit as st
from datetime import datetime

st.title("TDD Workspace")

content = st.session_state.get(

    "tdd_output",

    "No TDD generated yet."

)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Version", "1.0")

with c2:
    st.metric("Status", "In Review")

with c3:
    st.metric(
        "Review Date",
        datetime.now().strftime("%d-%b-%Y")
    )

st.markdown("---")

st.text_area(

    "Technical Design Document",

    value=content,

    height=700

)
