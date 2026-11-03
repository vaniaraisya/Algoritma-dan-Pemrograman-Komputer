pet_1 = {
    "animal": "Kucing",
    "owner": "Vania"
}

pet_2 = {
    "animal": "Anjing",
    "owner": "Jaden"
}

pet_3 = {
    "animal": "Kelinci",
    "owner": "Sinta"
}

pet_4 = {
    "animal": "Burung",
    "owner": "Rizky"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print("\nInformasi Hewan Peliharaan:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")