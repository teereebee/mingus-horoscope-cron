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
        
        horoscope = """
        <h1>🐕 HOROSCOPE MINGUS - CANCER CANIN</h1>
        <div style="font-family: Arial; max-width: 600px;">
            <h2>🦴 SANTÉ</h2>
            <p>Ton poil resplendît d'un éclat lunaire. Énergie cosmique à son zénith !</p>
            
            <h2>🐾 MON MAÎTRE</h2>
            <p>Distraction olympique cette semaine. Squatte le canapé en mode ninja !</p>
            
            <h2>🍖 GOURMANDISE</h2>
            <p>La saucisse cosmique t'appelle. Technique : 3min d'yeux suppliants = steak gagné !</p>
            
            <h2>🐶 ASTUCE CANINE</h2>
            <p>"Le regard triste ouvre 90% des gamelles"</p>
            
            <hr>
            <p><em>✨ Mingus Astrologie - Chaque matin à 7h</em></p>
        </div>
        """
        
        message = Mail(
            from_email="noreply@mingus.fr",
            to_emails="thierry@barbedette.com",
            subject="🐕 Horoscope Mingus - Cancer Canin",
            html_content=horoscope
        )
        
        response = sg.send(message)
        return f"✅ HOROSCOPE CANCER ENVOYÉ ! Status: {response.status_code} 🐕💌"
        
    except Exception as e:
        return f"❌ Erreur : {str(e)}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default = 10000
    app.run(host="0.0.0.0", port=port, debug=False)
