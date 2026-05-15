import streamlit as st
st.title("Resource Management")

st.success(
    "Resource Management Module Loaded"
)

# =====================================================
# FILE UPLOAD
# =====================================================

st.subheader("Upload Resource Plan")

uploaded_file = st.file_uploader(
    "Upload Resource Excel",
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
            "Resource file uploaded successfully"
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
# MANUAL RESOURCE ENTRY
# =====================================================

st.markdown("---")

st.subheader("Add Resource")

with st.form("resource_form"):

    c1, c2 = st.columns(2)

    with c1:

        employee_name = st.text_input(
            "Employee Name"
        )

        employee_id = st.text_input(
            "Employee ID"
        )

        role = st.text_input(
            "Role"
        )

        department = st.text_input(
            "Department"
        )

        project_name = st.text_input(
            "Project Name"
        )

        skillset = st.text_area(
            "Skillset"
        )

    with c2:

        allocation_percentage = (
            st.number_input(
                "Allocation %",
                min_value=0,
                max_value=100,
                value=100
            )
        )

        manager = st.text_input(
            "Manager"
        )

        location = st.text_input(
            "Location"
        )

        availability_status = st.selectbox(

            "Availability",

            [
                "Allocated",
                "Partially Available",
                "Available",
                "On Leave"
            ]
        )

        start_date = st.date_input(
            "Start Date",
            date.today()
        )

        end_date = st.date_input(
            "End Date",
            date.today()
        )

        remarks = st.text_area(
            "Remarks"
        )

    submitted = st.form_submit_button(
        "Add Resource"
    )

    if submitted:

        execute_query(

            """

            INSERT INTO resources (

                employee_name,
                employee_id,
                role,
                department,
                project_name,
                allocation_percentage,
                skillset,
                manager,
                location,
                availability_status,
                start_date,
                end_date,
                remarks

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                employee_name,
                employee_id,
                role,
                department,
                project_name,
                str(allocation_percentage),
                skillset,
                manager,
                location,
                availability_status,
                str(start_date),
                str(end_date),
                remarks

            )
        )

        st.success(
            "Resource added successfully"
        )

# =====================================================
# RESOURCE REGISTER
# =====================================================

st.subheader("Resource Register")

df = fetch_data(
    "SELECT * FROM resources"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("Resource KPIs")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Resources",
        len(df)
    )

with k2:

    allocated = len(

        df[
            df["availability_status"]
            == "Allocated"
        ]

    ) if not df.empty else 0

    st.metric(
        "Allocated",
        allocated
    )

with k3:

    available = len(

        df[
            df["availability_status"]
            == "Available"
        ]

    ) if not df.empty else 0

    st.metric(
        "Available",
        available
    )

with k4:

    partial = len(

        df[
            df["availability_status"]
            == "Partially Available"
        ]

    ) if not df.empty else 0

    st.metric(
        "Partial",
        partial
    )