Came up with list of the game flow algorithm, lemme know if this makes sense
Round Setup Algorithm:
    Randomly select a drink to contain the health booster and the other to contain poison.
    Assign the drinks to the dealer and the player.

Player Action Algorithm:
    Display the drinks to the player.
    Allow the player to select a drink to offer to the dealer.

Dealer Reaction Algorithm:
    Check the selected drink.
    If it's poison, reduce the dealer's health by a certain amount.
    If it's the health booster:
      Check if the dealer's health is at maximum capacity.
      If it is, ask the dealer if they want to take the drink.
      If they do, do nothing; if they don't, do nothing.
    Update the dealer's health status.

Dealer Action Algorithm:
    Randomly select a drink to offer to the player.
    Display the drink to the player.
    Allow the player to choose whether to accept the drink or not.


Player Reaction Algorithm (Updated):
    If the player accepts the drink, check its contents.
    If it's poison, reduce the player's health by a certain amount.
    If it's the health booster:
        Check if the player's health is at maximum capacity.
        If it is, ask the player if they want to take the drink.
        If they do, do nothing; if they don't, do nothing.
    Update the player's health status.

Game Loop Algorithm:
    Include the dealer's offer and the player's reaction as part of each round in the game loop.

Win/Lose Condition Algorithm:
    Check if the player or the dealer's health has reached zero.
    Declare the winner based on the remaining health points.
