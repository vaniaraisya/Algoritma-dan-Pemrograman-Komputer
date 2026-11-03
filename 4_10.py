# Membuat list angka kubik
cubes = []

for number in range(1, 11):
    cubes.append(number ** 3)

# Menampilkan tiga item pertama
print("The first three items in the list are:")
print(cubes[:3])

# Menampilkan tiga item tengah
print("Three items from the middle of the list are:")
print(cubes[3:6])

# Menampilkan tiga item terakhir
print("The last three items in the list are:")
print(cubes[-3:])

