# hello.py

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hellow Word</h1>"


@app.route("/users")
def get_users():
    users = ["Maomao", "Alicia"]
    resp = ["<p>{}</p>".format(user) for user in users]
    resp = "\n".join(resp)

    return resp


@app.route("/user/<name>")
def get_user_name(name):
    return "<h1>Hello, {}!</h1>".format(name)


@app.route("/user/<int:uid>")
def get_user_id(uid):
    if isinstance(uid, int):
        return "<h1>Your ID: {}</h1>".format(uid)
    return "<h1>ID should be int</h1>"


@app.route("/user/<path:path>")
def get_user_path(path):
    return "<h1>Path: {}</h1>".format(path)


if __name__ == "__main__":
    app.run(port=5566)