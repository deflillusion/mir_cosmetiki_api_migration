import requests
from auth import get_billz_token
from config import BILLZ_PRODUCTS_URL


def send_product_to_billz(product):
    token = get_billz_token()
    payload = {
        "external_id": str(product[0]),
        "name": product[1],
        "price": float(product[2])
    }

    response = requests.post(
        BILLZ_PRODUCTS_URL,
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    return response.status_code, response.text
