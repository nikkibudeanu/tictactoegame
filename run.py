# Imports
import random
import gspread
from google.oauth2.service_account import Credentials


# Google Scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tictactoe')

sheet_data = SHEET.worksheet('game')

# Variables to push data to the spreadsheet
count_win = 0
count_lose = 0
count_draw = 0

# Game variables
game_field = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
x_or_o = ["x", "o"]


# Game name function
def print_game_name():
    """
    Prints the game name
    """
    print("""
 _ _ _   __     ____     _ _ _      __        ____     _ _ _    ____    _____
|_   _| |  |  /   __|   |_   _|    /  \     /   __|   |_   _|  / __ \  |  _ _|
  | |   |  | (   /        | |     / /\ \   (   /        | |   | |__| | | |___|
  |_|   |__|  \ _\_       |_|    / ==== \   \ _\__      |_|    \____/  |_|___
    """)


# Game game_field function
def print_game_field():
    """
    Print the game_field for the game and
    sets position for the items in the list.
    """
    print(" Game field" + " "*9 + "Reference game field")
    print(" " + game_field[1] + " | " + game_field[2] +
          " | " + game_field[3] + "  " +
          " "*10 + " " + "1" + " | " + "2" + " | " + "3" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + game_field[4] + " | " + game_field[5] +
          " | " + game_field[6] + "  " +
          " "*10 + " " + "4" + " | " + "5" + " | " + "6" + "  ")
    print("---|---|---" + " "*11 + "---|---|---")
    print(" " + game_field[7] + " | " + game_field[8] +
          " | " + game_field[9] + "  " +
          " "*10 + " " + "7" + " | " + "8" + " | " + "9" + "  ")
    print("\n")

# Reset game_field function


def reset_game_field():
    """
    Reset game_field so the user is able to start a new game
    """
    game_field.clear()
    game_field.extend([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])


# Input username function + add it to the spreadsheet


def take_username_input():
    """
    Ask users to input their name and add it to the spreadsheet first column.
    """
    global username
    global new_col_number
    print("What is your name?\n")
    username = input()
    new_col_number = len(sheet_data.col_values(1)) + 1
    show_choices_and_take_input()

# Quit game function


def quit_game():
    """
    Function to quit the game.
    """
    print("Thank you " + username + " for playing the game!")
    quit()


def add_user_row_to_sheet():
    """
    Function to add user row to sheet.
    """
    sheet_data.update_cell(new_col_number, 1, username)


# Function to count number of games won by the user.
def increment_wins_in_spreadsheet():
    """
    Update the spreadsheet win column with number of wins of each user.
    """
    global count_win
    count_win += 1
    add_user_row_to_sheet()
    sheet_data.update_cell(new_col_number, 3, count_win)


# Function to count draw games.


def increment_draws_in_spreadsheet():
    """
    Update the spreadsheet draw column with number of draws of the user.
    """
    global count_draw
    count_draw += 1
    add_user_row_to_sheet()
    sheet_data.update_cell(new_col_number, 2, count_draw)


# Function to count lost games and update the spreadsheet lost column.


def increment_loses_in_spreadsheet():
    """
    Update the spreadsheet loss column with the number of losses for each user.
    """
    global count_lose
    count_lose += 1
    add_user_row_to_sheet()
    sheet_data.update_cell(new_col_number, 4, count_lose)


# Main function of the game.


def show_choices_and_take_input():
    """
    The function of the main menu that requires user input
    in order to select one of the game sections.
    """
    print("Hello " + username + "!")
    print("Please select one of the following options.\n")
    print("1. Play our game\n")
    print("2. How to play\n")
    print("3. Your score\n")
    print("Q. Quit game\n")

    # Condition to loop through player inputs and go to the next menu.
    while True:
        player_choice = input().strip().lower()
        if player_choice == "1":
            select_game_type()
        elif player_choice == "2":
            how_to_play()
        elif player_choice == "3":
            show_scores()
        elif player_choice == "q":
            quit_game()
        else:
            print("Invalid input. Please select from the options above.")


# Function that brings users to the 'how to play' section.
def how_to_play():
    """
    How to play the game.
    """
    print("1. You will play on the field composed by 3 by 3 squares")
    print("2. Select your symbol betweeen 'X' and 'O'.")
    print("3. Your opponent gets the other symbol once you pick one")
    print("4. Use the reference field to find out which number to input.")
    print("5. The player who gets 3 of his symbols in a row is the winner.")
    print("6. If nobody has 3 marks in a row,game is over with no winners.")
    print("3. If you want to return to the main menu - enter 0.")
    print("4. If you want to quit the game - enter 'q'")

    # Condition to loop to quit or return to the main menu.
    while True:
        player_choice = input().strip().lower()
        if player_choice == "0":
            show_choices_and_take_input()
        elif player_choice == "q":
            quit_game()
        else:
            print("Invalid input, please select '0' or 'q'!")

