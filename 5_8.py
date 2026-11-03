
# Membuat list nama pengguna
usernames = ["rastiva", "jaden", "kayna", "budi", "nayla"]

# Menampilkan sapaan kepada setiap pengguna
for username in usernames:
    if username == "admin":
        print("Halo admin, apakah kamu ingin melihat laporan status?")
    else:
        print(f"Halo {username}, terima kasih telah login kembali.")
