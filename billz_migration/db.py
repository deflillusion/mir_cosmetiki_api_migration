import psycopg2
from config import POSTGRES_DSN

def get_products():
    conn = psycopg2.connect(POSTGRES_DSN)
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products LIMIT 20;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
