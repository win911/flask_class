# hello.py

from flask import Flask
from flask_script import Manager
#from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    return "<h1>Hello Word</h1>"


@manager.command
def hello():
    """Just say hello"""
    print("hello")


if __name__ == "__main__":
    manager.run()
