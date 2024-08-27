import random
#import game_play

def mode_setup():
    # Define the modes
    #Easy_Mode = "Easy"
    #Hard_Mode = "Hard"
    #Super_Hard_Mode = "Super Hard"

    # Prompt the user to select a mode
    mode_selection = int(input("Please select the difficulty rating (1: Easy, 2: Hard, 3: Super Hard): "))
    while mode_selection < 1 or mode_selection > 3:
            print("Invalid selection. Please enter a number between 1 and 3.")
            mode_selection = int(input("Please select the difficulty rating (1: Easy, 2: Hard, 3: Super Hard): "))
            if mode_selection == 1 or mode_selection == 2 or  mode_selection == 3:
                break
    return mode_selection

mode_setup()
    # Set initial values
def health_setup():
    """Set up player's starting health based on selected mode"""
    # Health is starting at a default value of 1o while damage start at 0
    health = 10
    damage = 0
    mode = mode_setup()
    if mode == 1:
        health += 1
        damage -= 1
    elif mode == 2:
        health += 2
        damage -= 2
    else:
        health += 5
        damage -= 5
    
def drink(self):
        # Define the possible outcomes as a dictionary
        outcomes = {
            1: "poison",
            2: "health booster",
            3: "neutral"
        }

        # Ask the player to select an effect
        print("Select an effect: 1 (poison), 2 (health booster), 3 (neutral)")
        selected_effect = int(input("Your choice: "))

        # Get the corresponding drink
        selected_drink = outcomes.get(selected_effect)
        if selected_drink is None:
            print("Invalid choice. No effect on your health.")
        else:
            # Apply the effects of the selected drink
            self.player_health += selected_effect
            if selected_effect < 0:
                print(f"You drank {selected_drink}! Your health is decreased by {-selected_effect}.")
            elif selected_effect > 0:
                print(f"You drank {selected_drink}! Your health is increased by {selected_effect}.")
            else:
                print("You drank a neutral drink. No effect on your health.")

        # Print the current health status
        print(f"Your current health is {self.player_health}.")
    # Return the selected mode and adjusted values
    #return selected_mode, Health, Damage

# Example usage
#selected_mode, health, damage = mode_setup()
#print(f"Selected mode: {selected_mode}, Health: {health}, Damage: {damage}")

# Start the game
#game_play.start_game(selected_mode, health, damage)