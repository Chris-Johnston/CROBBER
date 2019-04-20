"""
Add a new post to the crob feed.
New post needs to be validated to ensure it meets regex requirements.
Post will be saved as a raw text file because REEEEEEEEEEEEEEEE
"""

from flask import Blueprint, send_from_directory
from flask import render_template
from flask import redirect
from flask import url_for
import time
newcaw = Blueprint('newcaw', __name__, url_prefix='/caw')

@newcaw.route('/', methods=['GET', 'POST'])
def root():
    return render_template('newcaw.html')

@newcaw.route('/caw/', methods=['GET', 'POST'])
def make_new_crob_post():
    """
    TODO: validate auth status for logged in user? Add username?
    TODO: string replacement
    """
    return redirect(url_for('landing'))
