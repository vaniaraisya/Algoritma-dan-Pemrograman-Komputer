
# Membuat dictionary istilah pemrograman
glossary = {
    "Variable": "Tempat untuk menyimpan data.",
    "List": "Struktur data untuk menyimpan banyak nilai.",
    "Loop": "Perulangan untuk menjalankan kode berulang kali.",
    "If Statement": "Kondisi untuk menentukan perintah yang dijalankan.",
    "Dictionary": "Struktur data yang menyimpan pasangan key dan value."
}

# Menampilkan istilah dan artinya
for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"    {meaning}\n")
