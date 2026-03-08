from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "🐕 Mingus Horoscope Cron OK !"

@app.route('/test-horoscope')
def test_horoscope():
    return """
🐕 HOROSCOPE MINGUS - CANCER CANIN

🦴 SANTÉ  
Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith !

🐾 MON MAÎTRE  
Distraction olympique. Parfait pour squatter le canapé ninja !

💪 EFFORT  
Motivation 200% ! Courir, aboyer, vivre à fond !

🍖 GOURMANDISE  
Saucisse cosmique t'appelle. Yeux tristes 3min = steak gagné !

🐶 ASTUCE  
"Le regard triste ouvre 90% des gamelles"

✨ Mingus Astrologie - Chaque matin à 7h
"""

@app.route("/send-horoscope")
def send_horoscope():
    try:
        # Vérif clé API
        api_key = os.environ.get('SENDGRID_API_KEY')
        if not api_key:
            return "❌ SENDGRID_API_KEY manquante"
        if not api_key.startswith('SG.'):
            return f"❌ Clé invalide : {api_key[:10]}..."
        
        # Horoscope Cancer TEST
        horoscope = """
🐕 HOROSCOPE MINGUS - CANCER CANIN - 08/03

🦴 SANTÉ  
Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith ! 

🐾 MON MAÎTRE  
Distraction olympique cette semaine. Squatte le canapé en mode furtif !

💪 EFFORT  
Ardeur guerrière ! Courir, aboyer, conquérir le monde canin t'anime.

🍖 GOURMANDISE  
Saucisse cosmique t'appelle. 3min yeux suppliants = steak gagné !

🐶 ASTUCE CANINE  
"Le regard triste ouvre 90% des gamelles - arme fatale !"

✨ Mingus Astrologie - Chaque matin à 7h
"""
        
        # ENVOI EMAIL - thierry@barbedette.com expéditeur ET destinataire
        sg = SendGridAPIClient(api_key=api_key)
        message = Mail(
            from_email='test@sendgrid.net',
            to_emails='thierry@barbedette.com',
            subject='🐕 Horoscope Mingus TEST 08/03',
            html_content=horoscope
        )
        
        sg.send(message)
        return "✅ EMAIL HOROSCOPE ENVOYÉ ! 🐕💌 Vérifie thierry@barbedette.com"
        
    except Exception as e:
        return f"❌ Erreur : {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
