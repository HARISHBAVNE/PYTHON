import random

char = "abcdefghijklmnopqrstuvwxyz1234567890@"
password = "".join(random.sample(char,6))
print(password)
no = random.randint(1,6)
print(no)
