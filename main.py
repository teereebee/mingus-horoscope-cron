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
        
        # Horoscope du jour (TEST Cancer)
        horoscope = """
🐕 HOROSCOPE MINGUS - CANCER CANIN - 08/03

🦴 SANTÉ  
Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith, 
mais vigilance : flatulences suspectes signalées.

🐾 MON MAÎTRE  
Distraction olympique cette semaine. L'occasion rêvée pour squatter 
le canapé en mode furtif absolu.

💪 EFFORT  
Ardeur guerrière ! L'envie de courir, d'aboyer, de conquérir le monde canin.

🍖 GOURMANDISE  
La saucisse cosmique t'appelle. Technique : 3min yeux suppliants = steak gagné !

🐶 ASTUCE CANINE  
"Le regard triste, arme fatale du chenil, ouvre 90% des portes"

✨ Mingus Astrologie - Chaque matin à 7h
"""
        
        # Envoi email
        sg = SendGridAPIClient(api_key=api_key)
        message = Mail(
            from_email='noreply@mingus.fr',
            to_emails='TON_EMAIL@gmail.com',  # ← CHANGE ICI TON EMAIL !
            subject='🐕 Horoscope Mingus 08/03',
            html_content=horoscope
        )
        
        sg.send(message)
        return "✅ EMAIL HOROSCOPE ENVOYÉ ! 🐕💌"
        
    except Exception as e:
        return f"❌ Erreur : {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
