# hello.py

import os
from threading import Thread


from flask import Flask, render_template
from flask import session, redirect, url_for
from flask import flash
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
#from flask.ext.mail import Mail, Message
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"    # Important for CSRF token
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # do not write information here directly
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # do not write information here directly
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <your-email@example.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')   # do not write information here directly
app.config['DEBUG'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
mail = Mail(app)


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField("Submit")


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            send_email(to=app.config['FLASKY_ADMIN'], subject='New User',
                       template='mail/new_user', user=form.name.data)
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get("name"))


if __name__ == '__main__':
    manager.run()
