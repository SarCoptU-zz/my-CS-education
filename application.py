from cs50 import SQL
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# database for courses taken / in progress
db = SQL("sqlite:///courses.db")

# route for all the courses taken / in progress page
@app.route("/", methods=["GET", "POST"])
def index():
    rows = db.execute("SELECT * FROM courses ORDER BY category ASC, started DESC;")
    for row in rows:
        id = row["id"]

    if request.method == "GET":
        return render_template("index.html", rows=rows)

    # insert current date in the finished column
    else:
        db.execute("UPDATE courses SET ended = strftime('%d/%m/%Y','now','localtime') WHERE id=:id;", id=request.form.get("new", "row['id'].value"))
        return redirect("/")

# route for adding a new course page
@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    else:
        # variables for request forms
        title = request.form.get("title")
        platform = request.form.get("platform")
        category = request.form.get("category")
        duration = request.form.get("duration")
        effort = request.form.get("effort")

        # insert course info into database
        db.execute("INSERT INTO courses (title, platform, category, duration, effort) VALUES (:title, :platform, :category, :duration, :effort);",
                    title=title, platform=platform, category=category, duration=duration, effort=effort)
        return redirect("/")

# page for deleting courses if not introduced correctly
@app.route("/edit", methods=["GET", "POST"])
def edit():
    rows = db.execute("SELECT * FROM courses ORDER BY category ASC, started DESC;")

    if request.method == "GET":
        return render_template("edit.html", rows=rows)

    # delete course
    else:
        db.execute("DELETE FROM courses WHERE id=:id;", id=request.form.get("delete", "row['id'].value")) # Need to look into this
        return redirect("/")