
# Membuat dictionary bahasa pemrograman favorit
favorite_languages = {
    "vania": "python",
    "jaden": "java",
    "budi": "c++",
    "sinta": "python",
    "rizky": "javascript"
}

# Membuat list orang yang harus mengikuti polling
people = [
    "vania",
    "jaden",
    "andi",
    "sinta",
    "dina",
    "rizky"
]

# Memeriksa apakah orang sudah mengikuti polling
for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} sudah mengikuti polling.")
    else:
        print(f"{person.title()}, silakan ikuti polling bahasa favorit.")
