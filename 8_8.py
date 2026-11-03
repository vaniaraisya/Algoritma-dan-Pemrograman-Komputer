def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }

    return album


while True:
    print("\nMasukkan informasi album:")
    print("(Ketik 'quit' untuk berhenti)")

    artist = input("Nama artis: ")

    if artist.lower() == "quit":
        break

    title = input("Judul album: ")

    if title.lower() == "quit":
        break

    album = make_album(artist, title)

    print("\nInformasi Album:")
    print(album)

print("\nProgram selesai.")