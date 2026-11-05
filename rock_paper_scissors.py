import random

print("Welcome to Rock, Paper, Scissors!")

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("\nThanks for playing!")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        continue

    player = choices[int(choice) - 1]
    computer = random.choice(choices)

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"\nScore: You {player_score} - {computer_score} Computer")