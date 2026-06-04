import mysql.connector


def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz"
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Martindale")

    cursor.close()
    conn.close()


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz",
        database="Martindale"
    )


# =========================
# STATE TABLE
# =========================

def create_state_table():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS state_url (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category_url TEXT,
        state_name VARCHAR(255),
        state_url TEXT,
        status VARCHAR(25) DEFAULT 'pending',
        UNIQUE KEY uq_state_url (state_url(255))
    )
    """

    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()

    print("state_url table created successfully")


def insert_state_url(category_url, state_urls, state_names):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO state_url (
        category_url,
        state_name,
        state_url,
        status
    )
    VALUES (%s, %s, %s, %s)
    """

    data = [
        (
            category_url,
            state_name,
            state_url,
            'pending'
        )
        for state_name, state_url in zip(state_names, state_urls)
    ]

    cursor.executemany(query, data)

    conn.commit()
    cursor.close()
    conn.close()


def fetch_state_url():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT state_name, state_url
    FROM state_url
    WHERE status = 'pending'
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def update_state_status(state_url):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE state_url
    SET status = 'success'
    WHERE state_url = %s
    """

    cursor.execute(query, (state_url,))
    conn.commit()

    cursor.close()
    conn.close()


# =========================
# CITY TABLE
# =========================

def create_city_url_table():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS city_url (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state_name VARCHAR(255),
        state_url TEXT,
        city_name VARCHAR(255),
        city_url TEXT,
        status VARCHAR(20) DEFAULT 'pending',
        UNIQUE KEY uq_city_url (city_url(255))
    )
    """

    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()

    print("city_url table created successfully")


def insert_city_url(
    state_name,
    state_url,
    city_urls,
    city_names
):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO city_url (
        state_name,
        state_url,
        city_name,
        city_url,
        status
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    data = [
        (
            state_name,
            state_url,
            city_name,
            city_url,
            'pending'
        )
        for city_name, city_url in zip(city_names, city_urls)
    ]

    cursor.executemany(query, data)

    conn.commit()

    cursor.close()
    conn.close()