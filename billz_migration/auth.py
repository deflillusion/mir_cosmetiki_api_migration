import requests
from config import BILLZ_SECRET_TOKEN, BILLZ_AUTH_URL


def get_billz_token():
    response = requests.post(
        BILLZ_AUTH_URL,
        json={"secret_token": BILLZ_SECRET_TOKEN},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Auth failed: {response.status_code} {response.text}")
