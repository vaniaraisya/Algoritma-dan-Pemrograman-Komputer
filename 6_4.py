
# Membuat dictionary istilah pemrograman
glossary = {
    "Variable": "Tempat untuk menyimpan data.",
    "List": "Struktur data untuk menyimpan banyak nilai.",
    "Loop": "Perulangan untuk menjalankan kode berulang kali.",
    "If Statement": "Kondisi untuk menentukan perintah yang dijalankan.",
    "Dictionary": "Struktur data yang menyimpan pasangan key dan value.",
    "String": "Tipe data yang berisi kumpulan karakter.",
    "Integer": "Tipe data berupa bilangan bulat.",
    "Boolean": "Tipe data yang memiliki nilai True atau False.",
    "Float": "Tipe data berupa bilangan desimal.",
    "Function": "Blok kode yang dapat digunakan kembali."
}

# Menampilkan semua istilah dan artinya
for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"    {meaning}\n")
