import round_setup
import random
def print_intro():
    intro = """
      
██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║
██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║
██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║
██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║
╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗
██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░
██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░
██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗
╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝
    """
    print(intro)

# Call the function to display the intro
print_intro()

def game_play():
    
    #print_intro()

    print("Welcome to the Game!")
    print("A bartender has been serving you a drink night after night, and they") 
    print("invite you for a chance to play a Russian Roulette game for a chance to win a night of free drinks.")

    name = input("Enter your Name: ")
    
    print(f"{name}, do you wish to play the game?")
    choice = input("Type 'yes' or 'no': ").lower()

    if choice == "yes":
        select_mode = round_setup.mode_selection()
        print(f"You have selected {select_mode} mode.")

        # Example of a simple game loop
        while True:
            round_result = round_setup.round_setup()
            print(f"The drink is: {round_result}")
            continue_choice = input("Do you want to continue playing? (yes/no): ").lower()
            if continue_choice != "yes":
                break

        print("Thanks for playing!")

if __name__ == "__main__":
    game_play()