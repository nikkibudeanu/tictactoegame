# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# imports
import random 

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

def reset_field():
    """
    Reset field so the user is able to start a new game
    """
    field.clear()
    field.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

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
            play_game
        elif player_game_choice == "2":
            game_level = 2
            play_game()
        elif player_game_choice == "q":
            quit_game()
        else: 
            print("Invalid input, please select '1' to play against the computer, '2' to play a 2 player game or 'q' to quit the game")

def computer_choice(field, player2_symbol_choice):
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

    # game loop 
    while True:
        print_field()
        # loops through user input for selecting squares
        while True:
            # loops throgh user inputs
            # check if the square is taken and if the input is valid
            # give feedback to the user if the input is not valid
            # give feedbck to the user if the square is taken
            try:
              choice = int(input("Please select an empty square for your next move as" + player_symbol_choice + ". \n"))
              if choice in range(1,10):
                    if field[choice] == " ":
                        field[choice] = player_symbol_choice
                        break
                    else:
                        print("Unfortunately, that space is taken! ")
                else:
                    print("Invalid input. Please select a number between 1-9. \n")
            except ValueError:
                print("Please enter a valid number!")
    # check who has won the game
    if winner(field, player_symbol_choice):
      print_field()
      if game_level == 1:
        print("Congratulations! You win!")
        return_to_main_page()
      elif game_level == 2:
        print("Congratulations! Player one wins! ")
        return_to_main_page()
      else: 
        return None
    print_field()
    # draw method learnt here - https://www.geeksforgeeks.org/wand-drawing-function-in-python/
    # function to check if the frid is full
    if draw(field):
      print("Oops! 2 winners! It's a draw!")
      return_to_main_page()
   # check the game type and is vs computer, generate a random move.
    if game_level == 1:
      choice = computer_choice(field, player2_symbol_choice)
      field[choice] = player2_symbol_choice

      # check if winner 
      if winner(field, player2_symbol_choice):
        print_field()
        print("Computer is the winner!")
        return_to_main_page()

      # check if draw 
      if draw(field):
        print("Oops! 2 winners! It's a draw!")
        return_to_main_page()
    # check if the game type is vs another player
    if game_level == 2:
      # loop that asks for a symbol input.
      while True:
        try:
          choice = int(input("Player TWO, please select an empty square for yout next move as" + player2_symbol_choice))
          if choice in range(1,10):
            if field[choice] == " ":
              field[choice] = player_symbol_choice
              break
            else:
              print("Unfortunately, that space is taken! ") 
          else:
            print("Invalid input. Please select a number between 1-9. \n")
      except ValueError:
        print("Please enter a valid number!")

         # check is the 2nd player has won
        if winner(field, player2_symbol_choice):
           print_field()
           print("Congratulations! Player two" + player2_symbol_choice + "wins! ")
           return_to_main_page()
        print_field()

        # check if draw
        if draw(field):
          print("Oops! 2 winners! It's a draw!")
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
play_game()