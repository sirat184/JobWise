from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            resume TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------- HOME ROUTE ----------
@app.route('/')
def index():
    return render_template('index.html')

# ---------- ADD APPLICATION ----------
@app.route('/add_application', methods=['POST'])
def add_application():
    data = request.get_json()
    company = data['company']
    role = data['role']
    status = data['status']
    resume = data['resume']

    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('INSERT INTO applications (company, role, status, resume) VALUES (?, ?, ?, ?)',
              (company, role, status, resume))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Application added successfully'})

# ---------- GET APPLICATIONS ----------
@app.route('/get_applications')
def get_applications():
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute('SELECT company, role, status, resume FROM applications')
    rows = c.fetchall()
    conn.close()

    applications = [{'company': row[0], 'role': row[1], 'status': row[2], 'resume': row[3]} for row in rows]
    return jsonify(applications)

# ---------- CUSTOMIZE RESUME ----------
@app.route('/customize_resume', methods=['POST'])
def customize_resume():
    data = request.get_json()
    role = data.get('role', '')
    resume = data.get('resume', '')

    # Simple placeholder logic (you can later connect OpenAI/OpenRouter API here)
    customized_resume = f"Customized for the role: {role}\n\n{resume}"

    return jsonify({'customized_resume': customized_resume})

# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True)



