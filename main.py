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
        from sendgrid.helpers.mail import Mail
        
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        
        message = Mail(
            from_email="noreply@mingus.fr",
            to_emails="test@mingus.fr",  # Ton email
            subject="🐕 Horoscope Cancer du jour",
            html_content="""
            <h1>🌙 Horoscope Cancer</h1>
            <p><strong>Aujourd'hui :</strong> Énergie lunaire favorable 🦀</p>
            <p>Amour : ❤️‍🔥 Connexion profonde<br>
            Travail : 💼 Intuition payante<br>
            Santé : 🌿 Équilibre parfait</p>
            <hr>
            <small>Envoyé par Mingus Horoscope API</small>
            """
        )
        
        response = sg.send(message)
        return f"✅ Email ENVOYÉ ! Status: {response.status_code}"
        
    except Exception as e:
        return f"❌ Erreur: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
