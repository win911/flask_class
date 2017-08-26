# hello.py

from flask import Flask
from flask import redirect
from flask import make_response, Response
from flask import abort


app = Flask(__name__)

'''
@app.route("/")
def index():
    return "<h1>Bad Request</h1>", 400
'''
'''
@app.route("/")
def index():
    return "<h1>Redirect</h1>", 302, {"Location": "http://www.google.com"}
'''

@app.route("/")
def index():
    return redirect("http://www.google.com")


@app.route("/no_cookie")
def no_cookie():
    response = make_response("<h1>This document doesn't carry a cookie!</h1>")
    return response

'''
@app.route("/has_cookie")
def has_cookie():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie("answer", "42")
    return response
'''

@app.route("/has_cookie")
def has_cookie():
    data = "<h1>This document carries a cookie!</h1>"
    headers = {}
    headers["Set-Cookie"] = "answer=45"
    return Response(data, headers=headers)


def load_user(uid):
    try:
        uid = int(uid)
        if uid == 1:
            return "Maomao"
        elif uid == 2:
            return "Alicia"
    except BaseException:
        return


@app.route("/user/<uid>")
def get_user(uid):
    user = load_user(uid)
    if not user:
        abort(400)
    else:
        return "<h1>Hello, {}!</h1>".format(user)


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
