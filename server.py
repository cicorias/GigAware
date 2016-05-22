"""GigAware Web App"""

app = Flask(__name__)

######################################################################

@app.route('/')
def landing_page():
    """Show landing page: About App. 2 steps to sign up. Next button"""


@app.route('login')
def login():
    """Login with facebook facebook oauth. Maybe hardcoded for the demo"""

@app.route('location')
def location():
    """Allow geolocation or grab geolocation from user input(address)"""

@app.route('usermode')
def usermode():
    """Select type of user. Form with checkbox input"""

@app.route('task_setup')
def login():
    """Form filled out by employer.

        Describe task. Taggs(possibly 2.0 or hardcoded)
        Sliding scale for the next 7 days,
        to specify days and times when task can be accomplished
        Checkboxes for food and pcik-up/drop-off availability
        Compensation is specified.
        """
