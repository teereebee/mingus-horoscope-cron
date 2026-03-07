from flask import Flask
import requests

app = Flask(__name__)

def chien_horoscope(humain):
    humain = humain.lower()
    if "voyages" in humain:
        return "🚗 ROAD TRIP ! Gamelle + cousins obligatoires ! 🐾"
    elif "enfants" in humain:
        return "👶 Balle infinie avec les petiots ! 🎾"
    elif "travail" in humain:
        return "💼 ROI DU CANAPÉ toute la journée ! 🛋️"
    else:
        return "⭐ Dormir, manger, jouer = parfait ! 🐕"

@app.route("/")
def home():
    return "🚀 Mingus Horoscope READY ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    try:
        r = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        humain = r.json().get("cancer", "OK")
        chien = chien_horoscope(humain)
        return f"""
        <h2>🐕 Horoscope HUMAIN</h2>
        <p>{humain}</p>
        <h2>🐶 Horoscope MINGUS</h2>
        <p><strong>{chien}</strong></p>
        """
    except Exception as e:
        return f"Erreur : {str(e)}"
