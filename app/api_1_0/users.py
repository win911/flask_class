# app/api_1_0/users.py

from . import api


@api.route('/users/<int:id>')
def get_user(id):
    # TODO
    pass


@api.route('/users/<int:id>/posts/')
def get_user_posts(id):
    # TODO
    pass


@api.route('/users/<int:id>/timeline/')
def get_user_followed_posts(id):
    # TODO
    pass