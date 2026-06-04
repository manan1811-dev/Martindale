import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz",
        database="Martindale"
    )

def create_data_table():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS DATA (
        id INT AUTO_INCREMENT PRIMARY KEY,
        url TEXT,
        title VARCHAR(255),
        address JSON,
        postal_code VARCHAR(20),
        rating_value VARCHAR(10),
        review_count INT,
        worst_rating VARCHAR(10),
        best_rating VARCHAR(10),
        contact VARCHAR(255),
        website_url TEXT,
        details TEXT,
        areas_of_practice JSON,
        total_people_count INT,
        attorneys JSON,
        status VARCHAR(25) DEFAULT 'pending',
    )
    """

    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA table created successfully")