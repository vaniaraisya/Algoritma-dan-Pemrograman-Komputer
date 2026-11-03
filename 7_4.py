prompt = "\nMasukkan topping pizza yang diinginkan:"
prompt += "\nKetik 'quit' jika sudah selesai. "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"Topping {topping} akan ditambahkan ke pizza Anda.")