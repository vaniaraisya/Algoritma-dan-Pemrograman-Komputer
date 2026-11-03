def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


album_1 = make_album("Taylor Swift", "Midnights")
album_2 = make_album("Adele", "25")
album_3 = make_album("Ed Sheeran", "Divide")

print(album_1)
print(album_2)
print(album_3)

# Album dengan informasi jumlah lagu
album_4 = make_album("Coldplay", "Parachutes", songs=10)

print(album_4)