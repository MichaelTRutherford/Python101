import random
# random
# while
# input
# print formatting
# comparison operators
# break and continue

lst = ["Rock", "Paper", "Scissors"]

while True:
    print("Rock, Paper or Scissors? (Quit to Quit)")
    choice = input("What is your choice? ")
    choice = choice.lower()
    computer_choice = random.choice(lst)
    computer_choice = computer_choice.lower()
    print(f"Computer chose {computer_choice}")
    
    if choice != "rock" and choice != "paper" and choice.lower != "scissors" and choice != "cancel":
        print("Please choose a correct answer")
    if choice == "quit":
        break
    elif choice == computer_choice: 
        print("You tied")
    elif choice == "rock" and computer_choice == "scissors":
        print("You win")
        break;
    elif choice == "paper" and computer_choice == "rock":
        print("You win")
        break;
    elif choice == "scissors" and computer_choice == "paper":
        print("You win")
        break
    else:
        print("You lose. Try again!")
