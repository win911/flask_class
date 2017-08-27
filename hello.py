# hello.py

from flask import Flask, render_template


app = Flask(__name__)
registered_users = ["maomao", "alicia"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    if name not in registered_users:
        name = None
    return render_template("user.html", name=name)


@app.route("/users")
def users():
    return render_template("users.html", users=registered_users)


if __name__ == "__main__":
    app.run(debug=True)
