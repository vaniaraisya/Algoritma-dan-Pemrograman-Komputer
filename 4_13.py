# Membuat tuple berisi lima makanan
foods = ("nasi goreng", "ayam bakar", "sate", "bakso", "soto")

# Menampilkan menu awal
print("Menu awal restoran:")
for food in foods:
    print(food)

# Mencoba mengubah salah satu item tuple
# Python akan menghasilkan TypeError
# foods[0] = "mie goreng"

# Mengubah menu dengan membuat tuple baru
foods = ("mie goreng", "ayam bakar", "sate", "rendang", "soto")

# Menampilkan menu baru
print("\nMenu baru restoran:")
for food in foods:
    print(food)
