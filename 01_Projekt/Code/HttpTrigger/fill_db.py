import sqlite3
from web_scraper_urlhaus import web_scraper_urlhaus
from datetime import date

# Initialize the scraper and get all URLs
scraper = web_scraper_urlhaus()
all_urls = scraper.all_urls

# Connect to SQLite database
con = sqlite3.connect('db/database.db')
cur = con.cursor()

# Create the table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS domains
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     domain TEXT NOT NULL UNIQUE,
                     created_at TEXT,
                     went_offline TEXT)''')

# Define function to fetch domain list from scraper
def domain_list():
    return [(domain, date.today().strftime('%Y-%m-%d')) for domain in all_urls]

# Insert domains into the database
cur.executemany('INSERT OR IGNORE INTO domains (domain, created_at) VALUES (?, ?)', domain_list())

# Function to update went_offline
def update_went_offline(domains_not_found):
    for domain in domains_not_found:
        cur.execute("UPDATE domains SET went_offline = ? WHERE domain = ?", (date.today().strftime('%Y-%m-%d'), domain))

# Function to fetch all domains from the database
def fetch_all_domains():
    cur.execute('SELECT domain FROM domains')
    return {row[0] for row in cur.fetchall()}

# Fetch all domains from the database
all_domains_in_db = fetch_all_domains()

# Convert all_urls to a set
all_scraped_domains = set(all_urls)

# Find the domains that are in the database but not in the latest scrape
domains_not_found = all_domains_in_db - all_scraped_domains

# Update went_offline field for these domains
update_went_offline(domains_not_found)

# Commit changes and close the connection
con.commit()
con.close()
