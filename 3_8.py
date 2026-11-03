places = ["Arab", "Swiss", "Paris", "Korea Selatan", "Jepang"]

# Menampilkan urutan asli
print("Original list:")
print(places)

# Mengurutkan berdasarkan abjad tanpa mengubah list asli
print("\nAlphabetical order:")
print(sorted(places))

# Membuktikan urutan asli tidak berubah
print("\nOriginal list:")
print(places)

# Mengurutkan berdasarkan abjad terbalik
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Membuktikan urutan asli masih sama
print("\nOriginal list:")
print(places)

# Membalik urutan list
places.reverse()
print("\nReverse list:")
print(places)

# Mengembalikan urutan list seperti semula
places.reverse()
print("\nOriginal order again:")
print(places)

# Mengurutkan list berdasarkan abjad
places.sort()
print("\nAlphabetical order:")
print(places)

# Mengurutkan list berdasarkan abjad terbalik
places.sort(reverse=True)
print("\nReverse alphabetical order:")
print(places)