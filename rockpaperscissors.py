import random

print('Welcome to Rock, Paper, Scissors!') 

def play():
    user = input("Enter 'r' for rock 'p' for paper 's' for scissors: ")
    user_choice = user.lower()

    computer = random.choice(["r", "p", "s"])

    print("You chose " + user_choice + " and the computer chose " + computer )

    if user_choice == computer:
        print("You tied")
    elif user_choice == "r":
        if computer == "s":
            print("You win")
        else:
            print("You lose")
    elif user_choice == "p":
        if computer == "r":
            print("You win")
        else:
            print("You lose")
    elif user_choice == "s":
        if computer == "p":
            print("You win")
        else:
            print("You lose")
    menu()

def menu():
    
    while True:
        play_again = input("Enter 1 to play again and 2 to exit: ")
        if play_again == "1":
            play()
        elif play_again == "2":
            exit()
        else:
            print("Not a valid option, choose again.")

play()