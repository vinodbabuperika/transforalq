import streamlit as st
from datetime import datetime

st.title("Configuration Workspace")

content = st.session_state.get(

    "config_output",

    "No Configuration generated yet."

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

    "Configuration Workbook",

    value=content,

    height=700

)
