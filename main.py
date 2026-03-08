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
        
        # HOROSCOPE MINGUS 100% CHIEN
        if "voyage" in humain.lower():
            chien = "🚗 <strong>ROAD TRIP ÉPIQUE !</strong> Ton humain charge la voiture = TOI en star du coffre ! 6h route + 50 pipi-stops + motel pourri. Mission : bave toutes les vitres ! 🐾"
        elif "enfant" in humain.lower():
            chien = "👶 <strong>JOURNÉE BALLE INFINIE !</strong> Les petiots = jackpot câlins ! Balle tennis x1000 + flaques boue. ⚠️ Ils oublieront ta gamelle → FAIS LE MORT = double ration ! 🎾"
        elif "travail" in humain.lower():
            chien = "💼 <strong>ROI DU CANAPÉ !</strong> Ton humain au bureau = TOI maître du domaine ! 14h sieste + Netflix. Bonus soir : il rentre HS = câlins x1000 ! 😍"
        else:
            chien = "⭐ <strong>PARFAIT VENDREDI CHIOT !</strong> Dormir 7h-12h, gamelle 12h, balle 13h-17h, dîner 18h, câlins 19h, ronflements 20h-7h. 100% bonheur ! 🐕🥩🎾"
        
        return f"""
        <div style="font-family: Arial; max-width: 600px; margin: auto;">
            <h1 style="color: #ff6b35;">🐕 HOROSCOPE MINGUS</h1>
            <div style="background: #f8f9fa; padding: 25px; border-radius: 15px;">
                <h2 style="color: #2d5a27; line-height: 1.5;">{chien}</h2>
                <p style="color: #666; font-size: 14px; margin-top: 20px;">
                    ✨ Mingus Astrologie - Tous les matins à 7h
                </p>
            </div>
        </div>
        """
    except:
        return "✅ Mingus prêt !"
