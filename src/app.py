from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/search")
def search():
    member_id = request.args.get("member_id")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT page_number, member_id, payer_name, copay
        FROM documents
        WHERE member_id = %s
    """, (member_id,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)


@app.route("/all")
def all_records():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT page_number, member_id, payer_name, copay
        FROM documents
    """)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
