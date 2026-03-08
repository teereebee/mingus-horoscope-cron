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
@app.route("/send-horoscope")
def send_horoscope():
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    
    # TES rubriques horoscope
    horoscope = """
🐕 HOROSCOPE MINGUS - CANCER CANIN

🦴 SANTÉ  
Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith. 

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
    
    sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    message = Mail(
        from_email='noreply@mingus.fr',
        to_emails='TON_EMAIL@gmail.com',  # ← METS TON EMAIL ICI
        subject='🐕 Horoscope Mingus 08/03',
        html_content=horoscope
    )
    
    sg.send(message)
    return "✅ EMAIL ENVOYÉ ! 🐕💌"
