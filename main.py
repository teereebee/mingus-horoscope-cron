from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK !"

@app.route("/send-horoscope")
def send_horoscope():
    try:
        # Horoscope API GRATUITE (pas d'API key)
        response = requests.get("https://api.api-ninjas.com/v1/horoscope?sign=cancer")
        horoscope = response.json()[0]['horoscope']
        
        # Email via ton SMTP direct (PAS SendGrid)
        import smtplib
        from email.mime.text import MIMEText
        
        msg = MIMEText(f"🌙 Cancer: {horoscope}\n\nMingus Horoscope")
        msg['Subject'] = '🐕 Horoscope Cancer'
        msg['From'] = 'thierry@barbedette.com'
        msg['To'] = 'thierry@barbedette.com'
        
        server = smtplib.SMTP('mail.barbedette.com', 587)  # Change par ton serveur
        server.starttls()
        server.login('thierry@barbedette.com', 'TON_MDP_EMAIL')
        server.send_message(msg)
        server.quit()
        
        return "✅ CANCER ENVOYÉ ! (API + SMTP)"
    except Exception as e:
        return f"❌ {str(e)}"
