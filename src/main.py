from flask import Flask, send_from_directory, session, url_for, request, flash, redirect, render_template
from authlib.flask.client import OAuth
import os
import sqlite3
from post import Post

app = Flask(__name__)

# totally secret
# security for this app is a joke
# because this app is a joke
app.secret_key = 'CRAWWWW'


# app.register_blueprint(newcaw)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html')
def landing():
    if 'user_id' in session and session['user_id']:
        # logged in
        return render_template('homepage.html', user_id = session['user_id'],
            posts=[Post("CRAWWWW", "CAW CAW CAW"), Post("CRAWWWWW", "caw caw caw.")])
    # not logged in
    return send_from_directory('static', filename='landing.html')

@app.route('/crawwwwww')
@app.route('/logout')
def logout():
    if 'user_id' in session:
        session['user_id'] = None
    return redirect('/')

@app.route('/caw', methods=['POST'])
def caw():
    """
    new post, from form parameters

    message is from le_caw
    """
    if 'user_id' in session and session['user_id']:
        # logged in
        if 'le_caw' in request.form and request.form['le_caw']:
            user_id = session['user_id']
            message = request.form['le_caw']
            # TODO post this to the thing
            # TODO: actual functional logic to add the post to the database
    # not logged in, yell at them to log in
    return redirect('/')

@app.route('/craww', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    """
    Login route, accept a user and password,
    if successful, stores a logged in user id in the session
    """
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print('user', username, 'password', password)
    session['user_id'] = 1337
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
