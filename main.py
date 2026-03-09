from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK"

@app.route("/send-horoscope")
def send_horoscope():
    api_key = os.environ.get("SENDGRID_API_KEY")
    if not api_key:
        return "❌ SENDGRID_API_KEY manquante dans Render"

    try:
        sg = SendGridAPIClient(api_key)
        message = Mail(
            from_email="test@sendgrid.net",      # expéditeur simple pour le test
            to_emails="thierry@barbedette.com",  # destinataire = toi
            subject="Test SendGrid depuis Render",
            html_content="<p>Si tu vois ce mail, SendGrid fonctionne ✅</p>",
        )
        response = sg.send(message)
        return f"✅ Email envoyé, status SendGrid = {response.status_code}"
    except Exception as e:
        return f"❌ Erreur SendGrid : {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", 
