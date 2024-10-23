import os

import requests
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API Finnhub
finnhub_api_key = os.getenv("FINNHUB_API_KEY")

if finnhub_api_key is None:
    raise ValueError("La clé API Finnhub n'est pas définie. Vérifie ton fichier .env.")


# URL pour récupérer les composants du S&P 500
url = (
    f"https://finnhub.io/api/v1/index/constituents?symbol=^GSPC&token={finnhub_api_key}"
)
print(url)
# Faire la requête
response = requests.get(url)

# Vérifier la réponse
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erreur : {response.status_code}")
