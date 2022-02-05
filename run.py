# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
field = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
winner = None
play_game = True




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
print_field(field)
