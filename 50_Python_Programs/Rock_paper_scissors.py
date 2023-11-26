import random

choices = ['rock','paper','scissors']
computer_choices = random.choice(choices)
user_choice = input("Enter any one of them from rock paper and scissors :\n")

if user_choice == computer_choices:
    print("Tie")

elif (user_choice=='rock' and computer_choices=='scissor') or (user_choice=='paper' and computer_choices=='rock') or (user_choice=='scissor' and computer_choices=='paper'):
    print("You Win!")
    
else:
    print("Computer Wins!")
           
