import sqlite3
import pytest

# Create a fixture to set up the database connection
# Fixture prepares everything so that the test can be executed like in this case a DB connection
# wihtout DB connection u cant do anything
@pytest.fixture
def database_connection():
    connection = sqlite3.connect('db/database.db')  # Use an in-memory SQLite database for testing
    '''
    connection = sqlite3.connect(':memory:')  # Use an in-memory SQLite database for testing / local new DB
    '''
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS domains (domain TEXT, created_at TEXT)''')
    yield connection, cur
    connection.close()

# Define test functions for database operations ( Exampl. Test connection, inserting, deleting, if certain data exists etc)
def test_database_connection(database_connection):
    connection, _ = database_connection
    # Check if the database connection is established
    assert connection is not None

def test_insert_data(database_connection):
    connection, cur = database_connection
    # Insert data into the in-memory database
    cur.execute("INSERT INTO domains (domain, created_at) VALUES (?, ?)", ('example.com', '2023-09-25'))
    connection.commit()  # Commit the transaction

    # Fetch the inserted data from the database
    cur.execute("SELECT domain FROM domains WHERE domain=?", ('example.com',))
    result = cur.fetchone()

    # Assert that the data was inserted correctly
    assert result is not None
    assert result[0] == 'example.com'


if __name__ == "__main__":
    pytest.main()
