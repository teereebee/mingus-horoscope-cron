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
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        
        # Message ULTRA minimal
        message = Mail(
            from_email="thierry@barbedette.com",
            to_emails=["thierry@barbedette.com"],
            subject="Test",
            plain_text_content="Si tu reçois ce mail, SendGrid marche !"
        )
        
        response = sg.send(message)
        return f"SUCCESS ! Status: {response.status_code}"
        
    except Exception as e:
        return f"ERREUR: {type(e).__name__}: {str(e)}"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default = 10000
    app.run(host="0.0.0.0", port=port, debug=False)
