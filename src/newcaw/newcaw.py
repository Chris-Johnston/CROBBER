"""
Add a new post to the crob feed.
New post needs to be validated to ensure it meets regex requirements.
Post will be saved as a raw text file because REEEEEEEEEEEEEEEE
"""

from flask import Blueprint, send_from_directory

newcaw = Blueprint('newcaw', __name__, url_prefix='/caw')

@newcaw.route('/', methods=['GET'])
def root():
    return send_from_directory('static', filename='newcaw.html')

def make_new_crob_post():
    """
    Display a page with an input field and a submit button.
    TODO: validate auth status for logged in user? Add username?
    """
    return "the method got called, hurrah"
