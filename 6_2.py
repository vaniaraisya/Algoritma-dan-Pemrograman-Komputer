
# Membuat dictionary angka favorit
favorite_numbers = {
    "Vania": 7,
    "Jaden": 10,
    "Budi": 5,
    "Sinta": 8,
    "Rizky": 12
}

# Menampilkan angka favorit setiap orang
print("Daftar Angka Favorit:")

for name, number in favorite_numbers.items():
    print(f"{name} menyukai angka {number}.")
