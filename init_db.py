import sqlite3

def initialize_database():
    try:
        conn = sqlite3.connect('product_comments.db')
        cursor = conn.cursor()

        # Execute SQL script to create tables
        with open('data.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        cursor.executescript(sql_script)

        conn.commit()
        conn.close()
        print("Database initialized successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    initialize_database()