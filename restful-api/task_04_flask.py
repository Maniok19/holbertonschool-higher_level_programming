#!/usr/bin/python3
"""This module demonstrates how to use the Flask library to create"""
from flask import Flask
from flask import jsonify
from requests import request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """ Home route """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """ Data route """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """ Status route """
    return "OK"


@app.route("/users/<username>")
def get_users(username):
    """Get user by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def post_register():
    """Add user"""
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        name = data.get("name")
        age = data.get("age")
        city = data.get("city")

        if not username:
            return jsonify({"error": "Username is required"}), 400

        users[username] = {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }
        return jsonify({"message": "User added",
                        "user": users[username]
                        }), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run()
