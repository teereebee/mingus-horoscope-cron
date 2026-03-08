from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope OK ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    # HOROSCOPE MINGUS = TON STYLE (copie-colle et MODIFIE)
    chien = """
    🐕 <strong>OPÉRATION GAMELLE MYSTÈRE</strong> 🧩
    
    Ton humain fixe le frigo comme s'il contenait la réponse à la vie.
    Ce soir : il teste une recette TikTok démente = <strong>TOI = dégustateur officiel !</strong>
    
    Verdict probable : 70% chance pâtée bizarre, 25% chance jackpot steak haché,
    5% chance il pleure et te donne tout son assiette.
    
    <strong>TA MISSION : yeux suppliants + queue frénétique = +200% portions !</strong>
    
    ✨ Mingus Astrologie - Le seul horoscope qui parle VRAIMENT aux chiens
    """
    
    return f"""
    <div style="font-family: Arial; max-width: 600px; margin: auto;">
        <h1 style="color: #ff6b35;">🐕 HOROSCOPE MINGUS</h1>
        <div style="background: #f8f9fa; padding: 25px; border-radius: 15px;">
            <div style="color: #2d5a27; line-height: 1.6;">{chien}</div>
        </div>
    </div>
    """
