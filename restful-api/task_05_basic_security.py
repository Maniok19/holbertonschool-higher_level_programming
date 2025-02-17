#!/usr/bin/python3
""" This module demonstrates how to use the Flask library"""

from flask import Flask
from flask import jsonify
from flask import request

from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

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
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """ Protected route using Basic Auth """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login route"""
    if not request.is_json:
        return jsonify(), 400

    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if not username or not password:
        return jsonify(), 400

    user = users.get(username, None)
    if not user or not check_password_hash(user["password"], password):
        return jsonify(), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """ Protected route using JWT """
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """ Route accessible to admin only """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
