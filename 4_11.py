# Membuat list pizza
pizzas = ["pepperoni", "cheese", "chicken"]

# Menyalin list pizza
friend_pizzas = pizzas[:]

# Menambahkan pizza ke masing-masing list
pizzas.append("beef")
friend_pizzas.append("mushroom")

# Menampilkan pizza favorit saya
print("Pizza kesukaan ku adalah:")
for pizza in pizzas:
    print(pizza)

# Menampilkan pizza favorit teman
print("\nPizza kesukaan temanku adalah:")
for pizza in friend_pizzas:
    print(pizza)
