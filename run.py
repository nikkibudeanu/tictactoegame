# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# imports
import random 

field = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
xoro = ["x", "o"]




# game name
def print_game_name():
  """
  Prints the game name
  """
print(
        """
         _ _ _   __     ____       _ _ _      __        ____         _ _ _    ____    _____
        |_   _| |  |  /   __|     |_   _|    /  \     /   __|       |_   _|  /    \  |  __ |
          | |   |  | (   /          | |     / /\ \   (   /            | |   |  __  | | |__
          | |   |  |  \  \__        | |    / ==== \   \  \__          | |   | |__| | | |__
          |_|   |__|   \____|       |_|   / /    \ \   \____|         |_|    \____/  |_____|
                            
        """
  )


# game field 
def print_field():
    """
    Print the field for the game and sets position for the items in the list.
    """
    print(" Game Field" + " "*9 + "Reference field")
    print(" " + field[1] + " | " + field[2] + " | " + field[3] + "  " +
          " "*10 + " " + "1" + " | " + "2" + " | " + "3" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + field[4] + " | " + field[5] + " | " + field[6] + "  " +
          " "*10 + " " + "4" + " | " + "5" + " | " + "6" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + field[7] + " | " + field[8] + " | " + field[9] + "  " +
          " "*10 + " " + "7" + " | " + "8" + " | " + "9" + "  ")
    print("\n")

def reset_field():
    """
    Reset field so the user is able to start a new game
    """
    field.clear()
    field.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

def quit_game():
    print("Thank you " + username + " for playing the game!")
    quit()

# username

def username():
    """
    Ask users to input their name.
    """
    global username
    print("What is your name?")
    username = input()
    game_running()

# main function
def game_running():
  """
  The main function
  """ 
  print_game_name()
  print("Hello " + username + "! Please select one of the following options.")
  print("1. Play our game")
  print("2. How to play")
  print("3. Print scores")
  print("Q. Quit game")
  
  # condition to loop through player inputs and go to the next menu
  while True:
    player_choice = input().strip().lower()
    if player_choice == "1":
      select_game()
    elif player_choice == "2":
      how_to_play()
    elif player_choice == "3":
      print_scores()
    elif player_choice == "q":
      quit_game()
    else: 
      print("Invalid input. Please select from the options above.")


# how to play
def how_to_play():
  """
  How to play the game.
  """
  print("1. You will play on the field composed by 3 by 3 squares")
  print("2. Select your symbol betweeen 'X' and 'O'.")
  print("3. Your opponent gets the other symbol once you pick one")
  print("4. Use the reference field to find out which number is asigned to the box you want to select.")
  print("5. The player who gets 3 of his symbols in a row is the winner.")
  print("6. If nobody has 3 marks in a row, the game is over and has no winners.")
  print("3. If you want to return to the main menu - enter 0. If you want to quit the game - enter 'q'")

  # condition to loop through user input
  while True:
    player_choice = input().strip().lower()
    if player_choice == "0":
      game_running()
    elif player_choice == "q":
      quit_game()
    else:
      print(" Incorrect input, please select '0' or 'q'.\n")

# select game with the computer or with a player
def select_game():
    """
    Enables user to play against computer or another player. 
    """
    print("Select which type of game would you like to play: ")
    print("1. Play the game against the computer. ")
    print("2. 2 player game. ")
    print("Q. Quit game. ")
    # loops through user input
    while True:
        player_game_choice = input().strip().lower()
        global game_level
        if player_game_choice == "1":
            game_level = 1
            play_game()
        elif player_game_choice == "2":
            game_level = 2
            play_game()
        elif player_game_choice == "q":
            quit_game()
        else: 
            print("Invalid input, please select '1' to play against the computer, '2' to play a 2 player game or 'q' to quit the game")

def champion(field, username):
  """
  Function to determine who has won the game. returns True or False.
  """
  if (field[1] == username and field[2] == username and field[3] == username) or \
     (field[4] == username and field[5] == username and field[6] == username) or \
     (field[7] == username and field[8] == username and field[9] == username) or \
     (field[1] == username and field[4] == username and field[7] == username) or \
     (field[2] == username and field[5] == username and field[8] == username) or \
     (field[3] == username and field[6] == username and field[9] == username) or \
     (field[1] == username and field[5] == username and field[9] == username) or \
     (field[3] == username and field[5] == username and field[7] == username):
    return True
  else:
    return False

