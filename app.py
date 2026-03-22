from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "assigntrack_secret_2024"   # needed for flash messages

DB = "assignments.db"

# ─────────────────────────────────────────────
#  DATABASE HELPERS
# ─────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT    NOT NULL,
            subject     TEXT    NOT NULL,
            due_date    TEXT    NOT NULL,
            priority    TEXT    NOT NULL DEFAULT 'Medium',
            description TEXT,
            status      TEXT    NOT NULL DEFAULT 'pending',
            created_at  TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────
#  ROUTE 1 — Home Page  /
#  Displays all assignments in dashboard
# ─────────────────────────────────────────────

@app.route("/")
def index():
    conn  = get_db()
    rows  = conn.execute(
        "SELECT * FROM assignments ORDER BY due_date ASC"
    ).fetchall()

    # Stats for progress bar
    total     = len(rows)
    completed = sum(1 for r in rows if r["status"] == "completed")
    pending   = total - completed
    percent   = round((completed / total) * 100) if total else 0

    conn.close()
    return render_template("index.html",
        assignments = rows,
        total       = total,
        completed   = completed,
        pending     = pending,
        percent     = percent,
        now         = datetime.now().strftime("%Y-%m-%d")  # for overdue check in Jinja2
    )

# ─────────────────────────────────────────────
#  ROUTE 2 — Form Handling  /submit  (POST)
#  Adds a new assignment to DB
# ─────────────────────────────────────────────

@app.route("/submit", methods=["POST"])
def submit():
    title   = request.form.get("title",   "").strip()
    subject = request.form.get("subject", "").strip()
    due     = request.form.get("due_date", "")
    priority = request.form.get("priority", "Medium")
    desc    = request.form.get("description", "").strip()

    # Server-side validation
    errors = []
    if not title:   errors.append("Title is required.")
    if not subject: errors.append("Subject is required.")
    if not due:     errors.append("Due date is required.")

    if errors:
        for e in errors:
            flash(e, "danger")
        return redirect(url_for("index"))

    conn = get_db()
    conn.execute("""
        INSERT INTO assignments (title, subject, due_date, priority, description, status, created_at)
        VALUES (?, ?, ?, ?, ?, 'pending', ?)
    """, (title, subject, due, priority, desc, datetime.now().isoformat()))
    conn.commit()
    conn.close()

    flash(f'Assignment "{title}" added successfully!', "success")
    return redirect(url_for("success", action="added", name=title))

# ─────────────────────────────────────────────
#  ROUTE 3 — Success / Confirmation Page
# ─────────────────────────────────────────────

@app.route("/success")
def success():
    action = request.args.get("action", "done")
    name   = request.args.get("name", "")
    return render_template("success.html", action=action, name=name)

# ─────────────────────────────────────────────
#  ROUTE 4 — Toggle Status  /toggle/<id>
# ─────────────────────────────────────────────

@app.route("/toggle/<int:aid>")
def toggle(aid):
    conn = get_db()
    row  = conn.execute("SELECT status FROM assignments WHERE id=?", (aid,)).fetchone()
    if row:
        new_status = "completed" if row["status"] == "pending" else "pending"
        conn.execute("UPDATE assignments SET status=? WHERE id=?", (new_status, aid))
        conn.commit()
        flash(f'Assignment marked as {new_status}!',
              "success" if new_status == "completed" else "warning")
    conn.close()
    return redirect(url_for("index"))

# ─────────────────────────────────────────────
#  ROUTE 5 — Delete  /delete/<id>
# ─────────────────────────────────────────────

@app.route("/delete/<int:aid>")
def delete(aid):
    conn = get_db()
    row  = conn.execute("SELECT title FROM assignments WHERE id=?", (aid,)).fetchone()
    if row:
        conn.execute("DELETE FROM assignments WHERE id=?", (aid,))
        conn.commit()
        flash(f'Assignment "{row["title"]}" deleted.', "danger")
    conn.close()
    return redirect(url_for("index"))

# ─────────────────────────────────────────────
#  ROUTE 6 — Edit Form  /edit/<id>
# ─────────────────────────────────────────────

@app.route("/edit/<int:aid>")
def edit(aid):
    conn = get_db()
    row  = conn.execute("SELECT * FROM assignments WHERE id=?", (aid,)).fetchone()
    conn.close()
    if not row:
        flash("Assignment not found.", "danger")
        return redirect(url_for("index"))
    return render_template("edit.html", assignment=row)

# ─────────────────────────────────────────────
#  ROUTE 7 — Update  /update/<id>  (POST)
# ─────────────────────────────────────────────

@app.route("/update/<int:aid>", methods=["POST"])
def update(aid):
    title    = request.form.get("title",   "").strip()
    subject  = request.form.get("subject", "").strip()
    due      = request.form.get("due_date", "")
    priority = request.form.get("priority", "Medium")
    desc     = request.form.get("description", "").strip()

    errors = []
    if not title:   errors.append("Title is required.")
    if not subject: errors.append("Subject is required.")
    if not due:     errors.append("Due date is required.")

    if errors:
        for e in errors:
            flash(e, "danger")
        return redirect(url_for("edit", aid=aid))

    conn = get_db()
    conn.execute("""
        UPDATE assignments
        SET title=?, subject=?, due_date=?, priority=?, description=?
        WHERE id=?
    """, (title, subject, due, priority, desc, aid))
    conn.commit()
    conn.close()

    flash(f'Assignment "{title}" updated successfully!', "success")
    return redirect(url_for("success", action="updated", name=title))

# ─────────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    app.run(debug=True)