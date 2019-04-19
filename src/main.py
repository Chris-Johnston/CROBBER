from flask import Flask, send_from_directory, session, url_for, request, flash, redirect
from flask_oauth import OAuth
import os

app = Flask(__name__)

# https://discordapp.com/api/oauth2/authorize?client_id=568868246909091850&redirect_uri=localhost%3A5000&response_type=code&scope=identify

oauth = OAuth()
discord_remote = oauth.remote_app('Discord',
    base_url='https://discordapp.com/api/oauth2/',
    request_token_url='https://discordapp.com/api/oauth2/token',
    access_token_url='https://discordapp.com/api/oauth2/token',
    authorize_url='https://discordapp.com/api/oauth2/authorize',
    consumer_key=os.environ['DISCORD_KEY'],
    consumer_secret=os.environ['DISCORD_SECRET'])

@app.route('/')
@app.route('/index.html')
def landing():
    return send_from_directory('static', filename='landing.html')

@app.route('/oauth-authorized')
@discord_remote.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('/')
    if resp is None:
        flash('You denied the request to log in.')
        return redirect(next_url)
    session['discord_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['discord_user'] = resp['Username']

    flash(f'Signed in as ${session["discord_user"]}')
    return redirect(next_url)

@app.route('/login')
def login():
    return discord_remote.authorize(
        callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None)
    )

@discord_remote.tokengetter
def get_discord_token(token=None):
    return session.get('discord_token')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)