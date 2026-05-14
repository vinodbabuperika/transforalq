import streamlit as st
import pandas as pd

st.title("Statement of Work")

st.markdown("Enterprise Statement of Work and management")

# KPI SECTION

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Open Tasks", "42")

with col2:
    st.metric("Delayed Tasks", "5")

with col3:
    st.metric("Completion", "76%")

with col4:
    st.metric("Milestones", "12")

# PROJECT TABLE

st.subheader("Project Activities")

df = pd.DataFrame([
    {
        "Phase": "Design",
        "Owner": "Finance Lead",
        "Status": "Completed"
    },
    {
        "Phase": "Build",
        "Owner": "SI Partner",
        "Status": "In Progress"
    }
])

st.dataframe(df, use_container_width=True)

# AI INSIGHTS

st.subheader("AI Insights")

st.info("2 milestones at risk due to SIT delays")

st.warning("Finance signoff pending")

# FILE UPLOAD SECTION

st.subheader("Upload Evidence")

uploaded_file = st.file_uploader(
    "Upload File",
    type=["xlsx", "csv", "pdf", "docx"]
)

if uploaded_file:
    st.success("File uploaded successfully")