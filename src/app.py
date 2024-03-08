import pyrebase
import os
from flask import *
from twilio.twiml.voice_response import VoiceResponse

firebaseConfig = {
  "apiKey": "AIzaSyDr-f9ceqauHNdY2TxqbPZLuTvutn-MEIU",
  "authDomain": "scamzero-2a961.firebaseapp.com",
  "projectId": "scamzero-2a961",
  "storageBucket": "scamzero-2a961.appspot.com",
  "messagingSenderId": "638983487547",
  "appId": "1:638983487547:web:7cf8a36f9ca4287b1a9c1e",
  "measurementId": "G-8XJNJQP27N",
  "databaseURL": "https://scamzero-2a961-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


app = Flask(__name__)

@app.route('/call', methods=["POST"])
def call():
    resp = VoiceResponse()

    audio = "Hello, please state your name and purpose."
    resp.say(audio, voice='male')
    resp.record()
    resp.hangup()

    return str(resp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="66.42.94.26", port=5000)