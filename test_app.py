# Import the necessary modules
from unicodedata import name
from urllib import response
from flask import url_for
from flask_testing import TestCase
# import the app's classes and objects
from app import app, db, Team, Player 
# Create the base class
class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app
    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        # Create test team
        self.sample1 = Team(team_name="Arsenal")
        self.player1 = Player(name = "Dummy", team_id = self.sample1.id)
       
        # save users to database
        db.session.add
