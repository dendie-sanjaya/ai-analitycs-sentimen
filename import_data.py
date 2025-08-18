import sqlite3
import random

def import_sample_data():
    conn = sqlite3.connect('product_comments.db')
    cursor = conn.cursor()

    # Insert two sample products
    products = [
        ('Smartphone X', 799.99, 0.2),
        ('Laptop Y', 1200.50, 1.5)
    ]
    cursor.executemany("INSERT INTO products (name, price, weight) VALUES (?, ?, ?)", products)
    
    product_ids = [row[0] for row in cursor.execute("SELECT id FROM products")]

    # Sample comments for training data
    positive_comments = [
        "Produk ini luar biasa, sangat cepat dan efisien!",
        "Kualitasnya top banget, saya sangat puas.",
        "Desainnya elegan dan fungsionalitasnya luar biasa.",
        "Sangat direkomendasikan, performanya di atas ekspektasi.",
        "Pengiriman super cepat dan barangnya persis seperti yang diiklankan. Sempurna!",
        "Saya benar-benar menyukai produk ini. Nilai yang luar biasa untuk harganya.",
        "Ini adalah salah satu pembelian terbaik yang pernah saya lakukan. Sangat berguna!",
        "Tidak ada keluhan sama sekali. Berfungsi dengan sempurna dan terlihat bagus.",
        "Layanan pelanggan sangat membantu dan produknya tiba dalam kondisi prima.",
        "Sangat andal dan tahan lama. Produk ini melebihi harapan saya.",
        "Saya sudah lama mencari produk seperti ini. Sangat senang akhirnya menemukannya!",
        "Kualitas bahan yang digunakan terasa sangat premium. Sangat merekomendasikan.",
        "Sangat mudah digunakan dan dipasang, bahkan untuk pemula.",
        "Bekerja dengan sangat baik. Semua fitur berfungsi seperti yang dijanjikan.",
        "Sangat membantu dalam pekerjaan saya sehari-hari. Sangat praktis.",
        "Desainnya modern dan minimalis, cocok untuk dekorasi rumah saya.",
        "Kemasan produknya sangat rapi dan aman. Menunjukkan perhatian pada detail.",
        "Pengalaman berbelanja yang menyenangkan, dari awal sampai akhir.",
        "Harganya sepadan dengan kualitas yang ditawarkan. Investasi yang baik.",
        "Performa baterainya awet sekali, bisa dipakai seharian penuh.",
        "Sangat ringan dan mudah dibawa-bawa. Portabilitasnya luar biasa."
    ]

    neutral_comments = [
        "Cukup bagus, sesuai dengan deskripsi.",
        "Tidak ada yang spesial, standar saja.",
        "Berfungsi sebagaimana mestinya, tidak ada masalah.",
        "Pengirimannya cepat, produknya baik.",
        "Produk ini memenuhi kebutuhan dasar saya.",
        "Ukuran dan beratnya persis seperti yang disebutkan.",
        "Pengemasan rapi, produk tiba dengan aman.",
        "Harganya lumayan, tidak terlalu mahal, tidak terlalu murah.",
        "Tidak ada instruksi khusus, tapi mudah digunakan.",
        "Warnanya agak berbeda dari gambar, tapi tidak masalah.",
        "Saya tidak punya keluhan maupun pujian. Cukup baik.",
        "Fungsinya cukup standar untuk produk sejenis.",
        "Saya masih menguji produknya, belum bisa memberikan kesimpulan.",
        "Produknya tiba, belum sempat dicoba.",
        "Lumayanlah, tidak jelek tapi juga tidak terlalu istimewa.",
        "Ini adalah produk yang cukup memadai.",
        "Saya membeli ini karena rekomendasi teman. Belum tahu hasilnya.",
        "Barangnya sampai dengan selamat. Tidak ada kerusakan.",
        "Pilihan yang masuk akal jika Anda mencari solusi cepat.",
        "Tampilannya sederhana, fungsionalitasnya standar.",
        "Saya tidak merasa ada perbedaan signifikan dari produk sebelumnya."
    ]

    negative_comments = [
        "Sangat mengecewakan, baterai cepat habis.",
        "Kualitasnya tidak sesuai harga, ada cacat.",
        "Performanya lambat, sering lag.",
        "Pelayanannya buruk dan produknya rusak.",
        "Saya kecewa dengan produk ini. Tidak berfungsi dengan baik.",
        "Baru saja dibuka, sudah ada goresan di permukaannya. Kualitasnya buruk.",
        "Jauh dari apa yang saya harapkan. Benar-benar buang-buang uang.",
        "Tidak ada jaminan, dan sekarang produknya sudah rusak.",
        "Ada bau aneh pada produk saat pertama kali dibuka.",
        "Produk ini terlalu berat dan tidak nyaman digunakan.",
        "Fungsi yang dijanjikan tidak bekerja sama sekali.",
        "Saya sudah mencoba menghubungi penjual tapi tidak ada respons.",
        "Desainnya tidak ergonomis, membuat tangan saya sakit.",
        "Saya merasa tertipu dengan deskripsi produknya.",
        "Ini adalah pengalaman belanja online terburuk saya.",
        "Warna produk sangat pudar, tidak seperti di foto.",
        "Butuh waktu lama untuk pengiriman, dan produknya tidak sepadan.",
        "Koneksinya tidak stabil, selalu putus-putus.",
        "Bahan yang digunakan terasa murahan dan rapuh.",
        "Produknya datang tanpa beberapa bagian penting yang seharusnya ada."
    ]
    all_comments = []
    
    # Generate 100 comments for each product
    for product_id in product_ids:
        # Generate comments with mixed sentiments
        for i in range(100):
            sentiment_type = random.choice(['positive', 'neutral', 'negative'])
            if sentiment_type == 'positive':
                comment = random.choice(positive_comments)
            elif sentiment_type == 'neutral':
                comment = random.choice(neutral_comments)
            else:
                comment = random.choice(negative_comments)
            
            # Add a random unique number to avoid duplicate comments in the database.
            #comment = f"{comment} ({random.randint(1, 10000)})"
            all_comments.append((product_id, comment))

    cursor.executemany("INSERT INTO comments (product_id, comment) VALUES (?, ?)", all_comments)
    
    conn.commit()
    conn.close()
    print("Sample data imported successfully!")

if __name__ == "__main__":
    import_sample_data()