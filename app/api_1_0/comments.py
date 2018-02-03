# app/api_1_0/comments.py

from . import api
from .decorators import permission_required
from ..models import Permission


@api.route('/comments/')
def get_comments():
    # TODO
    pass


@api.route('/comments/<int:id>')
def get_comment(id):
    # TODO
    pass


@api.route('/posts/<int:id>/comments/')
def get_post_comments(id):
    # TODO
    pass


@api.route('/posts/<int:id>/comments/', methods=['POST'])
@permission_required(Permission.COMMENT)
def new_post_comment(id):
    # TODO
    pass