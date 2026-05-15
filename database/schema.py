from database.db import execute_query


# =========================================
# CREATE TABLES
# =========================================

def create_tables():
# -------------------------------------
# PROJECT PLAN
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS project_plan (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        client_name TEXT,
        phase TEXT,
        task_name TEXT,
        deliverable TEXT,
        owner TEXT,
        status TEXT,
        planned_start_date TEXT,
        planned_end_date TEXT,
        actual_start_date TEXT,
        actual_end_date TEXT,
        dependency TEXT,
        remarks TEXT

    )

    """)
        # -------------------------------------
        # CLIENTS
        # -------------------------------------

    execute_query("""

        CREATE TABLE IF NOT EXISTS clients (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            client_name TEXT,
            industry TEXT,
            region TEXT,
            erp_platform TEXT,
            status TEXT

        )

        """)

    # -------------------------------------
    # PROJECTS
    # -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS projects (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        project_name TEXT,
        client_name TEXT,
        phase TEXT,
        status TEXT,
        start_date TEXT,
        end_date TEXT

    )

    """)

    # -------------------------------------
    # STAKEHOLDERS
    # -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS stakeholders (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        stakeholder_name TEXT,
        role TEXT,
        email TEXT,
        client_name TEXT,
        workstream TEXT

    )

    """)

    # -------------------------------------
# DEFECTS
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS defects (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    defect_id TEXT,
    tool_name TEXT,
    defect_type TEXT,
    defect_priority TEXT,
    module_name TEXT,
    issue_description TEXT,
    impacted_data TEXT,
    reported_by TEXT,
    reported_date TEXT,
    issue_status TEXT,
    resolution_owner TEXT,
    resolution_team TEXT,
    resolution_comments TEXT,
    expected_closure_date TEXT,
    root_cause_analysis TEXT,
    actual_closure_date TEXT,
    ageing_reported_days TEXT,
    ageing_expected_days TEXT

    )

    """)
# -------------------------------------
# SIT SCRIPTS
# -------------------------------------

    execute_query("""

CREATE TABLE IF NOT EXISTS sit_scripts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    scenario_id TEXT,
    scenario_type TEXT,
    execution_day TEXT,
    master_data TEXT,
    entity_details TEXT,
    test_scenario TEXT,
    test_steps TEXT,
    expected_outcome TEXT,
    testing_status TEXT,
    tester_name TEXT,
    executed_date TEXT,
    test_data TEXT,
    defect_id TEXT,
    operation_remarks TEXT,
    other_team_remarks TEXT,
    action_owner TEXT,
    ageing TEXT

    )

    """)
# -------------------------------------
# UAT SCRIPTS
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS uat_scripts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    scenario_id TEXT,
    scenario_type TEXT,
    execution_day TEXT,
    master_data TEXT,
    entity_details TEXT,
    test_scenario TEXT,
    test_steps TEXT,
    expected_outcome TEXT,
    testing_status TEXT,
    tester_name TEXT,
    executed_date TEXT,
    test_data TEXT,
    defect_id TEXT,
    operation_remarks TEXT,
    other_team_remarks TEXT,
    action_owner TEXT,
    ageing TEXT

    )

    """)
# -------------------------------------
# RESOURCE MANAGEMENT
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS resources (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    employee_name TEXT,
    employee_id TEXT,
    role TEXT,
    department TEXT,
    project_name TEXT,
    allocation_percentage TEXT,
    skillset TEXT,
    manager TEXT,
    location TEXT,
    availability_status TEXT,
    start_date TEXT,
    end_date TEXT,
    remarks TEXT

    )

    """)
# -------------------------------------
# COST MANAGEMENT
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS project_costs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    cost_category TEXT,
    project_name TEXT,
    vendor_name TEXT,
    budget_amount TEXT,
    actual_amount TEXT,
    forecast_amount TEXT,
    variance_amount TEXT,
    cost_status TEXT,
    invoice_reference TEXT,
    approved_by TEXT,
    cost_date TEXT,
    remarks TEXT

    )

    """)
# -------------------------------------
# DEPLOYMENT TRACKER
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS deployment_tracker (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    deployment_id TEXT,
    wave_name TEXT,
    deployment_task TEXT,
    environment_name TEXT,
    deployment_owner TEXT,
    planned_start TEXT,
    planned_end TEXT,
    actual_start TEXT,
    actual_end TEXT,
    deployment_status TEXT,
    dependency TEXT,
    rollback_plan TEXT,
    remarks TEXT

    )

    """)
# -------------------------------------
# HYPERCARE GOVERNANCE
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS hypercare_issues (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    incident_id TEXT,
    issue_type TEXT,
    severity TEXT,
    business_impact TEXT,
    reported_by TEXT,
    assigned_team TEXT,
    issue_status TEXT,
    reported_date TEXT,
    expected_resolution TEXT,
    actual_resolution TEXT,
    sla_status TEXT,
    remarks TEXT

    )

    """)

# -------------------------------------
# RAID LOG
# -------------------------------------

    execute_query("""

    CREATE TABLE IF NOT EXISTS raid_log (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        raid_type TEXT,
        title TEXT,
        description TEXT,
        owner TEXT,
        status TEXT,
        due_date TEXT

    )

    """)

    print("All tables created successfully")
# -------------------------------------
# USERS
# -------------------------------------

execute_query("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,
    password TEXT,
    role TEXT

)

""")