from flask import Flask, send_from_directory, session, url_for, request, flash, redirect, render_template
import os
import sqlite3
from post import Post

app = Flask(__name__)
# totally secret
# security for this app is a joke
app.secret_key = 'CRAWWWW'

@app.route('/')
@app.route('/index.html')
def landing():
    if 'user_id' in session and session['user_id']:
        # logged in
        return render_template('homepage.html', user_id = session['user_id'])
    # not logged in
    return send_from_directory('static', filename='landing.html')

@app.route('/logout')
def logout():
    if 'user_id' in session:
        session['user_id'] = None
    return redirect('/')

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