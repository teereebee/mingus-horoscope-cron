from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Mingus Horoscope OK ! 🐕"

@app.route("/test-horoscope")
def test_horoscope():
    # HOROSCOPE MINGUS avec TES RUBRIQUES
    horoscope = """
    <div style="font-family: Arial; max-width: 600px; margin: auto;">
        <h1 style="color: #ff6b35;">🐕 HOROSCOPE MINGUS - CANCER CANIN</h1>
        
        <div style="background: #f8f9fa; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
            <h3 style="color: #2d5a27;">🦴 Santé</h3>
            <p>Ton poil brille comme jamais ! Énergie cosmique au max, mais <strong>attention flatulences suspectes</strong> → bois moins vite ta gamelle !</p>
        </div>
        
        <div style="background: #fff3cd; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
            <h3 style="color: #856404;">🐾 Mon Maître</h3>
            <p>Cette semaine, il est <strong>distrait niveau champion du monde</strong>. Parfait pour squatter le canapé en mode ninja ! (il ne verra pas les poils)</p>
        </div>
        
        <div style="background: #d1ecf1; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
            <h3 style="color: #0c5460;">💪 Effort</h3>
            <p>Motivation 200% ! Tu veux <strong>courir, aboyer, vivre !</strong> Conseil astral : évite la tondeuse du voisin = mauvais karma galactique.</p>
        </div>
        
        <div style="background: #f8f9fa; padding: 25px; border-radius: 15px; margin-bottom: 20px;">
            <h3 style="color: #2d5a27;">🍖 Gourmandise</h3>
            <p><strong>SAUCISSE VOLÉE confirmée !</strong> Ce soir, regarde ton humain avec les yeux tristes 3min → il craque et te file le steak.</p>
        </div>
        
        <div style="background: #e2e3e5; padding: 25px; border-radius: 15px;">
            <h3 style="color: #383d41;">🐶 Astuce Canine</h3>
            <p><strong>"Ne jamais sous-estimer le pouvoir du regard triste"</strong> → 90% de réussite sur gamelle, balade, câlins.</p>
        </div>
        
        <p style="text-align: center; color: #666; font-size: 14px; margin-top: 30px;">
            ✨ Mingus Astrologie - Tous les matins à 7h pour ton chien
        </p>
    </div>
    """
    
    return horoscope
 padding: 25px; border-radius: 15px;">
            <div style="color: #2d5a27; line-height: 1.6;">{chien}</div>
        </div>
    </div>
    """
