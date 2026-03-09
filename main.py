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
        
        sg

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
