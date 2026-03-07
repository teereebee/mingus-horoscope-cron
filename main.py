@app.route("/test-horoscope")
def test_horoscope():
    """Horoscope CHIEN adapté"""
    try:
        # API humaine française
        resp = requests.get("https://kayoo123.github.io/astroo-api/jour.json")
        data = resp.json()
        horo_humain = data.get("cancer", "Horoscope indisponible")
        
        # On réécrit pour CHIENS (IA-like)
        horo_chien = chien_horoscope(horo_humain)
        
        return f"""
        <h2>🐕 Horoscope HUMAIN (Cancer)</h2>
        <p><em>{horo_humain}</em></p>
        <hr>
        <h2>🐶 Horoscope CHIEN (adapté)</h2>
        <p><strong>{horo_chien}</strong></p>
        """
    except Exception as e:
        return f"❌ Erreur : {str(e)}"

def chien_horoscope(humain):
    """Transforme horoscope humain → chien"""
    humain = humain.lower()
    
    # RÈGLES AUTOMATIQUES
    if "voyages" in humain:
        return "🚗 Ton humain prépare un GRAND VOYAGE ! Prépare ta gamelle et ton coussin ! 🐾"
    elif "enfants" in humain or "famille" in humain:
        return "👨‍👩‍👧‍👦 Les petits humains jouent avec toi toute la journée ! Balle infinie ! 🎾"
    elif "travail" in humain or "carrière" in humain:
        return "💼 Ton humain rentre tôt du bureau → SOIRÉE CÂLINS garantie ! 🛋️"
    elif "amour" in humain or "couple" in humain:
        return "💕 Ton humain est amoureux → DOUBLE ration de caresses aujourd'hui ! 😍"
    elif "argent" in humain:
        return "💰 Croquettes PREMIUM au menu ce soir ! Ton humain a eu sa paye ! 🥩"
    else:
        return "⭐ Aujourd'hui = JOURNÉE PARFAITE pour dormir, manger, jouer ! 🐕💤🎾"
