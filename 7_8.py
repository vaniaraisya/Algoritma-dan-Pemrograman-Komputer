sandwich_orders = ["tuna", "chicken", "beef", "egg"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")

    finished_sandwiches.append(current_sandwich)

print("\nDaftar sandwich yang sudah dibuat:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")