from flask import Flask
import bugsnag
from bugsnag.flask import handle_exceptions

# Configure Bugsnag
bugsnag.configure(
  api_key = "dfd1602d7e456c0611c7d88dc3a4d76b",
  project_root = "~/Hackathon_Project",
)

# Attach Bugsnag to Flask's exception handler
app = Flask(__name__)
handle_exceptions(app)

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()