# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
field = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
xoro = ["x", "o"]
winner = None
play_game = True


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
def print_field(field):
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

def quit_game():
    print("Thank you" + username + "for playing the game!")
    quit()

# username
def username():
    """
    Ask users to input their name.
    """
    print("What is your name?")
    username = input()

# main function
def game_running():
  """
  The main function
  """ 
  print_game_name()
  print("Please select one of the following options.")
  print("1. Play our game")
  print("2. How to play")
  print("3. Print scores")
  print("Q. Quit game")
  
  # condition to loop through player inputs and go to the next menu
  while True:
    player_choice = input().strip().lower()
    if player_choice == "1":
      which_game()
    elif player_choice == "2":
      how_to_play()
    elif player_choice == "3":
      print_scores()
    elif player_choice == "q":
      quit()


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
      main()
    elif player_choice == "q":
      quit()
    else:
      print(" Incorrect input, please select '0' or 'q'.\n")

def play_game():
    """
    The main game function 
    """
    # User selects the prefered symbol : "X" or "O". 
    # Let the user know which symbol he selected.
    # Restart game if the user wants to change the symbol.
    print("Which symbol do you prefer, " + xoro[0] + " or " + xoro[1]+ " ? \n ")
    player_symbol_choice =  input().lower().strip()
    if player_symbol_choice == xoro[0]:
        player2_symbol_choice == xoro[1]
    elif player_symbol_choice == xoro[1]:
        player2_symbol_choice == xoro[0]
    elif player2_symbol_choice == "q":
        quit_game()
    else:
        print("Invalid input! Please select either 'X' or 'O'. \n")
        print("To quit the game, select 'Q' .")
        play_game()


play_game()