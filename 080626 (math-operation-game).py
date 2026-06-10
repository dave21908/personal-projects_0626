import random

def check_answer(guess, result): # Checking if the user's answer is correct or not
   if guess == result:
      print(f"\nCorrect!")
      return True
   else:
      print(f"\nIncorrect! The answer is {result}")
      return False

print(f">=<>=<>=<>=< OPERATION GAME >=<>=<>=<>=<")
game_start = input("Type 'start' to play the game!\n>> ").lower()

if game_start != "start":
   print(f"Understandable, bye!")
   exit()

else:
   # Initializing variables and difficulties settings
   score = 0
   correct = 0
   difficulties = {
      "easy": (7, 1, 5),
      "normal": (10, 2, 10),
      "hard": (15, 3, 30)
   }

   while True:
      diff_select = input("\nSelect difficulties: Easy (7q) / Normal (10q) / Hard (15q):\n>> ").lower()

      settings = difficulties.get(diff_select)
      if settings is None: # Checking if the user's input matches with difficulties key
         print(f"\nPlease type based on three difficulties, it could be either typos or just jumbled words.")
         continue
      max_q, low, high = settings # Unpacking the settings into variables
      
      for i in range(1, max_q + 1): # Looping through the questions
         num = random.randint(low, high)
         num2 = random.randint(low, high)

         # Operation logic and ensuring the results are not negative or decimal numbers
         op = random.choice(["+", "-", "*", "/"])
         if op == "+":
            result = num + num2
         elif op == "-":
            if num < num2: # Avoiding negative results
               num, num2 = num2, num
            result = num - num2
         elif op == "*":
            result = num * num2
         else:
            if num < num2:
               num, num2 = num2, num
            if num % num2 != 0:
               num = num2 * random.randint(1,10) # Ensuring the division results in an integer
            result = num // num2

         print(f"\nScore: {score} | Question {i}")
         print(f"{num} {op} {num2} = ?")
         guess = input(">> ")

         if guess.lower() in ["l", "leave"]:
            print(f"Leaving to menu...")
            break
         try:
            guess_num = int(guess)
            if check_answer(guess_num, result):
               score += 1
               correct += 1
         except ValueError:
            print(f"\nInvalid character, please answer using numbers!")
      
      print(f"\n{max_q} questions completed!\n\nTotal score: {score}\nCorrect guesses: {correct}\nIncorrect guesses: {max_q - correct}")
      replay = input("\nContinue playing? (y/n)\n>> ").lower()

      if replay not in ["y", "yes"]:
         print(f"Thank you for playing!")
         print(f"Exiting the game...")
         exit()
      else:
         score = 0
         correct = 0
         continue

"""
(Reflection 08/06/26) What went wrong during the process?
-  Missplaced function (placing `check_answer()` inside of loop)
-  Putting two random generated numbers outside the `for` loop, this makes numbers never change and become repetitive
-  Inconsistent variable naming (for example: `guess_num` and `guess`)
-  Lack of input validation for difficulty selection
-  Incorrect handling of division operation, leading to nonsensical fractions and decimal numbers
-  Mostly unreadable
"""