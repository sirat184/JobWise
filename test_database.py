
import sqlite3

# Connect to the existing database
conn = sqlite3.connect("job_tracker.db")
cursor = conn.cursor()

# Insert sample job application
cursor.execute("""
INSERT INTO applications (company_name, job_title, status, resume_version, date_applied)
VALUES (?, ?, ?, ?, ?)
""", (
    "Google",               # Company Name
    "Software Engineer",    # Job Title
    "Applied",              # Status
    "resume_v1.pdf",        # Resume Version
    "2025-07-20"            # Date Applied (YYYY-MM-DD)
))

# Commit the insert
conn.commit()

# Fetch and print all rows from the table
cursor.execute("SELECT * FROM applications")
rows = cursor.fetchall()

print(" Current Applications in Database:")
for row in rows:
    print(row)

# Close the connection
conn.close()
