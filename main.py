from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK !"

@app.route("/send-horoscope")
def send_horoscope():
    # DEBUG 1: Clé
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        return "❌ ENV SENDGRID_API_KEY VIDE"
    if not api_key.startswith('SG.'):
        return f"❌ CLÉ INVAILDE: {api_key[:10]}"
    
    # DEBUG 2: Import + Init
    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        sg = SendGridAPIClient(api_key)
        return f"✅ SENDGRID INIT OK (clé: {api_key[:15]}...)"
    except Exception as e:
        return f"❌ SENDGRID INIT: {str(e)}"
    
    # DEBUG 3: Email (ne passe JAMAIS ici si init OK)
    message = Mail(
        from_email='thierry@barbedette.com',
        to_emails='thierry@barbedette.com',
        subject='🐕 Cancer TEST',
        html_content='<h1>🦀 CANCER !</h1>'
    )
    
    response = sg.send(message)
    return f"✅ {response.status_code}"
