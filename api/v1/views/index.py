#!/usr/bin/env python3
"""
Module for the stats endpoint of the API
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify

<<<<<<< HEAD

@app_views.route('/status', methods=['GET'])
def status():
    """Returns API status"""
=======
@app_views.route('/status', strict_slashes=False)
def get_status():
    """Return the status of the API"""
>>>>>>> c859d7ff32e8e393cf2d2aaa21fdf927ff03e5b8
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """Retrieve the stats of all objects"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
