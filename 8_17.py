def favorite_book(title):
    """Menampilkan judul buku favorit."""
    print(f"Buku favorit saya adalah {title}.")


favorite_book("Laskar Pelangi")

def city_country(city, country):
    """Mengembalikan nama kota dan negara."""
    return f"{city}, {country}"


print(city_country("Surakarta", "Indonesia"))
print(city_country("Tokyo", "Jepang"))
print(city_country("Paris", "Prancis"))


def make_album(artist, title, songs=None):
    """Membuat dictionary berisi informasi album."""
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


print(make_album("Tulus", "Manusia"))
print(make_album("Hindia", "Menari dengan Bayangan"))
print(make_album("Taylor Swift", "Midnights", songs=13))
