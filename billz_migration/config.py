import os
from dotenv import load_dotenv

load_dotenv()

# Авторизация и импорт по новому API
BILLZ_SECRET_TOKEN = os.getenv("BILLZ_SECRET_TOKEN")
BILLZ_PRODUCTS_URL = "https://api-admin.billz.ai/v2/product-import/create-with-products"
BILLZ_AUTH_URL = "https://api-admin.billz.ai/v1/auth/login"
SHOP_ID = os.getenv("BILLZ_SHOP_ID")

# (опционально) стандартные значения
BILLZ_MEASUREMENT_UNIT_ID = os.getenv("BILLZ_MEASUREMENT_UNIT_ID")
BILLZ_CATEGORY_ID = os.getenv("BILLZ_CATEGORY_ID")
BILLZ_SUPPLIER_ID = os.getenv("BILLZ_SUPPLIER_ID")
BILLZ_BRAND_ID = os.getenv("BILLZ_BRAND_ID")
BILLZ_CUSTOMERS_URL = os.getenv("BILLZ_CUSTOMERS_URL")
BILLZ_MEASUREMENT_UNIT_ID = os.getenv("BILLZ_MEASUREMENT_UNIT_ID")

POSTGRES_DSN = os.getenv("POSTGRES_DSN")
