import random

chars = "abcdefghijklmnopqrstuvwxyz"
chars += chars.upper()
chars += "1234567890"

length = int(input("Length: "))
password = "".join(random.sample(chars, length))
print(password)