cities = {
    "Jakarta": {
        "country": "Indonesia",
        "population": "sekitar 10,7 juta jiwa",
        "fact": "Merupakan pusat pemerintahan dan ekonomi Indonesia."
    },

    "Tokyo": {
        "country": "Jepang",
        "population": "sekitar 14 juta jiwa",
        "fact": "Memiliki sistem transportasi kereta yang sangat maju."
    },

    "Paris": {
        "country": "Prancis",
        "population": "sekitar 2,1 juta jiwa",
        "fact": "Terkenal dengan Menara Eiffel."
    }
}

for city, information in cities.items():
    print(f"\nInformasi Kota {city}:")
    for key, value in information.items():
        print(f"{key.title()}: {value}")