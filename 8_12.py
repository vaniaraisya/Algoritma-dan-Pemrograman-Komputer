def make_sandwich(*items):
    print("\nSandwich yang dipesan:")
    for item in items:
        print(f"- {item}")


make_sandwich("keju", "selada")
make_sandwich("ayam", "tomat", "saus")
make_sandwich("telur", "keju", "selada", "mayones")