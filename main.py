def chien_horoscope(humain):
    """Horoscope MINGUS : drôle, long, viral 🐕"""
    humain = humain.lower()
    
    # 12 templates drôles + personnalisés
    templates = {
        "voyages": """🚗 <strong>ALERTE VOYAGE !</strong> 🗺️
Ton humain fait sa valise = <strong>ROAD TRIP CHIOT !</strong> 
Prépare-toi : 8h de voiture, 47 arrêts pipi, et TOI à l'arrière avec les gosses qui te tirent la queue.
✅ <strong>Bonus : motels pourris + croquettes de luxe au distributeur !</strong> 🏪""",
        
        "enfants": """👶 <strong>FUSÉE A GAMBAS !</strong> 🎾
Les petiots humains = <strong>TA JOURNÉE DE RÊVE !</strong>
Balle tennis x1000, flaques de boue, câlins baveux... 
⚠️ <strong>Attention : ils oublieront de te nourrir entre 14h-17h</strong> 
💡 <strong>Stratégie : fais le mort → ils paniquent → DOUBLE gamelle !</strong>""",
        
        "travail": """💼 <strong>LIBERTÉ TOTALE !</strong> 🛋️
Ton humain stresse au bureau = <strong>TOI ROI DU CANAPÉ !</strong>
Journée : 14h de sieste, 3h de ronflements, 2h de regard vide vers Netflix.
🎁 <strong>Bonus soir : il rentre HS → TOUTES les caresses pour TOI !</strong> 😍""",
        
        "amour": """💕 <strong>TOI = 3ÈME ROUE !</strong> ❤️
Ton humain en mode lover = <strong>TOI en STAR secondaire !</strong>
Avantage : dîners romantiques = <strong>RESTES DE FILET MIGNON !</strong> 🥩
Inconvénient : moins de câlins (bof).
💡 <strong>Solution : fais semblant d'être triste → câlins x3 !</strong> 🥺""",
        
        "argent": """💰 <strong>JACKPOT CROQUETTES !</strong> 🥓
Prime / héritage / whatever = <strong>TOI BOURREAU DES FAISEAUX !</strong>
Ce soir : <strong>BOUCHER PLEIN DE VIANDE !</strong> + jouets qui couinent.
⚠️ <strong>Demain : ton humain dépensera tout sur Amazon → patience... </strong>📦""",
        
        "santé": """🏥 <strong>TOI = INFIRMIER STAR !</strong> 🩹
Ton humain malade = <strong>TOI en mode câlin-thérapie !</strong>
Stratégie gagnante : <strong>COLLE-TOI à lui H24 → il oublie son rhume !</strong>
Bonus : il reste à la maison = <strong>DOUBLE balades !</strong> 🚶‍♂️🐾""",
        
        "default": """⭐ <strong>PARFAIT MARDI CHIOT !</strong> 🌈
Aujourd'hui
