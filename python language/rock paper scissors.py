import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
player_choice = input("your choice (rock, paper, scissors): ").lower().strip()
print(f"computer choice is {computer_choice}")
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
       


