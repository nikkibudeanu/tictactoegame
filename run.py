# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
field = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
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

game_running()