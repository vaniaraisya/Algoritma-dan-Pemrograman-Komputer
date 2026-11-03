responses = {}

polling_active = True

while polling_active:
    name = input("\nSiapa nama Anda? ")
    place = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain yang ingin mengikuti polling? (ya/tidak) ")

    if repeat.lower() == "tidak":
        polling_active = False

print("\n===== HASIL POLLING LIBURAN IMPIAN =====")

for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")