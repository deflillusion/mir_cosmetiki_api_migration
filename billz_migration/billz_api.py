import requests
from auth import get_billz_token
from config import BILLZ_PRODUCTS_URL, SHOP_ID, BILLZ_CUSTOMERS_URL


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
                "measurement_value": float(product[6]),
                # "measurement_unit_id": "8711b37a-42bf-4bc2-84fd-6de4673d6302"  # kg
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
