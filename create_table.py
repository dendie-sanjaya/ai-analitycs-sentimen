import sqlite3

# Nama file database yang akan dibuat
DB_FILE = 'product_comments.db'

def create_tables():
    """
    Menghubungkan ke database SQLite dan membuat dua tabel:
    - products
    - comments
    """
    try:
        # Menghubungkan ke database. Jika file tidak ada, akan dibuat.
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # SQL untuk membuat tabel 'products'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            weight REAL NOT NULL
        );
        """)

        # SQL untuk membuat tabel 'comments'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            comment TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
        """)

        # Simpan perubahan dan tutup koneksi
        conn.commit()
        print("Tabel 'products' dan 'comments' berhasil dibuat.")

    except sqlite3.Error as e:
        print(f"Terjadi kesalahan SQLite: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_tables()