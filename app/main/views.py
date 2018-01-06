# app/main/views.py

from flask import render_template, abort
from flask_login import login_required

from . import main
from ..decorators import admin_required, permission_required
from ..models import Permission, User


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"


@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment moderators!"


@main.route('/user/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
