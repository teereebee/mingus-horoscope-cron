from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK !"

@app.route("/send-horoscope")
def send_horoscope():
    api_key = os.environ.get("SENDGRID_API_KEY")
    
    if not api_key:
        return "❌ Pas de clé"
    if not api_key.startswith("SG."):
        return f"❌ Clé invalide: {api_key[:10]}"
    
    try:
        from sendgrid import SendGridAPIClient
        sg = SendGridAPIClient(api_key)
        return f"✅ SendGrid OK ! Clé: {api_key[:15]}... | Permissions OK"
    except Exception as e:
        return f"❌ Erreur précise: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
