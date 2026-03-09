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
        return "❌ SENDGRID_API_KEY manquante"
    if not api_key.startswith("SG."):
        return f"❌ Clé invalide: {api_key[:10]}"
    
    return f"✅ Clé SendGrid OK ! ({api_key[:15]}...) Prêt pour email !"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
