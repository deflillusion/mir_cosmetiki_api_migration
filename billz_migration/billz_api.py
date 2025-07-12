import requests
from auth import get_billz_token
from config import BILLZ_PRODUCTS_URL, SHOP_ID, BILLZ_CUSTOMERS_URL, BILLZ_MEASUREMENT_UNIT_ID, BILLZ_CATEGORY_ID


def send_products_to_billz(products, batch_size=1000):
    """
    Отправка списка товаров в BILLZ пачками
    :param products: список кортежей (product[1]=articul, product[2]=name и т.д.)
    :param batch_size: размер одной пачки (по умолчанию 1000)
    :return: список результатов по каждой пачке
    """
    token = get_billz_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    results = []

    for i in range(0, len(products), batch_size):
        batch = products[i:i + batch_size]
        payload_products = []

        for product in batch:
            payload_products.append({
                "name": product[2],                        # name
                "retail_price": float(product[4]),         # price
                "supply_price": float(product[5]),
                "wholesale_price": float(product[5]),      # volume_price
                "sku": product[1],                         # articul
                "barcode": product[3],                     # barcode
                "measurement_value": float(product[7]),
                "measurement_unit_id": BILLZ_MEASUREMENT_UNIT_ID,
                "category_ids": [BILLZ_CATEGORY_ID] if product[6] == 1 else []
            })

        payload = {
            "shop_id": SHOP_ID,
            "products": payload_products
        }

        response = requests.post(
            BILLZ_PRODUCTS_URL, json=payload, headers=headers)

        results.append({
            "batch_index": i // batch_size,
            "count": len(batch),
            "status": response.status_code,
            "response": response.text
        })

    return results


def send_clients_to_billz(clients):
    """
    Отправка клиентов в BILLZ по одному.
    :param clients: список клиентов с полями: name, phone
    :return: список результатов отправки
    """
    token = get_billz_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    results = []

    for i, client in enumerate(clients):
        payload = {
            "shop_id": SHOP_ID,
            "first_name": client.get("first_name", ""),
            # можно передавать пустым
            "last_name": client.get("last_name", ""),
            "phone_number": client.get("phone_number", "")
        }

        response = requests.post(
            BILLZ_CUSTOMERS_URL, json=payload, headers=headers
        )

        results.append({
            "index": i,
            "status": response.status_code,
            "response": response.text
        })

    return results
