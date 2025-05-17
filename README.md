# 🏛️ TASC Portal – Architectural Governance System

A full-stack web portal built using **Django (backend)** and **Angular (frontend)** to manage and streamline architectural governance processes across software teams.

---

## 🚀 Overview

The TASC Portal enables teams to:

- Understand the architectural review process.
- Register their applications for governance evaluation.
- Submit evidence across 8 key architecture criteria (A1–A8).
- Save progress during submissions and return later.
- Read team testimonials and get in touch with the governance team.
- View Frequently Asked Questions (FAQs) to support the journey.

---

## 🧱 Tech Stack

| Layer      | Technology    |
|-----------|----------------|
| Backend    | Python, Django, Django REST Framework |
| Frontend   | Angular 17+, TypeScript |
| Database   | PostgreSQL / SQLite (local) |
| API Format | JSON (RESTful) |
| Dev Tools  | Git, VSCode, Postman, Angular CLI, pipenv/venv |

---

## 📁 Project Structure

tasc_portal/
├── manage.py
├── tasc_portal/ # Django settings
├── core/ # Django app (testimonials, team, forms)
├── frontend/ # Angular frontend app
│ ├── src/
│ ├── angular.json
│ └── dist/
├── .gitignore
├── README.md
└── requirements.txt



---

## 🛠️ Setup Instructions

### 🐍 Backend (Django)

1. **Create & activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate   # Windows: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations and run server:

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
⚡ Frontend (Angular)
Navigate to the frontend folder:

bash
Copy
Edit
cd frontend
Install dependencies:

bash
Copy
Edit
npm install
Run the Angular development server:

bash
Copy
Edit
ng serve
Access at: http://localhost:4200/
