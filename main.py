from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope OK ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    chien = """
🐕 HOROSCOPE MINGUS - CANCER CANIN (littéraire + tes rubriques)

🦴 SANTÉ : Ton poil resplendit d'un éclat lunaire, énergie cosmique à son zénith. 
Mais vigilance : flatulences suspectes signalées - bois ta gamelle avec la dignité d'un seigneur.

🐾 MON MAÎTRE : Distraction olympique cette semaine. L'occasion rêvée pour toi, noble squatteur, 
de revendiquer le trône du canapé en mode furtif absolu.

💪 EFFORT : Ardeur guerrière ! L'envie de courir, d'aboyer, de conquérir le monde canin t'anime. 
Sage conseil astral : la tondeuse voisine demeure un ennemi karmique à éviter.

🍖 GOURMANDISE : La saucisse cosmique t'appelle. Technique infaillible : trois minutes d'yeux 
suppliants et ton humain capitule, le steak t'est acquis.

🐶 ASTUCE CANINE : "Le regard triste, arme fatale du chenil, ouvre 90% des portes 
- gamelles, balades, câlins. Un classique immuable de l'astrologie canine."

✨ Mingus Astrologie - Chaque matin à 7h, pour l'âme de ton chien
"""
    return f"""
<div style="font-family: Georgia, serif; max-width: 600px; margin: 20px auto; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <h1 style="color:
