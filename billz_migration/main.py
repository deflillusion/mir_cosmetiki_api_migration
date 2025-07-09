from fastapi import FastAPI
from db import get_products
from db import get_unique_clients
from billz_api import send_products_to_billz, send_clients_to_billz

app = FastAPI()


@app.post("/sync-products")
def sync_products():
    products = get_products()
    results = send_products_to_billz(products)
    return {
        "total_products": len(products),
        "batches_sent": len(results),
        "results": results
    }


@app.post("/sync-clients")
def sync_clients():
    """
    Загружает уникальных клиентов из базы данных и отправляет их в BILLZ
    """
    raw_clients = get_unique_clients()  # [(g_client, name, phone), ...]
    clients = [{"first_name": name, "phone_number": phone}
               for _, name, phone in raw_clients]

    results = send_clients_to_billz(clients)  # <-- вот это должно быть

    return {"count": len(clients), "results": results}
