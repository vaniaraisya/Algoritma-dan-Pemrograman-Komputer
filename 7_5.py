while True:
    age = input("\nBerapa usia Anda? ")
    age = int(age)

    if age < 3:
        print("Tiket bioskop gratis.")
    elif age <= 12:
        print("Harga tiket adalah $10.")
    else:
        print("Harga tiket adalah $15.")

    print("Masukkan -1 jika ingin berhenti.")
    if age == -1:
        break