# Function to select game vs the computer or vs a player.


def select_game_type():
    """
    Enables user to play against computer or another player.
    """
    print("Select which game would you like to play: \n")
    print("1. Play the game against the computer. \n")
    print("2. 2 player game. \n")
    print("Q. Quit game. \n")
    # Condition that loops through user input to select a game type.
    while True:
        player_game_choice = input().strip().lower()
        global game_type
        if player_game_choice == "1":
            game_type = 1
            play_game()
        elif player_game_choice == "2":
            game_type = 2
            play_game()
        elif player_game_choice == "q":
            quit_game()
        else:
            print("Invalid input, please select:")
            print("1' to play against the computer")
            print("'2' to play a 2 player game or 'q' to quit the game")


# Function to print scores, games played, lost games, won games and draw games.
def show_scores():
    """
    Function to print out user's score.
    Check sheet on column 1, if that user played previously.
    Fetch the scores of that user from GSheet.
    No of rows would be `count_games`,
    """

    cells_matching_username = sheet_data.findall(username)
    rows_matching_username = [cell.row for cell in cells_matching_username]
    total_games_played = len(rows_matching_username)
    games_won = 0
    games_lost = 0
    games_drawn = 0
    for row in rows_matching_username:
        row_data = sheet_data.row_values(row)
        if row_data[1] > '0':
            games_drawn += 1
        elif row_data[2] > '0':
            games_won += 1
        elif row_data[3] > '0':
            games_lost += 1

    print("Here is your score: \n")
    print("You have played " + str(total_games_played) + " times!\n")
    print("You have won " + str(games_won) + " times!\n")
    print("Draw games: " + str(games_drawn))
    print("You have lost " + str(games_lost) + " times!\n")
    print("If you want to start again, enter '0'.\n")
    print("To quit the game, enter 'q'.")

    while True:
        player_choice = input().strip().lower()
        if player_choice == "0":
            reset_game_field()
            start_game()
        elif player_choice == "q":
            quit_game()
        else:
            print("Invalid input,select '0' to return to the main page.\n")
            print("If you want to quit the game, please select 'q'.\n")

# Function to determine the winner.


def champion(game_field, player_symbol):
    """
    Function to determine who has won the game. Returns True or False.
    Each win scenario below:
    1. Middle column.
    2. First row
    3. Diagonal from upper left corner to lower right corner.
    4. Middle row.
    5. Last row.
    6. First column.
    7. Last column.
    8. Diagonal from upper right corner to lower left corner.
    """
    if(game_field[2] == player_symbol and game_field[5] == player_symbol
       and game_field[8] == player_symbol) or \
      (game_field[1] == player_symbol and game_field[2] == player_symbol
        and game_field[3] == player_symbol) or \
      (game_field[1] == player_symbol and game_field[5] == player_symbol
        and game_field[9] == player_symbol) or \
      (game_field[4] == player_symbol and game_field[5] == player_symbol
        and game_field[6] == player_symbol) or \
      (game_field[7] == player_symbol and game_field[8] == player_symbol
        and game_field[9] == player_symbol) or \
      (game_field[1] == player_symbol and game_field[4] == player_symbol
        and game_field[7] == player_symbol) or \
      (game_field[3] == player_symbol and game_field[6] == player_symbol
        and game_field[9] == player_symbol) or \
      (game_field[3] == player_symbol and game_field[5] == player_symbol and game_field[7] == player_symbol):
        return True
    else:
        return False

# Function to determine if it is a draw game.


def draw(game_field):
    """
    Function to check if there are any squares left.
    Returns false if there are more than 1 square left
    and true if not(game ends with no winners).
    """
    if game_field.count(" ") > 1:
        return False
    else:
        return True

# Function to create random computer moves in the vs computer game.


def computer_choice(game_field, opponent_symbol_choice):
    """
    Loops to get a random computer choice within the field.
    Checks if the choice is an empty string within the list.
    Place the symbol.
    Break the loop.
    """
    while True:
        # randint learnt on:
        #  https://www.w3schools.com/python/ref_random_randint.asp
        computer_choice = random.randint(1, 9)
        if game_field[computer_choice] == " ":
            return computer_choice

# Function to take user input for x_or_o


