from flask import Flask
import requests
import os
from datetime import datetime
import pytz
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

def chien_horoscope(humain):
    """Transforme horoscope humain → CHIEN"""
    humain = humain.lower()
    if "voyages" in humain:
        return "🚗 Ton humain prépare un GRAND VOYAGE ! Gamelle prête ! 🐾"
    elif "enfants" in humain or "famille" in humain:
        return "👶 Les petits humains jouent avec toi TOUTE LA JOURNÉE ! 🎾"
    elif "travail" in humain or "carrière" in humain:
        return "💼 Ton humain rentre TÔT → SOIRÉE CÂLINS garantie ! 🛋️"
    elif "amour" in humain or "couple" in humain:
        return "💕 DOUBLE ration de caresses aujourd'hui ! Ton humain amoureux ! 😍"
    elif "argent" in humain:
        return "💰 CROQUETTES PREMIUM ce soir ! Ton humain payé ! 🥩"
    else:
        return "⭐ Journée PARFAITE : dormir, manger, jouer ! 🐕💤🎾"

@app.route("/")
def home():
    return "🚀 Mingus Horoscope Cron READY ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    try:
        resp = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        data = resp.json()
        horo_humain = data.get("cancer", "Horoscope indisponible")
        horo_chien = chien_horoscope(horo_humain)
        
        return f"""
        <h2>🐕 Horoscope HUMAIN (Cancer)</h2>
        <p><em>{horo_humain}</em></p>
        <hr>
        <h2>🐶 Horoscope CHIEN Mingus</h2>
        <p><strong>{horo_chien}</strong></p>
        """
    except Exception as e:
        return f"❌ Erreur : {str(e)}"

@app.route("/send-horoscope")
def send_horoscope():
    paris = pytz.timezone('Europe/Paris')
    now = datetime.now(paris)
    
    if now.hour != 7:
        return f"⏰ Pas 7h (il est {now.hour}h)"
    
    try:
        resp = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        data = resp.json()
        horo_humain = data.get("cancer", "Horoscope indisponible")
        horo_chien = chien_horoscope(horo_humain)
        
        sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        message = Mail(
            from_email='noreply@mingus.fr',
            to_emails='tes_abonnes@mingus.fr',
            subject=f'🐕 Horoscope Chien {now.strftime("%d/%m")}',
            html_content=f'''
            <h1>🌟 Horoscope Chien Mingus {now.strftime("%d/%m")}</h1>
            <p><strong>{horo_chien}</strong></p>
            <hr>
            <small>Mingus Astrologie - Tous les jours à 7h</small>
            '''
        )
        sg.send(message)
        return "✅ EMAIL CHIEN ENVOYÉ ! 🐕💌"
    except Exception as e:
        return f"❌ Erreur : {str(e)}"
