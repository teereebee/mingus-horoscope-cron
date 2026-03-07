def chien_horoscope(humain):
    """Horoscope MINGUS simple (sans multi-lignes)"""
    humain = humain.lower()
    
    if "voyages" in humain:
        return "🚗 ROAD TRIP ! Ton humain fait ses valises = gamelle + cousins obligatoires ! 🐾"
    elif "enfants" in humain or "famille" in humain:
        return "👶 Journée balle infinie avec les petiots ! 🎾"
    elif "travail" in humain or "carrière" in humain:
        return "💼 Ton humain au bureau = TOI ROI DU CANAPÉ ! 🛋️"
    elif "amour" in humain or "couple" in humain:
        return "💕 Restes de dîners romantiques ce soir ! 🥩"
    elif "argent" in humain:
        return "💰 Croquettes PREMIUM au menu ! 🥓"
    else:
        return "⭐ Dormir, manger, jouer = journée parfaite ! 🐕"
