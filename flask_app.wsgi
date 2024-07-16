# flask_app.wsgi

import sys
import os

# Insert the project directory to sys.path dynamically
project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Define the WSGI application object
from app import app as application  # Import your Flask app from app.py

