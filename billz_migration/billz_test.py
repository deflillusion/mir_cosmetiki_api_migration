import requests
import os
from dotenv import load_dotenv

load_dotenv()

BILLZ_AUTH_URL = os.getenv("BILLZ_AUTH_URL")
BILLZ_SECRET_TOKEN = os.getenv("BILLZ_SECRET_TOKEN")
BILLZ_PRODUCTS_URL = os.getenv("BILLZ_PRODUCTS_URL")


def get_billz_token():
    response = requests.post(
        BILLZ_AUTH_URL,
        json={"secret_token": BILLZ_SECRET_TOKEN},
        headers={"Content-Type": "application/json"}
    )

    print(f"🔍 Response status: {response.status_code}")
    print(f"🔍 Response body: {response.text}")

    if response.status_code == 200:
        data = response.json().get("data", {})
        token = data.get("access_token")
        if not token:
            raise Exception("⚠️ 'access_token' not found in response['data']")
        print("✅ Auth successful")
        return token
    else:
        raise Exception(
            f"❌ Auth failed: {response.status_code} {response.text}")


print("📦 BILLZ_PRODUCTS_URL =", BILLZ_PRODUCTS_URL)


def send_test_product():
    token = get_billz_token()

    payload = {
        "shop_id": "fa0a3f4b-1af4-4a86-a40c-5e0b39f127d9",
        "products": [
            {
                "name": "Тестовый товар",
                "retail_price": 0,
                "supply_price": 0,
                "wholesale_price": 0,
                "sku": "TEST-123",
                "barcode": "1234567890123",
                "measurement_value": 0.9,
            }
        ]
    }

    response = requests.post(
        BILLZ_PRODUCTS_URL,
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    print(f"📤 Status: {response.status_code}")
    print(f"📦 Response: {response.text}")


if __name__ == "__main__":
    send_test_product()
