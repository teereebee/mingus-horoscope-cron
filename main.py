from flask import Flask
import requests
import os
from datetime import datetime
import pytz
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope Cron READY ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    """Teste l'horoscope MANUEL (ouvre cette URL)"""
    try:
        resp = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        data = resp.json()
        horoscope = data.get("cancer", "Horoscope indisponible")
        return f"✅ Horoscope Chien (Cancer) :<br><strong>{horoscope}</strong>"
    except Exception as e:
        return f"❌ Erreur API : {str(e)}"

@app.route("/send-horoscope")
def send_horoscope():
    """AUTOMATIQUE 7h tous les jours"""
    paris = pytz.timezone('Europe/Paris')
    now = datetime.now(paris)
    
    if now.hour != 7:
        return f"⏰ Pas 7h Paris (il est {now.hour}h)"
    
    try:
        # API horoscope
        resp = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        data = resp.json()
        horoscope = data.get("cancer", "Horoscope indisponible")
        
        # SendGrid
        sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        message = Mail(
            from_email='noreply@mingus.fr',
            to_emails='tes_abonnes@mingus.fr',  # ← CHANGE ICI
            subject=f'🐕 Horoscope Chien {now.strftime("%d/%m")}',
            html_content=f'''
            <h1>🌟 Horoscope Chien du {now.strftime("%d/%m")}</h1>
            <p><strong>{horoscope}</strong></p>
            <hr>
            <p>✨ Mingus Astrologie - Tous les jours à 7h</p>
            '''
        )
        sg.send(message)
        return "✅ EMAIL HOROSCOPE ENVOYÉ ! 🐕💌"
    except Exception as e:
        return f"❌ Erreur envoi : {str(e)}"
