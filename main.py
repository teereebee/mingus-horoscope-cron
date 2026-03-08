from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🐕 Mingus Horoscope OK !"

@app.route('/send-horoscope')
def send_horoscope():
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        return "❌ Pas de clé SendGrid"
    return f"✅ Clé SendGrid OK ! ({api_key[:15]}...)"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
