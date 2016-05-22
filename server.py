"""GigAware Web App"""

app = Flask(__name__)

######################################################################

@app.route('/')
def landing_page():
    """Show landing page: About App.

        "You are 3 clicks away from getting a gig or posting a gig".
        Start button
        """


@app.route('login')
def login():
    """Login with facebook facebook oauth. Maybe hardcoded for the demo"""


@app.route('location')
def location():
    """Allow geolocation or grab geolocation from user input(address)"""


@app.route('usermode')
def usermode():
    """Select type of user. Form with checkbox input"""


@app.route('employer')
def task_setup():
    """Employer dashboard containing task form and pending tasks.

        NON PRIORITY. BUILDING REFUGEE UX 1ST

        Task form filled out by employer:
        Describe task. Taggs(possibly 2.0 or hardcoded)
        Sliding scale for the next 7 days,
        to specify days and times when task can be accomplished
        Checkboxes for food and pcik-up/drop-off availability
        Compensation is specified.

        From pending tasks can go to '/applicants' page that shows
        list of people applied for the task.
        """


@app.route('employee')
def employee():
    """Worker availability. Sliding scale for the next 7 days,

        to specify days and times when refugee is availabale to work.
        List of all tasks for which application is pending
        """


@app.route('search_results')
def availability():
    """List of matching jobs based on a query"""


@app.route("task/<int:task_id>")
def show_task_info(task_id):
    """Show information about task from search results list.
        Select button to apply for this gig"""


@app.route('applications')
def list_applications():
    """Show list of aplicants per task

        NON PRIORITY. BUILDING REFUGEE UX 1ST
        """


@app.route("employee/<int:employee_id>")
def show_applicant_info(employee_id):
    """Show information about applicant

        NON PRIORITY. BUILDING REFUGEE UX 1ST

        Select button that completes transaction.
        Uppon clicking it 1. record of transaction is committed to database.
        2. task is no longer listed as available 3. employee availability is updated
        4. task is no longer is pending for other job seekers if they applied for it.
        Integrate Twillio to start am SMS dialogue between employer/employee.
        """

######################################################################

if __name__ == "__main__":
    # debug=True , since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)





