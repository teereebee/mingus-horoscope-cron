from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🐕 Mingus Horoscope OK"

@app.route("/send-horoscope")
def send_horoscope():
    api_key = os.environ.get("SENDGRID_API_KEY")
    
    # Test 1: Clé présente
    if not api_key:
        return "❌ Clé absente"
    
    # Test 2: Format correct
    if not api_key.startswith("SG."):
        return f"❌ Format invalide: {api_key[:10]}"
    
    # Test 3: SendGrid accepte la clé (SANS envoyer)
    try:
        from sendgrid import SendGridAPIClient
        sg = SendGridAPIClient(api_key)
        return f"✅ SendGrid OK ! Clé: {api_key[:15]}... Prêt pour email !"
    except Exception as e:
        return f"❌ SendGrid refuse: {str(e)}"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default = 10000
    app.run(host="0.0.0.0", port=port, debug=False)
