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
def task_setup():
    """Form filled out by employer.

        Describe task. Taggs(possibly 2.0 or hardcoded)
        Sliding scale for the next 7 days,
        to specify days and times when task can be accomplished
        Checkboxes for food and pcik-up/drop-off availability
        Compensation is specified.
        """

@app.route('availability')
def availability():
    """Worker availability. Sliding scale for the next 7 days,
        to specify days and times when refugee is availabale to work"""

@app.route('search_results')
def availability():
    """List of matching jobs based on a query"""

@app.route("task/<int:task_id>")
def show_task_info(task_id):
    """Show information about task from search results list.
        Select button to apply for this gig"""

        


