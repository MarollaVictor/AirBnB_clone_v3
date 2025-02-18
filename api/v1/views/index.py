#!/usr/bin/env python3
"""
Module for the stats endpoint of the API
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def get_status():
    """Return the status of the API"""
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
