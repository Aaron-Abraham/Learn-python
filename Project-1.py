#Project-1
#Rock, paper, scissor game with the computer

import random
#Notes:
#1-Rock ; 2-Paper; 3-Scissor

user_choice=int(input("Enter your choice: \n1.Rock \n2.Paper \n3.Scissor\n-"))
comp_choice=random.randint(1,3)
print("Computer chose:",comp_choice)
if user_choice==comp_choice:
    print('It is a tie')
elif user_choice==1 and comp_choice==3:
    print("You won, computer lost")
elif comp_choice==1 and user_choice==3:
    print("Computer won, you lost")
elif user_choice>comp_choice:
    print("You win, computer lost")
elif comp_choice>user_choice:
    print("You lose, computer won")