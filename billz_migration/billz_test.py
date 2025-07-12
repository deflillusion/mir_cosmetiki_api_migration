import requests
import os
from dotenv import load_dotenv
from config import BILLZ_PRODUCTS_URL, SHOP_ID, BILLZ_CUSTOMERS_URL, BILLZ_MEASUREMENT_UNIT_ID, BILLZ_CATEGORY_ID

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
                "name": "Тестовый товар 12-07-2025",
                "retail_price": 1999,
                "supply_price": 999,
                "wholesale_price": 999,
                "sku": "TEST-999",
                "barcode": "1234567890999",
                "measurement_value": 9,
                "measurement_unit_id": BILLZ_MEASUREMENT_UNIT_ID,
                "category_ids": [BILLZ_CATEGORY_ID]
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
