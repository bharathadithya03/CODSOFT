#task2 (rock,paper,scissor)

import random
rock = 0
paper = 1
scissor = 2

game=[rock,paper,scissor]
while True:
    user_choice=int(input("Choose 0 for Rock,Choose 1 for Paper,Choose 2 for Scissor :"))
    if user_choice >= 3 or user_choice < 0:
        print("Invalid Choice")
    else:
        print(game[user_choice])
        computer_choice=random.randint(0,2)
        print(game[computer_choice])
        print("Computer_choice:",computer_choice)
        if computer_choice == user_choice:
            print("it's draw")
        elif computer_choice == 2 and user_choice == 0:
            print("You win")
        elif computer_choice == 0 and user_choice == 2:
            print("computer win")
        elif computer_choice > user_choice :
            print("Computer win")
        elif computer_choice < user_choice :
            print("You win")
        Play_again=input("Play again?(y/n)")
        if Play_again.lower() != "y":
            print("Exit")
            break