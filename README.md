# 📚 AssignTrack — Web-Based Academic Assignment Tracking System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)
![jQuery](https://img.shields.io/badge/jQuery-3.7-blue?logo=jquery)

A full-stack web application that helps students manage academic assignments, track deadlines, and monitor progress — built as a college Full Stack Web Development project.

---

## 🌐 Live Demo

🔗 [https://assigntrack.onrender.com](https://assigntrack.onrender.com)

---

## 📸 Screenshots

> Dashboard View

![Dashboard](static/images/dashboard.png)

---

## ✨ Features

- ➕ Add assignment with title, subject, due date, priority and description
- ✏️ Edit any existing assignment
- 🗑️ Delete assignment with confirmation popup
- ✅ Mark assignment as completed or pending
- 🔴 Overdue detection — highlights past-due assignments in red
- 📊 Progress bar showing overall completion percentage
- 🔍 Live search by title or subject
- 🔽 Filter by All / Pending / Completed / Urgent (High priority)
- 💬 Flash messages for user feedback (success / error)
- ✅ Client-side validation using jQuery
- ✅ Server-side validation using Flask

---

## 🛠️ Technologies Used

| Layer | Technology |
|---|---|
| Frontend | HTML5, Bootstrap 5, Bootstrap Icons |
| Scripting | JavaScript, jQuery 3.7 |
| Backend | Python, Flask |
| Templating | Jinja2 |
| Database | SQLite (via Python sqlite3) |
| Deployment | Render |

---

## 📁 Project Structure
```
assigntrack/
├── app.py                  ← Flask backend — all routes and database logic
├── assignments.db          ← SQLite database (auto-created on first run)
├── requirements.txt        ← Python dependencies
├── Procfile                ← For Render deployment
├── README.md               ← Project documentation
├── static/
│   ├── css/
│   │   └── style.css       ← Minimal custom CSS
│   └── js/
│       └── script.js       ← jQuery: validation, filter, search, events
└── templates/
    ├── base.html           ← Master layout (navbar, flash messages, footer)
    ├── index.html          ← Dashboard: form + assignment table
    ├── edit.html           ← Edit assignment form
    └── success.html        ← Confirmation page after add/edit
```

---

## 🔗 Flask Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Home page — displays all assignments |
| `/submit` | POST | Add new assignment to database |
| `/success` | GET | Confirmation page after add/edit |
| `/edit/<id>` | GET | Show edit form for an assignment |
| `/update/<id>` | POST | Save updated assignment to database |
| `/toggle/<id>` | GET | Toggle status pending ↔ completed |
| `/delete/<id>` | GET | Delete assignment from database |

---

## 🗄️ Database Schema
```sql
CREATE TABLE assignments (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    subject     TEXT    NOT NULL,
    due_date    TEXT    NOT NULL,
    priority    TEXT    NOT NULL DEFAULT 'Medium',
    description TEXT,
    status      TEXT    NOT NULL DEFAULT 'pending',
    created_at  TEXT    NOT NULL
);
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Myladhanyasri/assigntrack.git
cd assigntrack
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

> ✅ The SQLite database `assignments.db` is created automatically on first run.

---

## 📊 How It Works (Workflow)
```
User fills form
      ↓
jQuery validates (client side)
      ↓
POST request → Flask /submit route
      ↓
Flask reads request.form + validates (server side)
      ↓
SQLite INSERT → saved to assignments.db
      ↓
Flash success message → redirect to success page
      ↓
User returns to dashboard
      ↓
Flask SELECT all assignments → Jinja2 renders updated table ✅
```

---

## 👤 Author

- **Name:** Myladha Nyasri
- **GitHub:** [@Myladhanyasri](https://github.com/Myladhanyasri)
- **Project:** Full Stack Web Development — College Project
- **Tech Stack:** HTML · CSS · Bootstrap · jQuery · Flask · SQLite

---

## 📄 License

This project is built for educational purposes as part of a college Full Stack Web Development course.
