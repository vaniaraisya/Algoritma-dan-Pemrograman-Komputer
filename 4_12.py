# Membuat list makanan favorit
my_foods = ["pizza", "nasi goreng", "bakso"]

# Membuat salinan list untuk teman
friend_foods = my_foods[:]

# Menambahkan makanan ke masing-masing list
my_foods.append("sate")
friend_foods.append("sushi")

# Menampilkan makanan favorit saya
print("Makananan kesukaaan saya adalah:")
for food in my_foods:
    print(food)

# Menampilkan makanan favorit teman
print("\nMakanan kesukaan teman saya adalah:")
for food in friend_foods:
    print(food)
