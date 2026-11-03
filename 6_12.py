cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": "sekitar 10,7 juta jiwa",
        "fact": "Merupakan pusat ekonomi Indonesia.",
        "language": "Bahasa Indonesia",
        "currency": "Rupiah",
        "tourist_place": "Monas"
    },

    "Tokyo": {
        "country": "Jepang",
        "population": "sekitar 14 juta jiwa",
        "fact": "Memiliki transportasi kereta yang maju.",
        "language": "Bahasa Jepang",
        "currency": "Yen",
        "tourist_place": "Tokyo Tower"
    },

    "Paris": {
        "country": "Prancis",
        "population": "sekitar 2,1 juta jiwa",
        "fact": "Terkenal dengan Menara Eiffel.",
        "language": "Bahasa Prancis",
        "currency": "Euro",
        "tourist_place": "Museum Louvre"
    }
}

print("=" * 40)
print("       INFORMASI KOTA DUNIA")
print("=" * 40)

for city, information in cities.items():
    print(f"\nNama Kota: {city}")
    print("-" * 40)

    print(f"Negara          : {information['country']}")
    print(f"Populasi        : {information['population']}")
    print(f"Fakta           : {information['fact']}")
    print(f"Bahasa Resmi    : {information['language']}")
    print(f"Mata Uang       : {information['currency']}")
    print(f"Tempat Wisata   : {information['tourist_place']}")

print("\n" + "=" * 40)
print("       DATA SELESAI DITAMPILKAN")
print("=" * 40)