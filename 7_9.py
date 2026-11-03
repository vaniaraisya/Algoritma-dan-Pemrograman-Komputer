sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "egg"
]

finished_sandwiches = []

print("Maaf, toko kehabisan sandwich pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\nPesanan yang tersedia:")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")

    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")