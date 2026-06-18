import random

def gambling(money, bet, bonus_used, multiplier, chance):
   # Resolve a single gamble round and handle the emergency bonus condition
   if money == 0:
      if bonus_used:
         print("\nSorry, son, but you've already received your bonus. You can't gamble anymore.")
         print("\n>=<>=<>=<>=< GAME OVER >=<>=<>=<>=<")
         exit()
      print(f"\nGoodness, son, you've run out of money. Here's a $100 bonus for ya. Carry on, son.")
      money += 100
      bonus_used = True # Set to true one-time only, so it will check if the bonus has been used
   
   else:
      # Winning condition: chance under threshold gives a payout
      if chance <= 0.5:
         earn = round((bet * random.randint(1,5)) * multiplier)
         money += earn
         print(f"\nCongratulations, my son! You've won ${earn}!\nYour total money: ${money}")
      else:
         print(f"\nSorry, son, better luck next time.\nYou have ${money} left.")
   return money, bonus_used
      
print("\n>=<>=<>=<>=< GAMBLING SIMULATOR >=<>=<>=<>=<")
start = input("Do you want to gamble, son? (yes/no)\n>> ")

if start not in ["yes", "y"]:
   print("\nAlright, then...")
   exit()

else:
   bonus_used = False
   money = 100
   total_bets = 0
   pulls = 5
   luck_boost = 0
   earn_multiplier = 1
   SHOP = {
      "1": {"name": "Pull Pack", "price": 50, "effect": "pulls"},
      "2": {"name": "Golden Ledger", "price": 75, "effect": "multiplier"},
      "3": {"name": "Lucky Charm", "price": 100, "effect": "chance"},
      "4": {"name": "Leave Shop", "price": 0, "effect": "exit"}
   }
   
   while True: # Main loop for choosing actions until the player leaves
      chance = random.random() - luck_boost
      print(f"\n=-=[ 💰 ${money}  |  🎟 {pulls} pulls ]=-=")
      action = input("Select your action:\n1) Take a gamble\n2) Go to Shop\n3) Leave\n>> ")
      if action in ["1", "gamble"]:
         try:
            if pulls == 0:
               print("\nSorry, son, but you've run out of pulls. You can buy more at the shop.")
               continue
            bet = int(input(f"\nPlace your bet, son. You have ${money} and [{pulls}] pulls left, use it carefully.\n>> $"))
            if bet <= 0:
               print("Make sure your bet is more than nothing, son.")
               continue
            elif bet > money:
               print("\nYou're overbetting your money, son. Try lowering your stake to something more reasonable.")
               continue
            else:
               # Deduct the bet and consume one pull before resolving the gamble
               money -= bet
               total_bets += 1
               pulls -= 1
               money, bonus_used = gambling(money, bet, bonus_used, earn_multiplier, chance)
         except:
            print("\nInvalid input, my son. Please type the amount of bet in number.")
            continue

      elif action in ["2", "shop"]:
         print("\n=-=-=[ SHOP ]=-=-=")
         for key, item in SHOP.items():
            print(f"{key}) {item['name']} (${item['price']})") if key != "4" else print(f"{key}) {item['name']}")
         item = input(f"\n💰 ${money}\nSelect an item you want to buy:\n>> ").strip().strip('"').strip("'")
         if item not in SHOP:
            print("\nInvalid item, son. Please select a valid item from the shop.")
         else:
            choice = SHOP[item]
            if choice["effect"] == "exit":
               continue
            elif money < choice["price"]:
               print("Sorry, son, you don't have enough money to buy this.")
            else:
               # Apply the purchased item effect to the player's resources
               if choice["effect"] == "pulls":
                  pulls += 5
                  print(f"\n(Add +5 more pulls)\nYour pulls: {pulls}")
               elif choice["effect"] == "multiplier":
                  earn_multiplier *= 1.25
                  print(f"\n(Increase 25% of win earnings)")
               elif choice["effect"] == "chance":
                  luck_boost = min(luck_boost + 0.1, 0.9)
                  print("\n(Increase the chance by 10%)")

               money -= choice["price"]
               print(f"You successfully bought {choice['name']}!")

      elif action in ["3", "leave"]:
         print("\nFarewell, son. Hope to see you again!")
         break

      else:
         print("\nInvalid action, son. Please select a valid action.")

   print(f"You walked away with ${money} after {total_bets} bets.")
   exit()
   
"""
(Reflection 11-15/06/26) What went wrong during the process?
-  Several logic bugs (for example: Deduction failure, bet `input()` prompt appeared before the pulls check,  )
-  Return the wrong kind of value inside of `gambling()` function
-  Inconsistent variables usage, causing `NameError`
-  chance `random()` (random-generated decimal numbers from 0 to 1) was recalculated before the loop, causing it to remain in program without generating again for each loop
-  `int(input())` was left unguarded, meaning that if the user types anything other than a number (zero or negative numbers, n <= 0), the program will crash with a ValueError
-  Totally unreadable
"""