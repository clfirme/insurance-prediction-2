import sys
path = '/mnt/data/insurance-prediction-2'  # Update the path to match the directory structure of your project on Render.com
if path not in sys.path:
    sys.path.append(path)
from app import app as application