def ask_for_x_or_o():
    """
    Let's user select the symbol he/she wants to play as. Either 'X'
     or 'O'. Prints out to user message that wrong symbol has been
     chosen, if so restarts the game.
    """
    print(f"Do you want to play as  '{x_or_o[0]}' or  '{x_or_o[1]}?' \n")
    global player_symbol_choice
    player_symbol_choice = input().lower().strip()
    if player_symbol_choice == x_or_o[0]:
        opponent_symbol_choice = x_or_o[1]
    elif player_symbol_choice == x_or_o[1]:
        opponent_symbol_choice = x_or_o[0]
    elif player_symbol_choice == "q":
        quit_game()
    else:
        print("Invalid input, please use either 'X' or 'O'.\n")
        print("If you want to quit the game, type 'Q'.\n")
        play_game()
    return [player_symbol_choice, opponent_symbol_choice]

# Main function which runs the game.


def play_game():
    """
    The main game function that gets executed after all previous options
    gets put through.
    """
    # Take user input for symbol choice
    [player_symbol_choice, opponent_symbol_choice] = ask_for_x_or_o()

    # The main game loop
    while True:
        print_game_field()
        # Condition to loop for the main player input.
        while True:
            # function to add input and check if the square is empty
            # and if the input is valid.
            try:
                choice = int(input(f"Please choose an empty space for "
                                   f"your move as '{player_symbol_choice}'."))
                if choice in range(1, 10):
                    if game_field[choice] == " ":
                        game_field[choice] = player_symbol_choice
                        break
                    else:
                        print("Please select an empty square!")
                else:
                    print("Invalid input. Please use the numbers "
                          "between 1-9.\n")
            except ValueError:
                print("Please enter a valid number!")

        # Condition to check if the user won.
        # Two different feedback messages depending on the game type.
        if champion(game_field, player_symbol_choice):
            print_game_field()
            increment_wins_in_spreadsheet()
            if game_type == 1:
                print("You win! Congratulations")
            elif game_type == 2:
                print("Player one wins! Congratulations")
            show_scores_or_quit()

        print_game_field()
        # Condition to check if the grid is full to declare no winners.
        if draw(game_field):
            increment_draws_in_spreadsheet()
            print("2 winners! It's a draw!")
            show_scores_or_quit()

        # Condition to check if the game type is against the computer.
        if game_type == 1:
            choice = computer_choice(game_field, opponent_symbol_choice)
            game_field[choice] = opponent_symbol_choice

            # Condition to check if the computer wins
            if champion(game_field, opponent_symbol_choice):
                print_game_field()
                increment_loses_in_spreadsheet()
                print("Computer wins!")
                show_scores_or_quit()

            # Condition to check if it's a draw.
            if draw(game_field):
                increment_draws_in_spreadsheet()
                print("2 winners! It's a draw!")
                show_scores_or_quit()

        # Condition to check if the game type is against a second player.
        if game_type == 2:
            # Loop for 2nd player to place its symbol in an empty square
            while True:
                try:
                    choice = int(input("Player TWO, select an empty space."))
                    if choice in range(1, 10):
                        if game_field[choice] == " ":
                            game_field[choice] = opponent_symbol_choice
                            break
                        else:
                            print("Please select an empty square!")
                    else:
                        print("Invalid input. Please select the numbers "
                              "between 1-9.\n")
                except ValueError:
                    print("Invalid input.")

            # Condition to check if the 2nd player wins
            if champion(game_field, opponent_symbol_choice):
                increment_loses_in_spreadsheet()
                print_game_field()
                print(f"Player two '{opponent_symbol_choice}' is the winner!")
                show_scores_or_quit()

            print_game_field()

            # Condition to check if it's a draw
            if draw(game_field):
                increment_draws_in_spreadsheet()
                print("2 winners! It's a draw!\n")
                show_scores_or_quit()

# Function to return to the main page.


def show_scores_or_quit():
    """
    User has to select to go back to the main page or quit the game.
    """
    print("Would you like to see your scores? \n")
    print("Select '1' if yes or 'q' if you would like to quit the game. \n ")
    print("If you want to start again, select '0'. \n ")
    while True:
        player_choice = input().strip()
        if player_choice == "1":
            show_scores()
        elif player_choice == "q":
            quit_game()
        elif player_choice == "0":
            reset_game_field()
            start_game()
        else:
            print("Invalid input!Please try again!")
# Function to start game


def start_game():
    """
    Functions to start game.
    """
    print_game_name()
    take_username_input()
    show_choices_and_take_input()


start_game()
