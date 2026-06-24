from sqlalchemy import create_engine, inspect

def print_all_tables(connection_string):
    try:
        # 1. Establish connection to the SQL database
        engine = create_engine(connection_string)
        
        # 2. Inspect the database structure
        inspector = inspect(engine)
        
        # 3. Retrieve and display table names
        tables = inspector.get_table_names()
        
        if not tables:
            print("Connection successful, but no tables were found in this database.")
            return

        print(f"--- Found {len(tables)} Tables ---")
        for table in tables:
            print(f" [Table] -> {table}")
            
    except Exception as e:
        print(f"An error occurred while connecting: {e}")

# ==========================================
# CONFIGURATION: Choose your database variant
# ==========================================

# Example 1: Local SQLite File
DATABASE_URL = "sqlite:///my_database.db"

# Example 2: PostgreSQL
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/my_database"

# Example 3: MySQL
# DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/my_database"

# Example 4: Microsoft SQL Server
# DATABASE_URL = "mssql+pyodbc://username:password@localhost/my_database?driver=ODBC+Driver+17+for+SQL+Server"

# Run the connector
if __name__ == "__main__":
    print_all_tables(DATABASE_URL)
