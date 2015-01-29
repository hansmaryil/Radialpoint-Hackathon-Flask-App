from flask import Flask, render_template, request
from bugsnag.flask import handle_exceptions
from flask.ext.sqlalchemy import SQLAlchemy
import os
import bugsnag

# Configure Bugsnag
bugsnag.configure(
  api_key = "dfd1602d7e456c0611c7d88dc3a4d76b",
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
    return render_template('index.html')


if __name__ == '__main__':
    app.run()