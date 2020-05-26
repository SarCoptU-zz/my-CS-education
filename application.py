from cs50 import SQL
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# database for courses taken / in progress
db = SQL("sqlite:///courses.db")

# route for all the courses taken / in progress page
@app.route("/", methods=["GET", "POST"])
def index():
    rows = db.execute("SELECT * FROM courses;")
    if request.method == "GET":
        return render_template("index.html", rows=rows)
    # TODO insert current time in the finished column
    #else:
        #db.execute("UPDATE time SET ended = strftime('%d/%m/%Y','now','localtime') WHERE id=':id';", id=row["id"]) needs some work here
        # not exactly sure if it's row["id"] or if I have to use request.form.get("id")

# route for adding a new course page
@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    else:
        # variables for request forms
        title = request.form.get("title")
        category = request.form.get("category") # radio input
        duration = request.form.get("duration")
        effort = request.form.get("effort")

        # TODO
        # I think I can just send an alert instead of a new page

        # error checks
        # THIS IS COMMENTED OUT CODE
        #if not title:
        #    return render_template("apology.html", message="You must provide a title for the course")
        #category =
        #if not category
        #if not duration
        #if not effort

        # insert course info into database - NEED TO CHANGE TAG TO CATEGORY - TABLE CHANGES LATER
        db.execute("INSERT INTO courses (title, category, duration, effort) VALUES (:title, :category, :duration, :effort);",
                    title=title, category=category, duration=duration, effort=effort)
        return redirect("/")

