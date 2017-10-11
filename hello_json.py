# hello_json.py

import os

from flask import Flask, request
from flask_jsonschema import JsonSchema, ValidationError


app = Flask(__name__)
app.config["JSONSCHEMA_DIR"] = os.path.join(app.root_path, "schemas")

jsonschema = JsonSchema(app)


@app.errorhandler(ValidationError)
def on_validation_error(e):
    return "error: {}".format(e)


@app.route("/books", methods=["POST"])
@jsonschema.validate("books", "create")
#@jsonschema.validate("create_book")
def create_book():
    book_name = request.json["title"]
    return "[success] create book: {}".format(book_name)


if __name__ == "__main__":
    app.run()
