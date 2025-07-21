
import sqlite3
conn = sqlite3.connect("job_tracker.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    job_title TEXT NOT NULL,
    status TEXT NOT NULL,
    resume_version TEXT,
    date_applied TEXT
)
""")
conn.commit()
conn.close()
print(" Database and table created successfully.")
