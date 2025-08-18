CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    weight REAL NOT NULL
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    comment TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);