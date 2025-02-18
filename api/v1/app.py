#!/usr/bin/python3
"""Flask Application"""
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import environ
import os
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors
    resp:
    404: resource not found

    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Application Function """
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True, debug=True)
