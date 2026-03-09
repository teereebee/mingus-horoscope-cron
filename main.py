from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK"

@app.route("/send-horoscope")
def send_horoscope():
    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        
        message = Mail(
            from_email="test@example.com",  # Email test ultra-simple
            to_emails="thierry@barbedette.com",
            subject="🐕 Test SendGrid FINAL",
            html_content="<h1>✅ SendGrid marche !</h1><p>Horoscope Cancer bientôt !</p>"
        )
        
        response = sg.send(message)
        return f"✅ EMAIL ENVOYÉ ! Status: {response.status_code} 🐕💌"
        
    except Exception as e:
        return f"❌ Erreur précise : {str(e)}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default = 10000
    app.run(host="0.0.0.0", port=port, debug=False)
