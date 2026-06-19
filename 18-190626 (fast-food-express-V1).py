def quiting():
   print(f"Your total orders: {order}\nYour total cost: ${total_spent}")
   exit()

def browsing():
   print("\n=-=-=-=[ MENU ]=-=-=-=")
   for key, item in menu.items():
      print(f"{key}: {item['name']} (${item['price']})")
   print("\n=-=-=-=[ COMMANDS ]=-=-=-=")
   for key, command in commands.items():
      print(f"{key}: {command['name']}")

def ordering(serve, money, order, total_spent):
   if serve not in menu:
      print(f"\nSorry, we don't have {serve} on the menu.")
      return money, order, total_spent
   
   item = menu[serve]
   if money < item["price"]:
      print(f"\nSorry, you can't afford {item['name']}. Try order something cheaper.")
   else:
      money -= item["price"]
      total_spent += item["price"]
      order += 1
      print(f"\nYour order of {item['name']} costs ${item['price']}.")
   return money, order, total_spent

def find_by_name(user_input, dictionary):
   for key, item in dictionary.items():
      if user_input.lower() == item["name"].lower():
         return key
   return None

# Variables and Tuples
money = 100
order = 0
total_spent = 0
menu = {
   "1": {"name": "Water", "price": 1.25},
   "2": {"name": "Soda", "price": 2},
   "3": {"name": "French Fries", "price": 3.50},
   "4": {"name": "Burger", "price": 4.50},
   "5": {"name": "Pizza", "price": 7},
   "6": {"name": "Onion Ring", "price": 4.25},
   "7": {"name": "Fish n' Chips", "price": 5},
   "8": {"name": "Vegan Salad", "price": 4.75}
}
commands = {
   "B": {"name": "Browse", "execute": "browse"},
   "T": {"name": "Gain Money", "execute": "transfer"},
   "Q": {"name": "Quit", "execute": "exit"}
}

# =-=-= Main Program =-=-=
print(">=<>=<>=<>=< FAST FOOD EXPRESS >=<>=<>=<>=<")
serve = input("Welcome! What would you like to order?\n(Type `B` to browse menu and commands)\n>> ").strip()

while True:
   if serve not in menu and serve not in commands:
      matched_key = find_by_name(serve, menu) or find_by_name(serve, commands)
      if matched_key:
         serve = matched_key
   
   if serve in commands:
      choice = commands[serve]
      if choice["execute"] == "exit":
         print("\nThank you for visiting us!")
         quiting()
         break
      elif choice["execute"] == "browse":
         browsing()
      elif choice["execute"] == "transfer":
         money += 100
         print(f"\nSuccessfully transfered $100 to your money.\nYour money: {money}")
   else:
      money, order, total_spent = ordering(serve, money, order, total_spent)

   serve = input(f"\nYour money: ${money}\nAnything else you would like to order?\n>> ").strip()

   

"""
Reflection (18-19/06/2026) What went wrong during the process?
- 
"""