# hello_email.py

import os

from flask import Flask
from flask_mail import Mail
#from flask.ext.mail import Mail
from flask_script import Manager

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config["DEBUG"] = True

mail = Mail(app)
manager = Manager(app)

if __name__ == "__main__":
    manager.run()