def draw(field):
  """
  Function to check if there are any squares left.Returns false if there are more than 1 square left
  and true if not(game ends with no winners).
  """
  if field.count(" ") > 1:
    return False
  else:
    return True


def computer_choice(field, opponent_symbol_choice):
    """
    Loops to get a random computer choice within the field. 
    Checks if the choice is an empty string within the list and place the symbol.
    Break the loop.
    """
    while True:
        # randint method learnt on  https://www.w3schools.com/python/ref_random_randint.asp
        computer_choice = random.randint(1, 9)
        if field[computer_choice] == " ":
            return computer_choice

def play_game():
    """
    The main game function that gets executed after all previous options
    gets put through.
    """
    # Let's user select the symbol he/she wants to play as. Either 'X'
    # or 'O'. Prints out to user message that wrong symbol has been
    # chosen, if so restarts the game.
    print(f"Do you want to play as  '{xoro[0]}' or  '{xoro[1]}?' \n")
    player_symbol_choice = input().lower().strip()
    if player_symbol_choice == xoro[0]:
        opponent_symbol_choice = xoro[1]
    elif player_symbol_choice == xoro[1]:
        opponent_symbol_choice = xoro[0]
    elif player_symbol_choice == "q":
        quit_game()
    else:
        print("Invalid input, please use either 'X' or 'O'.\n")
        print("If you want to quit the game, type 'Q'.")
        play_game()
    # The main game loop
    while True:
        print_field()
        # The main player loop that loops through input.
        while True:
            # Loops through until correct input from user has been
            # given. Checks if the space is taken and prints out message
            # to user if the input or space is taken.
            try:
                choice = int(input(f"Please choose an empty space for "
                                   f"your next move as '{player_symbol_choice}'. \n"))
                if choice in range(1, 10):
                    if field[choice] == " ":
                        field[choice] = player_symbol_choice
                        break
                    else:
                        print("Please select an empty square!")
                else:
                    print("Invalid input. Please use the numbers "
                          "between 1-9.\n")
            except ValueError:
                print("Please enter a valid number!")

        # Checks if player has won the game. Two different print outputs
        # depending on the game that has been selected.
        if champion(field, player_symbol_choice):
            print_field()
            if game_level == 1:
                print("You win! Congratulations")
                return_to_main_page()
            elif game_level == 2:
                print("Player one wins! Congratulations")
                return_to_main_page()
            else:
                return None

        print_field()
        # Checks if the grid is full. If yes then prints out message and
        # calls function return_to_menu to let user choose if he wants
        # to quit the script or go back to menu.
        if draw(field):
            print("2 winners! It's a draw!")
            return_to_main_page()

        # Check if the game level is vs computer. If yes then generates
        # a random computer move and sets that grid to computers symbol.
        if game_level == 1:
            choice = computer_choice(field, opponent_symbol_choice)
            field[choice] = opponent_symbol_choice

            # Checks for computer win same as previously for player.
            if champion(field, opponent_symbol_choice):
                print_field()
                print("Computer wins!")
                return_to_main_page()

            # Checks for a draw as the player above.
            if draw(field):
                print("2 winners! It's a draw!")
                return_to_main_page()

        # Checks if the game level is against another player.
        if game_level == 2:
            # Main 2nd player loop that asks for a grid input to place
            # correct symbol onto grid. Same function as the main player
            while True:
                try:
                    choice = int(input(f"Player TWO, please choose an empty "
                                       f"square for your next move as "
                                       f"'{opponent_symbol_choice}'.\n"))
                    if choice in range(1, 10):
                        if field[choice] == " ":
                            field[choice] = opponent_symbol_choice
                            break
                        else:
                            print("Please select an empty square!")
                    else:
                        print("Invalid input. Please use the numbers "
                              "between 1-9.\n")
                except ValueError:
                    print("Invalid input. Please enter a valid input")

            # Checks for 2nd player win.
            if champion(field, opponent_symbol_choice):
                print_field()
                print(f"Player two '{opponent_symbol}' wins! Congratulations")
                return_to_main_page()

            print_field()

            # Checks for a draw.
            if draw(field):
                print("2 winners! It's a draw!")
                return_to_main_page()

def return_to_main_page():
  """
  User has to select to go back to the main page or quit the game.
  """
  print("Would you like to play again?")
  print("Select '1' if yes or 'q' if you would like to quit the game. \n ")
  while True:
    player_choice = input().strip()
    if player_choice == "1":
      reset_field()
      game_running()
    elif player_choice == "q":
      quit_game()
    else:
      print("Invalid input!Please try again!")

username()