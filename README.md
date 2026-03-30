**AssignTrack - Web-Based Academic Assignment Tracking System**
A full-stack web application that helps students manage academic assignments, track deadlines, and monitor progress built as a 
college Full Stack Web Development project.
 Live Demo - https://assigntrack-o296.onrender.com/
 Dashboard View
 
 **✨ Features**
➕ Add assignment with title, subject, due date, priority and description
✏️ Edit any existing assignment
🗑️ Delete assignment with confirmation popup
✅ Mark assignment as completed or pending
🔴 Overdue detection — highlights past-due assignments in red
📊 Progress bar showing overall completion percentage
🔍 Live search by title or subject
🔽 Filter by All / Pending / Completed / Urgent (High priority)
💬 Flash messages for user feedback (success / error)
✅ Client-side validation using jQuery
✅ Server-side validation using Flask

**🛠️ Technologies Used**
LayerTechnologyFrontendHTML5, Bootstrap 5, Bootstrap IconsScriptingJavaScript, jQuery 3.7BackendPython, FlaskTemplatingJinja2DatabaseSQLite (via Python sqlite3)DeploymentRender
**📁 Project Structure**
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


**⚙️ Setup Instructions**
1. Clone the repository
bashgit clone https://github.com/Myladhanyasri/assigntrack.git
cd assigntrack
2. Install dependencies
bashpip install -r requirements.txt
3. Run the application
bash python app.py
4. Open in browser
http://127.0.0.1:5000

The SQLite database assignments.db is created automatically on first run.
