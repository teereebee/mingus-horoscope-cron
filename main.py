from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🐕 Mingus OK !"

@app.route('/send-horoscope')
def send_horoscope():
    api_key = os.environ.get('SENDGRID_API_KEY')
    
    if not api_key:
        return "❌ Pas de clé SendGrid"
    if not api_key.startswith('SG.'):
        return f"❌ Clé invalide"
    
    return f"✅ Clé SendGrid OK ! Prêt pour horoscope !"

if __name__ == '__main__':
    app.run()
