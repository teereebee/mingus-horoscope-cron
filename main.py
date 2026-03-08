@app.route("/test-horoscope")
def test_horoscope():
    try:
        r = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        humain = r.json().get("cancer", "")
        
        # HOROSCOPE MINGUS 100% CHIEN (drôle + long)
        horoscope_chien = mingus_chien_style(humain)
        
        return f"""
        <div style="font-family: Arial; max-width: 600px; margin: auto;">
            <h1 style="color: #ff6b35;">🐕 HOROSCOPE MINGUS DU JOUR</h1>
            <div style="background: #f8f9fa; padding: 20px; border-radius: 10px;">
                <h2 style="color: #2d5a27;">{horoscope_chien}</h2>
                <p style="color: #666; font-size: 14px;">
                    ✨ Mingus Astrologie - Tous les matins à 7h pour ton chien
                </p>
            </div>
        </div>
        """
    except:
        return "✅ Système prêt !"

def mingus_chien_style(humain):
    """Horoscope MINGUS : 100% chien, drôle, viral"""
    humain = humain.lower()
    
    # 7 styles différents selon le texte humain
    if any(mot in humain for mot in ["voyage", "déplacement", "sortie"]):
        return "🚗 <strong>ALERTE ROAD TRIP !</strong> Ton humain charge la voiture = <strong>TOI en star du coffre !</strong> Prépare-toi : 6h de route, 50 pipi-stops, motels improbables + croquettes distributeur 24h. <strong>TA MISSION : baver sur toutes les vitres !</strong> 🐾"
    
    elif any(mot in humain for mot in ["enfant", "famille", "maison"]):
        return "👨‍👩‍👧 <strong>FÊTE DES GAMINS !</strong> Les petiots = <strong>ta jackpot quotidien !</strong> Balle tennis infinie, flaques de boue, câlins collants... ⚠️ Ils oublieront ta gamelle 14h-17h → <strong>FAIS LE MORT = DOUBLE ration !</strong> 🎾"
    
    elif any(mot in humain for mot in ["travail", "bureau", "carrière"]):
        return "💼 <strong>ROI ABSOLU DU CANAPÉ !</strong> Ton humain au taf = <strong>TOI en maître du domaine !</strong> Programme : 14h sieste, 3h Netflix regard fixe, 2h 'j'ai-faim-mais-je-bouge-pas'. <strong>Bonus soir :
