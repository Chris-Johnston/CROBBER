from flask import Flask, send_from_directory, session, url_for, request, flash, redirect
# from flask import register_blueprint
from authlib.flask.client import OAuth
from newcaw.newcaw import newcaw as newcaw
import os

app = Flask(__name__)
# consumer_key=os.environ['DISCORD_KEY']
# consumer_secret=os.environ['DISCORD_SECRET']

# https://discordapp.com/api/oauth2/authorize?client_id=568868246909091850&redirect_uri=localhost%3A5000&response_type=code&scope=identify

app.register_blueprint(newcaw)

@app.route('/')
@app.route('/index.html')
def landing():
    return send_from_directory('static', filename='landing.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
