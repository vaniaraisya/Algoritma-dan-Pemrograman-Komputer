
# Membuat list nama pengguna
usernames = []

# Memeriksa apakah list kosong
if usernames:
    for username in usernames:
        if username == "vania":
            print("Halo vania, apakah kamu ingin melihat laporan status?")
        else:
            print(f"Halo {username}, terima kasih telah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")
