import sqlite3

# Connect to the database.
# If the file doesn't exist, SQLite creates it.
connection = sqlite3.connect("applications.db")

# Create a cursor to execute SQL commands.
cursor = connection.cursor()

# Create the applications table.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        job_title TEXT NOT NULL,
        application_date TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Applied',
        notes TEXT
    )
""")

# Save changes and close the connection.
connection.commit()
connection.close()

print("Database initialized successfully!")
