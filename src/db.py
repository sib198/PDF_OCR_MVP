import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="documents",
        user="sibanitiwari08",   # 👈 your mac username
        host="localhost",
        port="5432"
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        page_number INT,
        member_id TEXT,
        payer_name TEXT,
        copay TEXT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

