# hello.py

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

'''
@app.route("/test")
def test():
    mydict = {"key": "This is a secret"}
    mylist = [1, 2, 3, 4]
    myintvar = 0

    class Myobj():
        def method1(self):
            return "I'm a instance method."

        @staticmethod
        def method2():
            return "I'm a static method."

        @classmethod
        def method3(cls, value):
            return "I'm a class method, get value {}".format(value)

    context = {
        "mydict": mydict,
        "mylist": mylist,
        "myintvar": myintvar,
        "instance": Myobj(),
        "class": Myobj
    }

    return render_template("test.html", **context)
'''

@app.route("/test")
def test():
    code = "<h1>Hello</h1>"
    return render_template("test.html", code=code)


@app.route("/vulnerable")
def vulnerable():
    code = """<script>alert("I'm a hacker.")</script>"""
    return render_template("test.html", code=code)


if __name__ == "__main__":
    app.run(debug=True)
