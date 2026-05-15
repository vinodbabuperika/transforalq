import streamlit as st

st.title("TO-BE Process Summary")

content = st.session_state.get(

    "tobe_summary",

    "No TO-BE summary generated yet."

)

st.text_area(

    "TO-BE Process",

    value=content,

    height=700

)
