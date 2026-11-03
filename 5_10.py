
# Membuat list pengguna yang sudah terdaftar
current_users = [
    "Vania",
    "Arya",
    "Budi",
    "Rasti",
    "Kayna"
]

# Membuat list pengguna baru
new_users = [
    "Nayla",
    "Arya",
    "Dina",
    "Renaai",
    "Vania"
]

# Mengubah semua nama menjadi huruf kecil
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

# Memeriksa nama pengguna baru
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nama {new_user} sudah digunakan. Masukkan nama lain.")
    else:
        print(f"Nama {new_user} tersedia.")
