# 1. Pengujian kesamaan dan ketidaksamaan string
car = "subaru"

print("String equality:")
print(car == "subaru")  # True
print(car == "audi")    # False

print("\nString inequality:")
print(car != "audi")    # True
print(car != "subaru")  # False


# 2. Pengujian menggunakan lower()
name = "VANIA"

print("\nTesting lower():")
print(name.lower() == "vania")  # True
print(name.lower() == "VANIA")  # False


# 3. Pengujian numerik
number = 10

print("\nNumerical tests:")
print(number == 10)   # True
print(number != 10)   # False
print(number > 5)     # True
print(number > 15)    # False
print(number < 15)    # True
print(number < 5)     # False
print(number >= 10)   # True
print(number >= 15)   # False
print(number <= 10)   # True
print(number <= 5)    # False


# 4. Pengujian menggunakan and
age = 18

print("\nTesting and:")
print(age >= 18 and age <= 20)  # True
print(age >= 20 and age <= 25)  # False


# Pengujian menggunakan or
print("\nTesting or:")
print(age == 18 or age == 20)  # True
print(age == 15 or age == 20)  # False


# 5. Pengujian item dalam list
foods = ["pizza", "burger", "sushi"]

print("\nTesting item in list:")
print("pizza" in foods)   # True
print("sate" in foods)    # False


# 6. Pengujian item tidak dalam list
print("\nTesting item not in list:")
print("sate" not in foods)    # True
print("pizza" not in foods)   # False
