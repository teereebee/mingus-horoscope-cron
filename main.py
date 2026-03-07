from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope V2 OK ! 🐕"
