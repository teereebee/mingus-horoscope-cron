from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope OK ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    try:
        r = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        humain = r.json().get("cancer", "")
        
        chien = "🐕 ROAD TRIP ! Ton humain prépare voyage = gamelle + coussin ! 🚗"
        return f"<h1>{chien}</h1>"
    except:
        return "✅ Mingus prêt !"
