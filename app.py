from flask import Flask, render_template, request
from bugsnag.flask import handle_exceptions
from flask.ext.sqlalchemy import SQLAlchemy
import os
import bugsnag
import requests
import sqlalchemy.exc
import sys
import pprint
# Configure Bugsnag
bugsnag.configure(
  api_key = "32358772e5093a3e1a58ceec6d4cfe78",
  project_root = "~/Radialpoint-Hackathon-Flask-App/Radialpoint-Hackathon-Flask-App",
)

# Attach Bugsnag to Flask's exception handler
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
handle_exceptions(app)

from models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    # initialize the errors variablie in an empty list, will be populated with errors, if any
    errors = []
    users_list = []
    if request.method == "POST":
        # get the user email
        first_name = request.form['FirstName'].strip()
        last_name = request.form['LastName'].strip()
        email = request.form['Email'].strip()

        # check that all fields are filled, if not raise an error
        if not first_name or not last_name or not email:
            errors.append("Please fill in all fields.")

        # try-catch adding the user-info to the database
        try:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            db.session.add(new_user)
            db.session.commit()
        except:
            bugsnag.notify(Exception("Unable to add item to database."))
            errors.append("Unable to add item to database.")
    try:
        users_list = db.session.query(User)
        pprint.pprint(users_list)
    except:
        # catch all errors thrown and notify bugsnag
        e = sys.exc_info()[0]
        bugsnag.notify(e)
    return render_template("index.html", errors=errors, users_list=users_list)

if __name__ == '__main__':
    app.run()