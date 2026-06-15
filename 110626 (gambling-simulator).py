import random, time

def gambling(money, bet, bonus_used, multiplier, chance):
   if money == 0:
      if bonus_used:
         print("\nSorry, son, but you've already received your bonus. You can't gamble anymore.")
         print("\n>=<>=<>=<>=< GAME OVER >=<>=<>=<>=<")
         exit()
      print(f"\nGoodness, son, you've run out of money. Here's a $100 bonus for ya. Carry on, son.")
      money += 100
      bonus_used = True
   
   else:
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
   while True:
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
GAME START
   Importing libraries
   Defining the gambling function()
      If the player has no money, give them a $100 bonus (one time only)
         If the player has no money and has already received the bonus, print a message that they can't gamble anymore
         GAME END
      Else if the bet is not a digit, print an error message
      Else if the bet is greater than the player's money, print an error message
      Else, deduct the bet from the player's money
         Generate a random chance for winning
         If the chance is greater than 0.5, the player wins
            Deduct one pull from the player's pulls
            Calculate the earnings and add it to the player's money
            If the player has no pulls left, print a message
            Else, print a congratulatory message with the player's current money
         Else, print a message that the player lost and show their current money
   Printing the game title
   Initializing game variables
   Asking the player if they want to start gambling
   If the player doesn't want to start, exit the game
   If the player wants to start, enter the game loop
      Generate a random chance for winning
      Ask the player to select an action (gamble, shop, or leave)
      If the player selects gamble:
         Ask the player to place a bet
         Call the gambling function with the player's money and bet
      Else if the player selects shop:
         Display the shop items and their prices
         Ask the player to select an item to purchase
         If the player has enough money, deduct the cost and provide the item
         Else, print a message that the player doesn't have enough money
      Else if the player selects leave:
         Exit the game loop
      Else, print an error message for invalid action
GAME END
"""