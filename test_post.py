import requests

data = {
    "company": "Google",
    "role": "Software Engineer",
    "status": "Applied",
    "resume": "google_resume.pdf",
    "date_applied": "2025-07-20"
}

response = requests.post("http://127.0.0.1:5000/add_application", json=data)

print("Status Code:", response.status_code)
try:
    print("Response:", response.json())
except Exception as e:
    print("JSON Decode Error:", e)
    print("Raw Text:", response.text)

