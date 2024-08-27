import random
from drink import get_text_art
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
   mode_selection = int(input("Your Choice: "))
   while mode_selection not in [1, 2, 3]: #The only way we can get this to accept chars as invalid is to change mode_selection to non-int input,
       #This changes the whole codes iterability. we would have to type int(mode_selection) anytime it shows up in code.
       #Just keep this as is and hope somebody doesn't ask I guess.
       print("Invalid selection. Please enter a number between 1 and 3.")
       mode_selection = int(input("Your choice: "))
   return mode_selection




def health_setup(mode):#Condensed health since we already have health boosters
   health = 10
   if mode == 1:
       health -= 3
   elif mode == 2:
       health -= 5
   elif mode == 3:
       health -= 7
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



   while choice == "yes":
       mode = mode_setup()
       player_health = health_setup(mode)
       dealer_health = health_setup(mode)
       print(f"You have selected mode {mode}. Starting health: Player: {player_health}, Dealer: {dealer_health}")


       player_dmg = random.randint(0, 2)#Damage likelyhood, a one in three chance the player will take dmg vs dealer
       while mode == 1 or mode == 2: #Changed mode conditional statements
           effect = drink()
           if effect == 1:
               if player_dmg == 0:
                   player_health -= 1
                   print(f"Your health decreased by 1! Current health: {player_health}, \nDealer's current HP: {dealer_health}")
               else:
                   dealer_health -= 1
                   print(f"Dealer's health decreased by 1. Current dealer health: {dealer_health}, \nYour current HP: {player_health}")
           elif effect == 2:
               if player_health == health_setup(mode):
                   print("Health booster has no effect as health is at maximum.")
               else:
                   player_health += 1
                   print(f"Your health has increased! HP is now: {player_health} \nDealer's HP is now: {dealer_health}")
           elif effect == 3:
               print("No effect on anyone's health.")


       while mode == 3:
           effect = drink()
           player_dmg = random.randint(0,1) #Make it 50/50 odds for super hard mode!
           if effect == 1:
               if player_dmg == 0:
                   player_health -= 2
                   if player_health < 0:#Just to tidy up the values so they can't have negative HP
                       player_health = 0
                   print(f"Oh no!! You've lose 2 health! Current HP: {player_health}, \nDealers HP: {dealer_health}")
               else:
                   dealer_health -= 2
                   if dealer_health < 0:
                       dealer_health = 0
                   print(f"Dealers health has decreased by 2! Dealers health: {dealer_health}, \nYour current HP: {player_health}")
           elif effect == 2:
               if player_health == health_setup(mode):
                   print("Health booster has no effect as health is at maximum.")
               else:
                   player_health += 1
                   print(f"Your health has increased! HP is now: {player_health} \nDealer's HP is now: {dealer_health}")
           else:
               print("No effect on anyone's health.")


           dealer_health = max(dealer_health, 0)
           player_health = max(player_health, 0)




           if player_health <= 0:
               print("Game over! You have lost.")
               break
           elif dealer_health <= 0:
               print(f"Congrats {name}! You won! {get_text_art()}")
               break




           continue_choice = input("Do you want to continue playing? (yes/no): ").lower()
           if continue_choice == "no":
               random_bill = random.randint(100,3200)
               print(f"You have chosen not to continue, meaning your drinks are not on the house. \nHere's your bill {name}: $ {random_bill}")
               break
           elif continue_choice != "yes" and continue_choice != "no":
               print("Invalid option. Please try again.")
               break


       print("Thanks for playing!")
       break
   if choice == "no":
       print(f"Okay, {name}, you could have had a heck of a night with free drinks. Until next time!")




if __name__ == "__main__":
   game_play()


