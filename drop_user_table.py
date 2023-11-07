import sqlite3
import os

# Set up the database connection
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///models.db')
db_path = DATABASE_URL.split("///")[-1]  # Extracts the path to the SQLite database

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL command to drop the user table if it exists
drop_table_command = "DROP TABLE IF EXISTS user"

# Execute the drop table command
try:
    cursor.execute(drop_table_command)
    conn.commit()
    print("User table dropped successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    # If the script is run directly, execute the function
    pass
