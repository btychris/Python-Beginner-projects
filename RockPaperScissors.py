import random


def computer_option():
    return random.choice(["Rock", "Paper", "Scissors"])


def user_option():
    user_choice = input("Rock\nPaper\nScissors\n")
    print("Type '1' to stop")
    return user_choice

    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Please pick an option")
        user_choice = input("Rock\nPaper\nScissors\n")
        continue


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = user_option()
        computer_choice = computer_option()

        if user_choice == computer_choice:
            print("It's a draw")
            print(f"User Choice: {user_choice}")
            print(f"Computer Choice: {computer_choice}")
            user_score += 1
            computer_score += 1
        elif ((user_choice == "Rock" and computer_choice == "Scissors") or
              (user_choice == "Paper" and computer_choice == "Rock") or
              (user_choice == "Scissors" and computer_choice == "Paper")):
            print("You win")
            print(f"User Choice: {user_choice}")
            print(f"Computer Choice: {computer_choice}")
            user_score += 3
            continue
        else:
            print("You lose")
            print(f"User Choice: {user_choice}")
            print(f"Computer Choice: {computer_choice}")
            computer_score += 3

        if user_choice == "1":
            print(f"User_Score: {user_score}")
            print(f"Computer Score: {computer_score}")
        if user_score > computer_score:
            print("You win")
        elif user_score == computer_score:
            print("You drew")
        else:
            print("You lost")
            break


if __name__ == "__main__":
    main()
