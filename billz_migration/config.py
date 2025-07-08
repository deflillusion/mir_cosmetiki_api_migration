import os
from dotenv import load_dotenv

load_dotenv()

BILLZ_CLIENT_ID = os.getenv("BILLZ_CLIENT_ID")
BILLZ_CLIENT_SECRET = os.getenv("BILLZ_CLIENT_SECRET")
BILLZ_AUTH_URL = "https://api.billz.kz/api/v1/token/"
BILLZ_PRODUCTS_URL = "https://api.billz.kz/api/v1/products"

POSTGRES_DSN = os.getenv("POSTGRES_DSN")
