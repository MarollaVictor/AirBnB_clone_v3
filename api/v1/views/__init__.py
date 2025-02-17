from flask import Blueprint

# Create the blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all routes from index.py (or other view files)
from api.v1.views.index import *from flask import Blueprint

# Create the blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all routes from index.py (or other view files)
from api.v1.views.index import *
