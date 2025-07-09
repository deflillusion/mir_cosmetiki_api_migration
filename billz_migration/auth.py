import requests
from config import BILLZ_SECRET_TOKEN, BILLZ_AUTH_URL


def get_billz_token():
    response = requests.post(
        BILLZ_AUTH_URL,
        json={"secret_token": BILLZ_SECRET_TOKEN},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        data = response.json().get("data", {})
        token = data.get("access_token")
        if not token:
            raise Exception("⚠️ 'access_token' not found in response['data']")
        return token
    else:
        raise Exception(
            f"❌ Auth failed: {response.status_code} {response.text}")
