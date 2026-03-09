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
            from_email="thierry@barbedette.com",
            to_emails="thierry@barbedette.com",
            subject="🐕 Horoscope Cancer du jour",
            html_content="""
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <h1 style="color: #4a90e2;">🌙 Horoscope Cancer</h1>
                <p><strong>Aujourd'hui :</strong> Énergie lunaire favorable 🦀</p>
                <ul>
                    <li>Amour : ❤️‍🔥 Connexion profonde avec vos proches</li>
                    <li>Travail : 💼 Intuition payante, faites confiance à vos idées</li>
                    <li>Santé : 🌿 Équilibre parfait, prenez soin de vous</li>
                </ul>
                <hr style="border: 1px solid #eee;">
                <small style="color: #666;">Envoyé par Mingus Horoscope API</small>
            </div>
            """
        )
        
        response = sg.send(message)
        return f"✅ Email CANCER ENVOYÉ ! Status: {response.status_code}"
        
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
