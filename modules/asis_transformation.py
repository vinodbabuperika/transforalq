import streamlit as st

st.title("AS-IS Transformation Summary")

content = st.session_state.get(

    "asis_summary",

    "No AS-IS summary generated yet."

)

st.text_area(

    "AS-IS Transformation",

    value=content,

    height=700

)
