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
            from_email="authenticated@sendgrid.net",  # ← SendGrid sandbox officiel
            to_emails="thierry@barbedette.com",
            subject="🐕 Mingus Horoscope - Cancer Test",
            html_content="""
            <h1>🐕 CANCER CANIN - Mingus Horoscope</h1>
            <h3>🦴 SANTÉ :</h3><p>Éclat lunaire cosmique !</p>
            <h3>🍖 GOURMANDISE :</h3><p>Saucisse cosmique t'appelle !</p>
            <p><em>✨ Test réussi ! Mingus Astrologie</em></p>
            """
        )
        
        response = sg.send(message)
        return f"✅ HOROSCOPE ENVOYÉ SUCCESS ! Status: {response.status_code} 🐕💌"
        
    except Exception as e:
        return f"❌ ERREUR DÉTAILLÉE : {str(e)}"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default = 10000
    app.run(host="0.0.0.0", port=port, debug=False)
