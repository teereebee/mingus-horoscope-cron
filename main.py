import os
import requests
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

KLAVIYO_API_KEY = os.environ["KLAVIYO_API_KEY"]
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
FROM_EMAIL = os.environ.get("FROM_EMAIL", "horoscope@example.com")
FROM_NAME = os.environ.get("FROM_NAME", "Horoscope Mingus")

KLAVIYO_BASE_URL = "https://a.klaviyo.com/api"


def get_profiles_with_dog_list():
    headers = {
        "Authorization": f"Klaviyo-API-Key {KLAVIYO_API_KEY}",
        "accept": "application/json",
        "revision": "2023-12-15",
    }
    profiles = []
    url = f"{KLAVIYO_BASE_URL}/profiles/"

    params = {
        "fields[profile]": "email,first_name,last_name,properties",
        "page[size]": 100,
    }

    while True:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        for item in data.get("data", []):
            attrs = item.get("attributes", {})
            props = attrs.get("properties", {}) or {}
            dog_list = props.get("dog_list")
            email = attrs.get("email")
            if email and dog_list:
                profiles.append(
                    {
                        "email": email,
                        "first_name": attrs.get("first_name"),
                        "last_name": attrs.get("last_name"),
                        "dog_list": dog_list,
                    }
                )
        links = data.get("links", {})
        next_link = links.get("next")
        if not next_link:
            break
        url = next_link
        params = None

    return profiles


def parse_dog_list(dog_list_raw: str):
    if not dog_list_raw:
        return []
    parts = [p.strip() for p in dog_list_raw.replace(";", ",").split(",")]
    return [p for p in parts if p]


def generate_daily_horoscope_fr(dog_name: str, today: datetime):
    jour = today.strftime("%A %d %B %Y")
    base = (
        f"Aujourd'hui, {jour}, {dog_name} ressentira une énergie particulière. "
        "Son intuition canine sera plus forte que d'habitude : observe sa façon de renifler, d'écouter et de te regarder. "
        "C'est une excellente journée pour renforcer votre lien avec du temps de qualité, des caresses et un peu de jeu."
    )
    conseils = [
        "Privilégie une promenade un peu plus longue que d'habitude, dans un endroit calme où il pourra explorer à son rythme.",
        "Garde un oeil sur son alimentation aujourd'hui : évite les extras trop gras ou trop sucrés, mise sur la simplicité.",
        "Si tu le sens plus nerveux, parle-lui doucement et propose-lui un coin tranquille pour se reposer.",
        "Un nouveau jouet d'occupation (tapis de fouille, Kong, etc.) pourrait le stimuler positivement.",
        "N'hésite pas à prendre une photo de lui aujourd'hui : ce moment pourrait devenir un beau souvenir.",
    ]
    idx = (hash(dog_name + jour) % len(conseils))
    return base + " " + conseils[idx]


def build_email_html(owner_first_name, horoscopes_by_dog, today: datetime):
    jour = today.strftime("%A %d %B %Y")
    if owner_first_name:
        intro = f"<p>Bonjour {owner_first_name},</p>"
    else:
        intro = "<p>Bonjour,</p>"

    intro += (
        f"<p>Voici l'horoscope canin Mingus pour aujourd'hui "
        f"(<strong>{jour}</strong>) pour ton ou tes compagnons :</p>"
    )

    blocs = []
    for dog_name, texte in horoscopes_by_dog.items():
        blocs.append(
            f"""
            <h3 style="margin-top:24px;margin-bottom:8px;">🐶 {dog_name}</h3>
            <p style="margin-top:0;margin-bottom:12px;line-height:1.5;">{texte}</p>
            """
        )

    outro = """
    <p style="margin-top:24px;">
        Merci de faire confiance à <strong>Mingus</strong> pour t'accompagner
        dans le quotidien de ton chien. 🐾
    </p>
    <p style="font-size:12px;color:#777;">
        Tu peux mettre à jour les informations de ton chien depuis ta page d'inscription.
    </p>
    """

    html = (
        "<html><body>"
        + intro
        + "".join(blocs)
        + outro
        + "</body></html>"
    )
    return html


def send_email_via_sendgrid(to_email, subject, html_content):
    message = Mail(
        from_email=(FROM_EMAIL, FROM_NAME),
        to_emails=to_email,
        subject=subject,
        html_content=html_content,
    )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    return response.status_code


def run_daily_job():
    today = datetime.now()
    profiles = get_profiles_with_dog_list()
    for p in profiles:
        email = p["email"]
        first_name = p.get("first_name")
        dog_list_raw = p["dog_list"]

        dog_names = parse_dog_list(dog_list_raw)
        if not dog_names:
            continue

        horoscopes_by_dog = {}
        for dog in dog_names:
            horoscopes_by_dog[dog] = generate_daily_horoscope_fr(dog, today)

        html = build_email_html(first_name, horoscopes_by_dog, today)
        subject = f"Horoscope canin Mingus – {today.strftime('%d/%m/%Y')}"
        try:
            status = send_email_via_sendgrid(email, subject, html)
            print(f"Email envoyé à {email} (status {status})")
        except Exception as e:
            print(f"Erreur envoi {email}: {e}")


if __name__ == "__main__":
    run_daily_job()
