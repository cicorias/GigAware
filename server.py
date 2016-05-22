"""GigAware Web App"""

app = Flask(__name__)

######################################################################

@app.route('/')
def landing_page():
    """Show landing page: About App. 2 steps to sign up. Next button"""

    