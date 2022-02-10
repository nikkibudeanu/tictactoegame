# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# imports
import random 
import gspread 
from google.oauth2.service_account import Credentials


# Google scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tictactoe')

data = SHEET.worksheet('game')



# variables to push data to the spreadsheet
count_games = 0
count_win = 0
count_lose = 0
count_draw = 0 
count_x = 0
count_o = 0

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
    global new_col_number
    print("What is your name?")
    username = input()
    new_col_number = len(data.col_values(1)) + 1
    data.update_cell(new_col_number, 1, username)
    game_running()

# function to count wins
def count_wins():
  """
  Update the spreadsheet win column with number of wins of each user.
  """
  global count_win
  count_win += 1
  data.update_cell(new_col_number, 3, count_win)
  count_total_games()

# function to count draw games
def count_draws():
  """
  Update the spreadsheet draw column with number of draws of the user. 
  """
  global count_draw
  count_draw += 1
  data.update_cell(new_col_number, 2, count_draw)
  count_total_games()

# function to count lost games
def count_loses():
  """
  Update the spreadsheet loss column with the number of losses for each user.
  """
  global count_lose
  count_lose += 1
  data.update_cell(new_col_number, 4, count_lose)
  count_total_games()


# function to count the number of games of each user
def count_total_games():
  """
  Counts the amount of games played by each user and updates the google sheet. 
  """
  global count_games
  count_games = count_win + count_draw + count_lose
  data.update_cell(new_col_number, 5, count_games)

# times played as x
def count_x_games():
  """
  Counts the amount of games played by the user as 'x'.
  """
  global count_x
  if player_symbol_choice == xoro[0]:
    count_x += 1
    data.update_cell(new_col_number, 6, count_x)


# times played as o


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

# function to print scores
def print_scores():
  """
  Function to print out user's score.
  """
  print("Here is your score: ")
  print("You have played " + str(count_games) + " times!")
  print("You have won " + str(count_win) + " times!")
  print("Draw games: " + str(count_draw))
  print("You have lost " + str(count_lose) + " times!")
  print("If you want to return to the main menu, enter '0'. To quit the game, enter 'q'")

  # loop to quit or return to the main menu depending on user input
  while True:
    player_choice = input().strip().lower()
    if player_choice == "0":
      game_running()
    elif player_choice == "q":
      quit_game()
    else:
      print("Invalid input, please select '0' or 'q'!")
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
    global player_symbol_choice
    player_symbol_choice = input().lower().strip()
    if player_symbol_choice == xoro[0]:
        opponent_symbol_choice = xoro[1]
        count_x_games()
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
        # loop for the main player input
        while True:
            # function to add input and check if the square is empty and if the input is valid.
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

        # condition to check if the user won : two different feedback messages depending on the game type.
        if champion(field, player_symbol_choice):
            print_field()
            count_wins()
            if game_level == 1:
                print("You win! Congratulations")
                return_to_main_page()
            elif game_level == 2:
                print("Player one wins! Congratulations")
                return_to_main_page()
            else:
                return None

        print_field()
        # condition to check if the grid is full to declare no winners.
        if draw(field):
            count_draws()
            print("2 winners! It's a draw!")
            return_to_main_page()

        # condition to check if the game type is against the computer.
        if game_level == 1:
            choice = computer_choice(field, opponent_symbol_choice)
            field[choice] = opponent_symbol_choice

            # condition to check if the computer wins
            if champion(field, opponent_symbol_choice):
                count_loses()
                print_field()
                print("Computer wins!")
                return_to_main_page()

            # condition to check if it's a draw.
            if draw(field):
                count_draws()
                print("2 winners! It's a draw!")
                return_to_main_page()

        # condition to check if the game type is against a second player. 
        if game_level == 2:
            # loop for 2nd player to place its symbol in an empty square
            while True:
                try:
                    choice = int(input(f"Player TWO, it's your turn! Select an empty score for your next move as " + opponent_symbol_choice + "." ))
                    if choice in range(1, 10):
                        if field[choice] == " ":
                            field[choice] = opponent_symbol_choice
                            break
                        else:
                            print("Please select an empty square!")
                    else:
                        print("Invalid input. Please select the numbers "
                              "between 1-9.\n")
                except ValueError:
                    print("Invalid input.")

            # condition to check if the 2nd player wins
            if champion(field, opponent_symbol_choice):
                print_field()
                count_loses()
                print(f"Player two '{opponent_symbol_choice}' is the winner! Congratulations")
                return_to_main_page()

            print_field()

            # condition to check if it's a draw
            if draw(field):
                count_draws()
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