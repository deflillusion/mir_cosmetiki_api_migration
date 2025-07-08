from fastapi import FastAPI
from db import get_products
from billz_api import send_product_to_billz

app = FastAPI()

@app.post("/sync-products")
def sync_products():
    products = get_products()
    results = []
    for product in products:
        status, text = send_product_to_billz(product)
        results.append({
            "product": product[1],
            "status": status,
            "response": text
        })
    return results
