import sqlite3
from constants import DB_PATH

def get_bad_sites_from_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT domain FROM domains")
    bad_sites = [item[0] for item in cursor.fetchall()]
    conn.close()
    return bad_sites
