import requests
from config import BILLZ_CLIENT_ID, BILLZ_CLIENT_SECRET, BILLZ_AUTH_URL

def get_billz_token():
    response = requests.post(BILLZ_AUTH_URL, data={
        "client_id": BILLZ_CLIENT_ID,
        "client_secret": BILLZ_CLIENT_SECRET,
        # "grant_type": "client_credentials" — если нужно
    })

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Auth failed: {response.status_code} {response.text}")
