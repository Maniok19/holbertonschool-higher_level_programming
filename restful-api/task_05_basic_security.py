#!/usr/bin/python3
""" This module demonstrates how to use the Flask library"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash
              ("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash
               ("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """ Verify username and password """
    if (username in users and
            check_password_hash(users[username]["password"], password)):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """ Protected route using Basic Auth """
    return jsonify(message="Basic Auth: Access Granted"), 200


@app.route('/login', methods=['POST'])
def login():
    """ Login route to generate JWT token """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if (username in users and
            check_password_hash(users[username]["password"], password)):
        identity = {"username": username, "role": users[username]["role"]}
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token), 200
    return jsonify(error="Invalid credentials"), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """ Protected route using JWT """
    return jsonify(message="JWT Auth: Access Granted"), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """ Admin-only route using JWT """
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return jsonify(message="Admin Access: Granted"), 200
    return jsonify(error="Admin access required"), 403


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    """ Callback for unauthorized access """
    return jsonify(error="Missing or invalid token"), 401


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    """ Callback for invalid token """
    return jsonify(error="Invalid token"), 401


@jwt.expired_token_loader
def expired_token_callback(callback):
    """ Callback for expired token """
    return jsonify(error="Token has expired"), 401


if __name__ == '__main__':
    app.run()
