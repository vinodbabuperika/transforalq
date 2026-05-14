CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(150),
    role VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projects (
    project_id SERIAL PRIMARY KEY,
    client_name VARCHAR(100),
    erp_platform VARCHAR(100),
    module_name VARCHAR(100),
    project_status VARCHAR(50),
    go_live_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raid_log (
    raid_id SERIAL PRIMARY KEY,
    project_id INT,
    raid_type VARCHAR(20),
    title VARCHAR(255),
    description TEXT,
    priority VARCHAR(20),
    owner_name VARCHAR(100),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raci_matrix (
    raci_id SERIAL PRIMARY KEY,
    project_id INT,
    activity_name VARCHAR(255),
    responsible VARCHAR(100),
    accountable VARCHAR(100),
    consulted VARCHAR(100),
    informed VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS fit_gap_analysis (
    fitgap_id SERIAL PRIMARY KEY,
    project_id INT,
    process_name VARCHAR(255),
    requirement_desc TEXT,
    fit_gap_status VARCHAR(50),
    solution_approach TEXT,
    owner_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS test_scripts (
    script_id SERIAL PRIMARY KEY,
    project_id INT,
    test_phase VARCHAR(20),
    script_name VARCHAR(255),
    tester_name VARCHAR(100),
    execution_status VARCHAR(50),
    defect_count INT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS defects (
    defect_id SERIAL PRIMARY KEY,
    project_id INT,
    defect_title VARCHAR(255),
    severity VARCHAR(50),
    status VARCHAR(50),
    assigned_to VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS deployment_tracker (
    deployment_id SERIAL PRIMARY KEY,
    project_id INT,
    deployment_phase VARCHAR(100),
    deployment_status VARCHAR(50),
    deployment_date DATE,
    owner_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS migration_tracker (
    migration_id SERIAL PRIMARY KEY,
    project_id INT,
    object_name VARCHAR(255),
    source_system VARCHAR(100),
    target_system VARCHAR(100),
    reconciliation_status VARCHAR(50),
    validation_status VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS uploaded_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INT,
    document_name VARCHAR(255),
    document_type VARCHAR(100),
    uploaded_by VARCHAR(100),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS raid_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raid_type TEXT,
    title TEXT,
    description TEXT,
    owner TEXT,
    priority TEXT,
    status TEXT,
    mitigation_plan TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);