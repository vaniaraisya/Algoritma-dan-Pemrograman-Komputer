prompt = "\nMasukkan topping pizza:"
prompt += "\nKetik 'quit' untuk berhenti. "

topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"{topping} akan ditambahkan ke pizza Anda.")

prompt = "\nMasukkan topping pizza:"
prompt += "\nKetik 'quit' untuk berhenti. "

active = True

while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"{topping} akan ditambahkan ke pizza Anda.")

prompt = "\nMasukkan topping pizza:"
prompt += "\nKetik 'quit' untuk berhenti. "

while True:
    topping = input(prompt)

    if topping == "quit":
        break

    print(f"{topping} akan ditambahkan ke pizza Anda.")