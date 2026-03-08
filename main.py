from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope OK ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    chien = """
🐕 HOROSCOPE MINGUS - CANCER CANIN

🦴 SANTÉ : Ton poil brille ! Energie max mais attention flatulences suspectes → bois moins vite !

🐾 MON MAÎTRE : Distrait niveau champion du monde. Parfait pour squatter le canapé ninja !

💪 EFFORT : Motivation 200% ! Courir, aboyer, vivre ! Evite la tondeuse du voisin (mauvais karma).

🍖 GOURMANDISE : SAUCISSE VOLÉE confirmée ! Regarde ton humain 3min yeux tristes → il craque.

🐶 ASTUCE : "Ne jamais sous-estimer le pouvoir du regard triste" → 90% réussite !

✨ Mingus Astrologie - Tous les matins à 7h
"""
    return f"<pre style='font-family: Arial; max-width: 600px; margin: auto; white-space: pre-wrap;'>{chien}</pre>"
