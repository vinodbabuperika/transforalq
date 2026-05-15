from database.schema import create_tables

# =====================================================
# INITIALIZE DATABASE
# =====================================================

def initialize_database():

    create_tables()

# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    initialize_database()

    print("Database initialized successfully")