import random

# global variable for grid size, the grid, the number of ships to be randomly place and messages 
grid_size = 10
grid = [ ['']*grid_size for i in range(grid_size) ]
num_of_ships = 5
message = []

# function to draw my board with row and column with numbering
def drawBoard(myBoard):
    # puts a space before we make the line of numbers for the columns
    print("  ", end="")
    # loops through the range given and places a numbers 0 through grid_size on the first line
    for column in range(grid_size):
        print(f"  {column}  ", end="")
    print()

    # loops through grid amount and prints out the matrix/board
    for i in range(grid_size):
        # creates the numbering on the rows
        print(f"{i} ", end="")
        for j in range(grid_size):
            print(f'['+myBoard[i][j]+']', end = "")
        print()
    return

# populates the 2d matrix 
def setupBoard(myBoard):
    i = j = 0
    # loops through all the locations on the board
    while i < grid_size:
        while j < grid_size:
            # replaces the empty area with a " . "
            myBoard[i][j] = ' . '
            j += 1
        j = 0
        i += 1

    # places ships in 5 random locations
    for _ in range(num_of_ships):
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)
        myBoard[randomRow][randomCol] = ' S '

# function to check if the user guess a ship location or not
def hitOrMiss(myBoard, row, col):
    # loops through the board
    for i in range(grid_size):
        for j in range(grid_size):
            # if the location of the users guess and the board line up this is true
            if (myBoard[row][col] == myBoard[i][j]):
                # if the user has enter this location before this runs
                if (myBoard[row][col] == ' X '):
                    message.append('You already hit this ship.')
                    return True
                # if the user enters the location of a ship the first time this runs
                if (myBoard[i][j] == ' S '):
                    myBoard[row][col] = ' X '
                    return True
                # if the users enters the location where a ship is not, this runs
                if (myBoard[i][j] == ' . '):
                    myBoard[row][col] = ' O '
                    return False
    return 

# function to determine if all the ships have been sunk
def isGameOver(myBoard):
    # insatiate a counter for ships being hit
    num_of_ships_hit = 0

    # loops through 2d array
    for i in range(grid_size):
        for j in range(grid_size):
            # if a ship is successfully hit this runs 
            if (myBoard[i][j] == ' X '):
                # increase the count of ships hit 
                num_of_ships_hit += 1
    # if the number of ships hit is not equal to the number of ship floating this is false
    return num_of_ships_hit != num_of_ships

def main(myBoard):
    print(f"Welcome to Battleship! Sink all the ships.")

    setupBoard(myBoard)
    drawBoard(myBoard)

    # while we still have ships this still runs
    while isGameOver(myBoard):
        try:
            while True:
                column = int(input("Enter a column number (X): "))
                # if the user enters a number outside of the grid we repeat this step
                if column >= grid_size or column < 0:
                    print(f"Invalid column number must be between 0 and {grid_size}.")
                    continue  
                break  
            while True:
                row = int(input(f"Enter a row number (Y): "))
                # if the user enters a number outside of the grid we repeat this step
                if row >= grid_size or row < 0:
                    print(f"Invalid row number must be between 0 and {grid_size}.")
                    continue  
                break  

            if hitOrMiss(myBoard, row, column): 
                print(f"Target Hit!")

                # if the user enters the same location of a successful previous hit this runs
                if message:
                    message_value = message[0]
                    print(message_value)
            else:
                print("Target Missed!")

            # redraw the board after a guess 
            drawBoard(myBoard)

        except ValueError:
            print("Enter a valid number.")
    # after all the ships have been hit the game will end displaying this message
    print('Game over! All ships are sunk!')

if __name__ == "__main__":
    main(grid)
