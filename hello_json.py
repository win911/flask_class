# hello_json.py

import os

from flask import Flask, request
from jsonschema import validate, ValidationError


app = Flask(__name__)

schema = {
    "type": "object",
    "properties": {
    "title": {"type": "string", "maxLength": 50, "minLength": 10},
    "author": {"type": "string", "maxLength": 30, "minLength": 1}
    },
    "required": ["title", "author"]
}


@app.errorhandler(ValidationError)
def on_validation_error(e):
    return "error: {}".format(e)


@app.route("/books", methods=["POST"])
def create_book():
    if request.form:
        validate(request.form, schema)
        book_name = request.form["title"]
    elif request.json:
        validate(request.json, schema)
        book_name = request.json["title"]
    else:
        raise ValidationError("Invalid data format")
    return "[success] create book: {}".format(book_name)


if __name__ == "__main__":
    app.run()
