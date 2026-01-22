import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st
# Load environment variables from .env
load_dotenv()

# Fetch variables
# DB_URL = os.getenv("DB_URL")
DB_URL = "postgresql://postgres.uzklqxaqtfigzorkirqx:WM5GYvAe91tN2GAJ@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"

# Connect to the database
try:
    connection = psycopg2.connect(
        DB_URL,
        connect_timeout=20
    )
    st.write("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT * FROM USERS;")
    result = cursor.fetchone()
    st.write("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    st.write("Connection closed.")

except Exception as e:
    st.write(f"Failed to connect: {e}")



# """
# Docstring for myapp.App
# """

# import os
# import sys

# CURRENT_FILE = os.path.abspath(__file__)
# SRC_PATH = os.path.dirname(os.path.dirname(CURRENT_FILE))

# if SRC_PATH not in sys.path:
#     sys.path.insert(0, SRC_PATH)

# import streamlit as st

# from myapp.common.container import Container
# from myapp.common.database.sqlite_db import SqliteDatabase
# from myapp.common.database.supabase_db import SupaBaseDatabase
# from myapp.common.database.supabase_db_v2 import SupaBaseDatabase_V2
# from myapp.common.state_manager import StateManager


# def main():
#     """
#     Docstring for main
#     """

#     if "Container" not in st.session_state:
#         # db: SqliteDatabase= SqliteDatabase()
#         # db: SupaBaseDatabase = SupaBaseDatabase()
#         db: SupaBaseDatabase_V2 = SupaBaseDatabase_V2()
#         container: Container = Container(db)
#         st.session_state.Container = container

#     auth_pages = [st.Page("_pages/home.py", title="Talksy")]

#     pages = [
#         st.Page("_pages/login.py", title="Login"),
#         st.Page("_pages/new_account.py", title="New Account"),
#     ]

#     if StateManager.get_user() is not None and StateManager.get_authenticated():
#         pg = st.navigation(auth_pages, position="top")
#     else:
#         pg = st.navigation(pages, position="top")

#     pg.run()

# if __name__ == "__main__":
#     main()
