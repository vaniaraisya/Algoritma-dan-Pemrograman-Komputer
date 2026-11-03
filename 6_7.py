person_1 = {
    "first_name": "Vania",
    "last_name": "Raisya",
    "age": 19,
    "city": "Surakarta"
}

person_2 = {
    "first_name": "Jaden",
    "last_name": "Pratama",
    "age": 20,
    "city": "Jakarta"
}

person_3 = {
    "first_name": "Sinta",
    "last_name": "Aulia",
    "age": 19,
    "city": "Yogyakarta"
}

people = [person_1, person_2, person_3]

for person in people:
    print("\nInformasi Orang:")
    for key, value in person.items():
        print(f"{key.title()}: {value}")