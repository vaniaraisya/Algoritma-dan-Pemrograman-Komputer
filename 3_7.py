guests = ["Mama", "Kakak", "Adik",
          "Papa", "Abang", "Nenek"]

print("Sayangnya aku hanya bisa mengundang dua orang untuk makan malam.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, Aku tidak bisa mengajak makan malam bersama.")

print("\nTetap diundang untuk makan malam bersama:")

print(f"Dear {guests[0]}, Tetap diundang ke makan malam bersama.")
print(f"Dear {guests[1]}, Tetap diundang ke makan malam bersama.")

del guests[0]
del guests[0]

print("\nFinal guest list:")
print(guests)