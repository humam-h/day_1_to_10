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

#Write your code below this line 👇
print("Welcome to rock paper Scissors game !")
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
choice_list = [rock, paper, scissors]
my_seliction = choice_list[my_choice]
computer_seliction = choice_list[computer_choice]
print(f" You choose:\n {my_seliction}\n and the computer choose:\n {computer_seliction}\n")
if my_choice == 0 and computer_choice == 2:
    print("you win!")
elif my_choice == 0 and computer_choice == 1:
    print("you lose")
elif my_choice == 1 and computer_choice == 0:
    print("you win!")
elif my_choice == 1 and computer_choice == 2:
    print("you lose")
elif my_choice == 2 and computer_choice == 0:
    print("you lose!")
elif my_choice == 2 and computer_choice == 1:
    print("you win")
elif my_choice == computer_choice:
    print("It's a drow! play agin")
else:
    print(" you have entered a wrong number! play agin")
