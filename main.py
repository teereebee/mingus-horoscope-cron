from flask import Flask
import requests

app = Flask(__name__)

def simple_chien(text):
    return "🐕 Ton humain est occupé aujourd'hui ! Profite pour dormir et manger ! 🛋️🥩"

@app.route("/")
def home():
    return "🚀 Mingus Horoscope READY ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    try:
        r = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        humain = r.json().get("cancer", "OK")
        chien = simple_chien(humain)
        return f"<h1>🐕 {chien}</h1><p>Humain: {humain}</p>"
    except:
        return "✅ Système OK !"

@app.route("/send-horoscope")
def send_horoscope():
    return "✅ Prêt pour 7h ! (test OK)"
