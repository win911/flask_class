# app/main/views.py

from flask import render_template
from flask_login import login_required

from . import main
from ..decorators import admin_required, permission_required
from ..models import Permission


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