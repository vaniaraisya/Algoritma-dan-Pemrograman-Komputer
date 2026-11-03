countries = ["Indonesia", "Jepang", "Malaysia", "Thailand"]

# Menampilkan list awal
print("Original list:")
print(countries)

# Mengakses elemen list
print("\nFirst country:")
print(countries[0])

# Menambahkan elemen di akhir list
countries.append("Singapura")
print("\nAfter append:")
print(countries)

# Menambahkan elemen pada posisi tertentu
countries.insert(1, "Korea Selatan")
print("\nAfter insert:")
print(countries)

# Menghapus elemen menggunakan del
del countries[2]
print("\nAfter del:")
print(countries)

# Menghapus elemen terakhir menggunakan pop
removed_country = countries.pop()
print("\nAfter pop:")
print(countries)

# Menghapus elemen berdasarkan nama
countries.remove("Malaysia")
print("\nAfter remove:")
print(countries)

# Mengurutkan list berdasarkan abjad
countries.sort()
print("\nAfter sort:")
print(countries)

# Mengurutkan list tanpa mengubah aslinya
print("\nUsing sorted:")
print(sorted(countries))

# Membalik urutan list
countries.reverse()
print("\nAfter reverse:")
print(countries)

# Menghitung jumlah elemen
print("\nTotal countries:")
print(len(countries))