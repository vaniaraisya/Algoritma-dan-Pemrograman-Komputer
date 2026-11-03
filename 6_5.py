
# Membuat dictionary sungai dan negara
rivers = {
    "nil": "mesir",
    "amazon": "brasil",
    "gangga": "india"
}

# Menampilkan informasi sungai dan negara
print("Informasi Sungai:")
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

# Menampilkan nama sungai
print("\nNama-nama sungai:")
for river in rivers.keys():
    print(river.title())

# Menampilkan nama negara
print("\nNama-nama negara:")
for country in rivers.values():
    print(country.title())
