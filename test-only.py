import random

# Use 'ctrl + alt + up/down arrow'
# for i in range(1,101):
#   n = random.randint(5,15)
#   n2 = random.randint(5,15)
# 
#   if n < n2:
#      n, n2 = n2, n
#   if n % n2 != 0:
#      n = n2 * random.randint(1,5)
#   print(f"{i}) {n} / {n2} = {n // n2}")

# def calling(name):
#    print(f"Hello, {name}!")

# enter = input("Enter your name:\n>> ")
# calling(enter)

file_path = input("Enter a file name:\n>> ")

try:
   with open(file_path, "r") as file:
      content = file.read()
   print({content})

except FileNotFoundError:
   print(f"{file_path} does not exist.")