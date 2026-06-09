import os
import time

def reading(f_name):
   if not os.path.exists(f_name):
      print("\nThe file you are looking for does not exist.")
      time.sleep(1)
   elif f_name.strip() == "":
      print("\nNothing to read.")
      time.sleep(1)
   elif os.path.getsize(f_name) == 0:
      print(f"\n{f_name} is empty... Try adding something in the file first.")
      time.sleep(1)
   elif not os.path.isfile(f_name):
      print(f"\n{f_name} is not a file.")
      time.sleep(1)
   elif not os.access(f_name, os.R_OK):
      print(f"\nYou do not have permission to read {f_name}.")
      time.sleep(1)
   else:
      file = open(f_name)
      print(f"\n{file.read()}")
      file.close()
      time.sleep(3)

def appending(f_name, new):
   if not os.path.exists(f_name):
      print(f"\nThe file does not exist.")
      time.sleep(1)
   elif new.strip() == "":
      print(f"\nNothing to add.")
      time.sleep(1)
   
   else:
      file = open(f_name, "a")
      file.write(f"\n{new}")
      file.close()
      print(f"\nSuccessfully added '{new}' to {f_name}!")
      time.sleep(1)

def writing(f_name, new):
   if not os.path.exists(f_name):
      print(f"\nThe file does not exist.")
      time.sleep(1)
   elif new.strip() == "":
      print(f"\nNothing to write.")
      time.sleep(1)
   else:
      file = open(f_name, "w")
      file.write(new)
      file.close()
      print(f"\nSuccessfully wrote to {f_name}!")
      time.sleep(1)

def creating(f_name):
   if os.path.exists(f_name):
      print(f"\nThe file is already exist.")
      time.sleep(1)
   elif f_name.strip() == "":
      print(f"\nNothing to create.")
      time.sleep(1)
   else:
      file = open(f_name, "x")
      print(f"\n{f_name} created successfully!")
      time.sleep(1)

def deleting(f_name):
   if not os.path.exists(f_name):
      print(f"\n{f_name}: NOT FOUND!\nThe file you want to delete does not exist.")
      time.sleep(1)
   elif f_name.strip() == "":
      print(f"\nNothing to delete.")
      time.sleep(1)
   else:
      os.remove(f_name)
      print(f"\n{f_name} has been deleted successfully!")
      time.sleep(1)

def renaming(old_name, new_name):
   if not os.path.exists(old_name):
      print(f"\n{old_name}: NOT FOUND!\nThe file you want to rename does not exist")
      time.sleep(1)
   elif old_name.strip() == "":
      print(f"\nNothing to rename.")
      time.sleep(1)
   else:
      os.rename(old_name, new_name)
      print(f"\nSuccessfully renamed it to {new_name}!")
      time.sleep(1)
   

print(f">=<>=<>=<>=< FILE MANAGER <=<>=<>=<>=<")
time.sleep(1)

while True:
   print(f"\nWhat would you like to do?\n1. Read the file [r]\n2. Add something in the file [a]\n3. Write over the file [w]\n4. Create a new file [x]\n5. Delete a file [d]\n6. Rename a file [n]\n7. Quit [q]\n")
   time.sleep(1)
   select = input(">> ").lower()

   if select in ["r", "read", "1"]:
      enter = input("\nEnter a file name to read:\n>> ")
      reading(enter)
   
   elif select in ["a", "add", "append", "2"]:
      enter = input("\nEnter a file name:\n>> ")
      new = input("\nAdd something you want in the file:\n>> ")
      appending(enter, new)
   
   elif select in ["w", "write", "3"]:
      enter = input("\nEnter a file name to write over:\n>> ")
      new = input("\nWrite something you want in the file:\n>> ")
      writing(enter, new)
   
   elif select in ["x", "c", "create", "4"]:
      enter = input("\nEnter a name to create a new file:\n>> ")
      creating(enter)

   elif select in ["d", "delete", "5"]:
      enter = input("\nEnter a file name you want to delete:\n>> ")
      deleting(enter)
   
   elif select in ["n", "rename", "6"]:
      enter = input("\nEnter a file name to rename it:\n>> ")
      time.sleep(1)
      rename = input("\nEnter a new name for the file:\n>> ")
      renaming(enter, rename)

   elif select in ["q", "quit", "7"]:
      exit()
   
   elif select.strip() == "":
      print(f"\nNothing to select. Try using the available commands!")
      time.sleep(1)

   else:
      print(f"\nInvalid input. Try using the available commands!")
      time.sleep(1)