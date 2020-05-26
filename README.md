# my-CS-education

OSSU My CS Education plan

Web app for keeping track of my online courses based on OSSU curriculum (Open Source Society University, github repository here: https://github.com/ossu/computer-science)
App done in line with the CS50 web track model.
Using Flask Python framework, HTML, CSS, JS, Bootstrap maybe and CS50 ide.

MCV – model, view, controller paradigm.

Model – a db in sqlite3 with the following columns
- id – integer, primary key, autoincrement, not null
- tag (eg: prerequisite, coreCS, advancedCS) -  varchar(255)
- duration (in weeks) – integer?
- effort (hours/week) – integer?
- started (date started) – should be datestamp, eventually autofilled based on os time when data row first inserted into the table ('started' TIMESTAMP DATE DEFAULT (datetime ('now', '+1 hour', 'localtime') – this is from my 'history' table from finance
- ended (date ended) – datestamp when completed button pressed by user, similar to 'started' above only it will be stamped when user presses completed button, I need to change ended's default because now both started and ended are just filled in at the same time

View – 2 pages 
- one index page with the current status of courses completed or started
- one page where all the info for the specific course is filled in by user – probably form will be kinda big: need to input course title, tag, effort, started should be filled automatically, ended by user when button in the index page pushed

Controller – application.py program with all the functionality for the front/backend of the app
- no login required as all data will be kept in the db locally
- methods get and post for new course forms, only get for the index page

Courses table:
CREATE TABLE IF NOT EXISTS 'courses' (
  'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  'title' VARCHAR(255),
  'category' VARCHAR(255),
  'duration' INTEGER,
  'effort' INTEGER,
  'started' DATE DEFAULT (strftime ('%d/%m/%Y', 'now', 'localtime')), 
  'ended' – DATE DEFAULT (strftime ('%d/%m/%Y', 'now', 'localtime'))
);

Issues:
- add get/post if/else statements to app.py for /new route – error checks
- learn to send alerts instead of sending user to new page - ?JS
- 'ended' column, I can add it when table created, but fill it in once I press on the respective incomplete button = ?submit button – which will send a ?post to somewhere? - instead of <a>
- is there any value to add NOT NULL to title/category/duration/effort? Will that help with the error  check in app.py??
- work on looks of the page after all the functionality is sorted

  
