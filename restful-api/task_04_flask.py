#!/usr/bin/python3
"""This module demonstrates how to use the Flask library to create"""
from flask import Flask
from flask import jsonify


app = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 35, "city": "New York"},
    "alice": {"name": "Alice", "age": 30, "city": "Chicago"}
}


@app.route("/")
def home():
    """ Home route """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """ Data route """
    use = list(users.keys())
    return jsonify(use)


@app.route("/status")
def status():
    """ Status route """
    return "OK"


@app.route("/user/<string:name>")
def user(name):
    """ User route"""
    if name in users:
        return jsonify(users[name])
    else:
        return jsonify({"error": "User not found"}), 404
