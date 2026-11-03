def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(f"Mengirim pesan: {current_message}")

        sent_messages.append(current_message)


messages = [
    "Selamat pagi!",
    "Jangan lupa belajar.",
    "Tetap semangat!",
    "Semoga hari ini menyenangkan."
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nDaftar pesan awal:")
print(messages)

print("\nDaftar pesan yang sudah dikirim:")
print(sent_messages)