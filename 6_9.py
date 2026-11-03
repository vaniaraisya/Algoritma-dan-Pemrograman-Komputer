favorite_places = {
    "Vania": ["yogyakarta"],
    "Jaden": ["solo"],
    "Sinta": ["jakarta"]
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name}:")
    for place in places:
        print(f"- {place}")