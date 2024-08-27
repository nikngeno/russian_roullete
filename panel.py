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

def mode_setup():
    print("Please select the difficulty rating:")
    print("1: Easy")
    print("2: Hard")
    print("3: Super Hard")
    mode_selection = int(input("Your choice: "))
    while mode_selection not in [1, 2, 3]:
        print("Invalid selection. Please enter a number between 1 and 3.")
        mode_selection = int(input("Your choice: "))
    return mode_selection

def health_setup(mode):
    health = 10
    if mode == 1:
        health -= 1
    elif mode == 2:
        health -= 2
    elif mode == 3:
        health -= 5
    return health

def drink():
    outcomes = {1: "poison", 2: "health booster", 3: "neutral"}
    effect = random.choice([1, 2, 3])
    print(f"The drink is: {outcomes[effect]}")
    return effect

def game_play():
    print_intro()
    print("Welcome to the Game!")
    print("A bartender has been serving you a drink night after night, and they") 
    print("invite you for a chance to play a Russian Roulette game for a chance to win a night of free drinks.")
    name = input("Enter your Name: ")
    print(f"{name}, do you wish to play the game?")
    choice = input("Type 'yes' or 'no': ").lower()

    if choice == "yes":
        mode = mode_setup()
        player_health = health_setup(mode)
        dealer_health = health_setup(mode)
        print(f"You have selected mode {mode}. Starting health: Player: {player_health}, Dealer: {dealer_health}")

        while True:
            effect = drink()
            if effect == 1:
                dealer_health -= 1
                print(f"Dealer's health decreased by 1. Current health: Dealer: {dealer_health}")
            elif effect == 2:
                print("Health booster has no effect as health is at maximum.")
            elif effect == 3:
                print("No effect on anyone's health.")

            dealer_health = max(dealer_health, 0)
            player_health = max(player_health, 0)

            if player_health <= 0:
                print("Game over! You have lost.")
                break
            elif dealer_health <= 0:
                print("Congratulations! You have won.")
                break

            continue_choice = input("Do you want to continue playing? (yes/no): ").lower()
            if continue_choice != "yes":
                break

        print("Thanks for playing!")

if __name__ == "__main__":
    game_play()
