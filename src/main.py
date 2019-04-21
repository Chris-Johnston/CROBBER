from flask import Flask, send_from_directory, session, url_for, request, flash, redirect, render_template, g
import os
import sqlite3
from post import Post, translate_message
import hashlib
import time

app = Flask(__name__)

images = ['angry-crob', 'crob-viking', 'crob', 'goatee-crob', 'interest-crob', 'thunder-crob', 'void-crob']

# totally secret
# security for this app is a joke
# because this app is a joke
app.secret_key = 'CRAWWWW'
DATABASE = 'craw.db'

# http://flask.pocoo.org/docs/1.0/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # init the database if not exists
        init_db(db)
    return db

def init_db(db):
    """
    Creates db tables if not already set up
    """
    cur = db.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT)
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS posts
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT,
        content TEXT,
        posted INTEGER,
        fries INTEGER)
    ''')
    # crows love fries, fries are the points

def get_posts():
    with app.app_context():
        print('getting posts')
        cur = get_db().cursor()
        cur.execute("SELECT * FROM posts ORDER BY posted DESC LIMIT 50")
        posts = []
        for row in cur.fetchall():
            print(row)
            p = Post(row[0], row[1], row[2], row[4])
            username = row[1]
            user_hash = int(hashlib.sha1(username.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
            image = images[user_hash % len(images)]
            p.img = image
            posts.append(p)
        return posts
    return None
        

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# app.register_blueprint(newcaw)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html')
def landing():
    posts = get_posts()
    print(len(posts))
    if 'user_id' in session and session['user_id']:
        # logged in
        return render_template('homepage.html', user_id = session['user_id'],
            posts=posts,
            username=session['username'])
    # not logged in
    return send_from_directory('static', filename='landing.html')

@app.route('/crawwwwww')
@app.route('/logout')
def logout():
    if 'user_id' in session:
        session['user_id'] = None
    return redirect('/')

def post_messge(author: str, message: str):
    """
    submits a post
    """
    with app.app_context():
        db = get_db()
        cur = db.cursor()
        message = translate_message(message)
        cur.execute('''INSERT INTO posts (content, posted, fries, author) VALUES (?, ?, ?, ?);''', (message, time.time(), 1, author))
        print(f'inserting message {message} from user {author}')
        db.commit()

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
            username = session['username']
            message = request.form['le_caw']
            post_messge(username, message)
    # not logged in, yell at them to log in
    return redirect('/')

@app.route('/give_fry', methods=['POST'])
def fries_for_crobs():
    post_id = ''
    if 'user_id' in session and session['user_id']:
        # logged in
        if 'postiboi' in request.form and request.form['postiboi']:
            post_id = request.form.get('postiboi')
            fries = request.form.get('frybois')
            print("post id is " + str(post_id))
            print(type(post_id))
            print("current fry count is " + str(fries))
            print(type(fries))
            with app.app_context():
                db = get_db()
                cur = db.cursor()
                cur.execute('''UPDATE posts SET fries = ? WHERE id = ?''', (str(int(fries) + 1), post_id))
                db.commit()
    return redirect('/')

def get_user_id(username: str, password: str) -> int:
    """
    gets the user id for the user, registers them if not
    if wrong, returns None
    """
    with app.app_context():
        db = get_db()
        cur = db.cursor()
        hash_pw = hashlib.sha256(password.encode('utf-8'))
        hash_str = hash_pw.hexdigest()
        # print(hash_str)
        cur.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, hash_str,))
        result = cur.fetchone()
        # print(result)
        if result is None:
            print(f'inserting user {username}')
            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_str,))
            db.commit()
            return cur.lastrowid
        else:
            return result[0]
    return None

@app.route('/craww', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    """
    Login route, accept a user and password,
    if successful, stores a logged in user id in the session
    """
    session['user_id'] = None
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # print('user', username, 'password', password)
        id = get_user_id(username, password)
        print('got id', id)
        if id:
            session['user_id'] = id
            session['username'] = username
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
