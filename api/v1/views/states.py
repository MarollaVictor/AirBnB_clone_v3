#!/usr/bin/python3
"""States API views"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all(State)
    return jsonify([state.to_dict() for state in states.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


<<<<<<< HEAD
@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
=======
@app_views.route('/states/<state_id>', methods=['DELETE'],
                strict_slashes=False)
>>>>>>> c859d7ff32e8e393cf2d2aaa21fdf927ff03e5b8
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    if not request.get_json():
        abort(400, description="Not a JSON")
<<<<<<< HEAD

    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")

=======
    
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    
>>>>>>> c859d7ff32e8e393cf2d2aaa21fdf927ff03e5b8
    state = State(**data)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
<<<<<<< HEAD

    if not request.get_json():
        abort(400, description="Not a JSON")

=======
    
    if not request.get_json():
        abort(400, description="Not a JSON")
    
>>>>>>> c859d7ff32e8e393cf2d2aaa21fdf927ff03e5b8
    data = request.get_json()
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
<<<<<<< HEAD

=======
    
>>>>>>> c859d7ff32e8e393cf2d2aaa21fdf927ff03e5b8
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
