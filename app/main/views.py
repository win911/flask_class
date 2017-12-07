# app/main/views.py

from flask import render_template, session, redirect, url_for, current_app
from flask_login import login_required, current_user

from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed! Current user: {}'.format(current_user.username)