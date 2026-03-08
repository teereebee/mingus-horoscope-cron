from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope OK ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    return """
🐕 HOROSCOPE MINGUS - CANCER CANIN

🦴 SANTÉ  
Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith, 
mais vigilance : flatulences suspectes signalées. Bois ta gamelle avec dignité.

🐾 MON MAÎTRE  
Distraction olympique cette semaine. L'occasion rêvée pour toi, noble squatteur,
de revendiquer le trône du canapé en mode furtif absolu.

💪 EFFORT  
Ardeur guerrière ! L'envie de courir, d'aboyer, de conquérir le monde canin t'anime. 
Sage conseil astral : la tondeuse voisine demeure un ennemi karmique.

🍖 GOURMANDISE  
La saucisse cosmique t'appelle. Technique infaillible : trois minutes d'yeux suppliants 
et ton humain capitule, le steak t'est acquis.

🐶 ASTUCE CANINE  
"Le regard triste, arme fatale du chenil, ouvre 90% des portes - gamelles, balades, câlins."

✨ Mingus Astrologie - Chaque matin à 7h, pour l'âme de ton chien
"""
