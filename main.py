from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🐕 Mingus Horoscope OK !"

@app.route('/send-horoscope')
@app.route('/send-horoscope')
def send_horoscope():
    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        import os
        
        api_key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(api_key=api_key)
        
        horoscope = """
🐕 HOROSCOPE MINGUS - CANCER CANIN - 08/03

🦴 SANTÉ  
Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith !

🐾 MON MAÎTRE  
Distraction olympique cette semaine. Squatte le canapé ninja style !

💪 EFFORT  
Ardeur guerrière ! Courir, aboyer, conquérir le monde canin !

🍖 GOURMANDISE  
Saucisse cosmique t'appelle. Yeux tristes 3min = steak gagné !

🐶 ASTUCE  
"Regard triste = 90% des gamelles ouvertes !"

✨ Mingus Astrologie - Chaque matin 7h
"""
        
        message = Mail(
            from_email='test@sendgrid.net',
            to_emails='thierry@barbedette.com',
            subject='🐕 Horoscope Mingus TEST',
            html_content=horoscope
        )
        
        sg.send(message)
        return "✅ EMAIL HOROSCOPE CANCER ENVOYÉ ! Vérifie ta boîte mail 🐕💌"
        
    except Exception as e:
        return f"❌ Erreur : {str(e)}"
