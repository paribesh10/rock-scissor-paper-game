import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choice >= 3 or choice < 0:
  print("You typed an invalid number. You lose!")
else:  
  print(game_image[choice]) 
  choosen_thing = random.randint(0, 2)
  print("Computer chose:")
  print(game_image[choosen_thing])

  if choice == 0 and choosen_thing == 2:
    print("You Win!")
  elif choice == 1 and choosen_thing == 0:
    print ("You Win!")
  elif choice == 2 and choosen_thing == 1:
    print("You Win!")
  elif choice == choosen_thing:
    print("It's a draw!")
  else:
    print("You Lose!")


