import count as countgame
import space_invaders as spacegame

def main():
    # offer choice for the user 
    print("Welcome to Game Selection!")
    print("Which game would you like to play?")
    print("1. Space Invaders")
    print("2. Count Game")
    choice = input("Enter the number of the game you want to play: ")

    # depending on selection --> present certain game 
    if choice == "1":
        print("Welcome to Space Invaders Game!")
        spacegame.run_space_game()
    elif choice == "2":
        print("Welcome to Count Game!")
        countgame.run_count_game()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
