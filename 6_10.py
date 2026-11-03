favorite_numbers = {
    "Vania": [7, 10, 15],
    "Jaden": [5, 8],
    "Budi": [3, 12, 20],
    "Sinta": [4, 9],
    "Rizky": [6, 11, 18]
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name}:")
    for number in numbers:
        print(f"- {number}")