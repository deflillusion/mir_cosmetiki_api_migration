import psycopg2
from config import POSTGRES_DSN


def get_products():
    conn = psycopg2.connect(POSTGRES_DSN)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            p.g_product,
            p.articul,
            p.name,
            p.barcode,
            p.price,
            p.volume_price,
            p.is_kaspi_shop,
            s.amount 
        FROM 
            public.g_product p
        JOIN 
            public.lt_sklad_product s ON p.g_product = s.g_product
        WHERE 
            p.is_active = 1 AND p.is_category = 0 AND s.amount > 0 AND s.amount % 1 = 0 AND p.price > 0 AND p.volume_price > 0
        ORDER BY 
            p.g_product ASC
        ;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_unique_clients():
    """
    Возвращает клиентов с уникальными номерами телефонов,
    у которых is_category = 0 и номер телефона не пустой.
    """
    conn = psycopg2.connect(POSTGRES_DSN)
    cur = conn.cursor()

    query = """
    SELECT 
        p.g_client,
        p.name,
        p.phone
    FROM public.g_client p
    WHERE p.is_category = 0
      AND p.is_active = 1
      AND p.phone IS NOT NULL
      AND p.phone != ''
      AND (
          SELECT COUNT(*) 
          FROM public.g_client sub 
          WHERE sub.phone = p.phone
      ) = 1
    ORDER BY p.g_client;
    """

    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
