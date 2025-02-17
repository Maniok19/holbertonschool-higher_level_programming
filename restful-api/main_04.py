#!/usr/bin/python3
from flask import Flask
from task_04_flask import home, app, data, status, user


if __name__ == "__main__": app.run(debug=True)
