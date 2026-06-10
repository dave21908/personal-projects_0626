import os

def validate(f_name, must_exist=True): # Validating the file name based on specific conditions
   try:
      if f_name.strip() == "":
         print("\nIt's empty. Atleast type something.")
         return False
      elif chars := set(r'<>:"/\|?*') & set(f_name):
         print(f"\nThe file name cannot contain the following characters: {', '.join(chars)}")
         return False
      elif must_exist and not os.path.exists(f_name):
         print(f"\nThe file '{f_name}' does not exist.")
         return False
      elif not must_exist and os.path.exists(f_name):
         print(f"\nThe file '{f_name}' already exists.")
         return False
      elif not os.path.isfile(f_name):
         print(f"\n'{f_name}' is not a file.")
         return False
      elif must_exist and not os.access(f_name, os.R_OK):
         print(f"\nYou do not have permission to read '{f_name}'.")
         return False
      else:
         return True
   except Exception as e:
      print(f"\nThere is an error occurred: {e}")

def reading(f_name): # Reading the file and printing its content
   if not validate(f_name, must_exist=True):
      return
   else:
      with open(f_name, "r") as file:
         print(f"\n{file.read()}")

def appending(f_name, new): # Appending content to a file
   if not validate(f_name, must_exist=True):
      return
   else:
      file = open(f_name, "a")
      file.write(f"\n{new}")
      file.close()
      print(f"\nSuccessfully added '{new}' to {f_name}!")

def writing(f_name, new): # Writing content to a file
   if not validate(f_name, must_exist=False):
      return
   else:
      file = open(f_name, "w")
      file.write(new)
      file.close()
      print(f"\nSuccessfully wrote '{new}' to {f_name}!")

def creating(f_name): # Creating a new file
   if not validate(f_name, must_exist=False):
      return
   else:
      file = open(f_name, "x")
      print(f"\n{f_name} created successfully!")
      file.close()

def deleting(f_name): # Deleting a file
   if not validate(f_name, must_exist=True):
      return
   else:
      os.remove(f_name)
      print(f"\n{f_name} has been deleted successfully!")

def renaming(old_name, new_name): # Renaming a file
   if not validate(old_name, must_exist=True):
      return
   elif not validate(new_name, must_exist=False):
      return
   elif new_name.strip() == "":
      print("\nNothing to rename to.")
   else:
      os.rename(old_name, new_name)
      print(f"\nSuccessfully renamed it to {new_name}!")

print(f">=<>=<>=<>=< FILE MANAGER <=<>=<>=<>=<")
COMMANDS = {
   ("r", "read", "1"): reading,
   ("a", "add", "append", "2"): appending,
   ("w", "write", "3"): writing,
   ("x", "c", "create", "4"): creating,
   ("d", "delete", "5"): deleting,
   ("n", "rename", "6"): renaming,
   ("q", "quit", "7"): exit()
}

while True:
   print(f"\nWhat would you like to do?\n1. Read the file [r]\n2. Add something in the file [a]\n3. Write over the file [w]\n4. Create a new file [x]\n5. Delete a file [d]\n6. Rename a file [n]\n7. Quit [q]\n")
   select = input(">> ").lower()

   for keys, action in COMMANDS.items(): # Checking if the user's input matches with the command keys
      if select in keys:
         if action == reading or action == deleting:
            f_name = input("\nType the file name:\n>> ")
            action(f_name)
         elif action == appending or action == writing:
            f_name = input("\nType the file name:\n>> ")
            new = input("Type the content you want to add/write:\n>> ")
            action(f_name, new)
         elif action == creating:
            f_name = input("\nType the file name:\n>> ")
            action(f_name)
         elif action == renaming:
            old_name = input("\nType the current file name:\n>> ")
            new_name = input("Type the new file name:\n>> ")
            action(old_name, new_name)
         else:
            action()
         break
      elif not select.strip():
         print(f"\nNothing to select. Try using the available commands!")
      else:
         print(f"\nInvalid input. Try using the available commands!")

"""
(Reflection 09/06/26) What went wrong during the process?
-  Forgot to switch `
-  Error in handling file (such as trying to read a non-existent file, or trying to create a file that already exists)
-  
"""