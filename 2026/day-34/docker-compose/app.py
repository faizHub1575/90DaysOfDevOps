from flask import Flask
import os
import psycopg2
import redis

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

REDIS_HOST = os.environ.get("REDIS_HOST")

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        db_status = "PostgreSQL Connected ✅"
        conn.close()
    except Exception as e:
        db_status = f"PostgreSQL Failed ❌: {e}"

    try:
        r = redis.Redis(host=REDIS_HOST, port=6379)
        r.ping()
        redis_status = "Redis Connected ✅"
    except Exception as e:
        redis_status = f"Redis Failed ❌: {e}"

    return f"""
    <h1>Hello Faiz DevOps 🚀</h1>
    <p>{db_status}</p>
    <p>{redis_status}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)