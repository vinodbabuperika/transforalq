import sqlite3

conn = sqlite3.connect("transforaiq.db")

cursor = conn.cursor()

# ---------------------------------------------------
# PROJECT PLAN
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS project_plan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    phase TEXT,
    task TEXT,
    owner TEXT,
    status TEXT,
    due_date TEXT
)
""")

# ---------------------------------------------------
# RACI MATRIX
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS raci_matrix (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity TEXT,
    responsible TEXT,
    accountable TEXT,
    consulted TEXT,
    informed TEXT
)
""")

# ---------------------------------------------------
# STAKEHOLDER LOG
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS stakeholder_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stakeholder TEXT,
    role TEXT,
    influence TEXT,
    engagement_status TEXT
)
""")

# ---------------------------------------------------
# COST TRACKER
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS cost_tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    budget REAL,
    actual REAL,
    variance REAL
)
""")


# ---------------------------------------------------
# DEFECT TRACKER
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS defect_tracker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    defect_title TEXT,
    severity TEXT,
    owner TEXT,
    environment TEXT,
    defect_status TEXT,
    workstream TEXT,
    defect_date TEXT,
    root_cause TEXT,
    resolution TEXT
)
""")
# ---------------------------------------------------
# CLIENT MASTER
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS client_master (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    client_name TEXT,

    erp_system TEXT,

    workflow TEXT,

    project_manager TEXT,

    si_partner TEXT,

    deployment_type TEXT,

    status TEXT,

    go_live_readiness INTEGER,

    ocr_scope TEXT,

    exception_concierge_scope TEXT,

    approval_process_scope TEXT,

    po_threeway_match_scope TEXT,

    po_twoway_match_scope TEXT
)
""")
# ---------------------------------------------------
# RAID LOG
# ---------------------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS raid_log (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    client_name TEXT,

    title TEXT,

    raid_date TEXT,

    raised_by TEXT,

    raid_type TEXT,

    priority TEXT,

    status TEXT,

    owner TEXT,

    due_date TEXT,

    mitigation_plan TEXT,

    description TEXT
)
""")

conn.commit()

conn.close()

print("Database initialized successfully")