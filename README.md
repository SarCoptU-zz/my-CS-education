# my-CS-education

OSSU My CS Education plan

Web app for keeping track of my online courses based on OSSU curriculum (Open Source Society University, github repository here: https://github.com/ossu/computer-science)
Done in line with the CS50 web track model.
Using Flask Python framework, HTML, CSS, JS, Bootstrap and CS50 ide.

MCV – model, view, controller paradigm.

Model – a database in sqlite3 with the following columns
- id – primary key
- title – course title
- category – prerequisite / intro to cs / core cs / advanced cs
- duration – in weeks
- effort – hours / week
- started – date when the course was started
- ended – date then the course was finished

View – 3 pages using HTML/CSS/Bootstrap 
- one index page with the current status of courses completed or started
- similart page to index called edit that is used to delete courses that were inserted by mistake
- one page where all the info for the specific course is filled in by user

Controller – application.py program with all the functionality for the front/backend of the app
- no login required as all data will be kept in the database locally
- methods get and post for new course forms
NB: this is not a deployable app at the moment as it is only meant to teach me how to use the flask framework

