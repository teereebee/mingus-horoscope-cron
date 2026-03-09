from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK !"

@app.route("/send-horoscope")
def send_horoscope():
    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail, FromEmail, ToEmail, ReplyTo
        
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        
        message = Mail(
            from_email=FromEmail('thierry@barbedette.com', 'Mingus'),
            to_emails=ToEmail('thierry@barbedette.com'),
            reply_to=ReplyTo('thierry@barbedette.com'),
            subject='🐕 Cancer du jour 🦀',
            plain_text_content='🌙 Cancer: Énergie lunaire favorable ! Amour ❤️ Travail 💼 Santé 🌿'
        )
        
        response = sg.send(message)
        return f"✅ CANCER ENVOYÉ ! Status: {response.status_code}"
        
    except Exception as e:
        return f"❌ {str(e)}"

