# hello.py

from flask import Flask, request
#from flask import url_for


app = Flask(__name__)

statistic_data = {}


@app.before_request
def statistic():
    if request.path in ["/", "/statistic"]:    # request.path in [url_for("index"), url_for("get_statistic")]
        return

    statistic_data[request.path] = statistic_data.setdefault(request.path, 0) + 1


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    user_name = request.args.get("name")
    return "<p>Your browser is {}</p><p>Your name is {}</p>".format(user_agent, user_name)


@app.route("/statistic")
def get_statistic():
    return "statistic_data: {}".format(statistic_data)


@app.route("/buy/food")
def buy_food():
    return "<p>Here is your food.</p>"


@app.route("/buy/drink")
def buy_drink():
    return "<p>Here is your dirnk.</p>"


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
