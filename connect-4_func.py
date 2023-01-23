def printGrid(grid: list, gridSize: list, symbols: list) -> None:
    """Print the grid in the CLI"""
    for i in range(gridSize[1]): # prints row's numbers
        print(f' {i+1} ', end='')
    print('') # bring the cursor bring the cursor down one line
    for i in (abs(y) for y in range(-gridSize[0], 0)):
    #'i' will iterate form 'gridSize[0]' to 0
        print('|', end='') 
        for y in grid:
            if len(y) >= i: print('', symbols[y[i-1]], end='|') # if the point exist, print it
            else: print('  ', end='|')
        print('')

def columnsIsWin(collumn: list, player: int, winLenght: int) -> bool:
    """Checks if the collumn just played contains an uninterupted line of 4
    player's points"""
    if len(collumn) >= winLenght:
    # there can not be a line of 4 point if the collumn is less than 4 point in lenght
        chain = 0
        # variable to stock the uninterputed line
        for i in range(len(collumn)):
            if collumn[i] == player: chain += 1
            else: chain = 0
            if chain == winLenght: return True
    return False
    # return a False if there is no uninterupted collumn of 4

def rowIsWin(row: int, player: int, grid: list, winLenght: int, gridSize: list) -> bool:
    """Checks if the row just played contains an uninterupted line of 4
    player's points"""
    chain = 0
    # variable to stock the uninterputed line
    for i in range(gridSize[1]):
        try:
            if grid[i][row] == player: chain += 1
            else: chain = 0
            if chain == winLenght: return True
            # only pass the 'try' if the point is a player's point
        except IndexError: chain = 0; continue
    return False
    # return a False if there are no uninterupted diagonal of 4

def diagonalIsWin(originalCoord: int, player: int, grid: list, winLenght: int, gridSize: list) -> bool:

    # check right to left diagonal
    originalCoord = [originalCoord-1, len(grid[originalCoord-1])-1]
    # convert the number of the line played by the coordonates of the last piece
    c = originalCoord
    # create a copy of 'originalCoord', to be used in the next 10 lines of code
    chain = 0
    l = min(gridSize[1]-c[0], c[1]+1)
    # distance the cursor will have to travel to get to the base of the grid
    c = [c[0]+l-1, c[1]-l+1]
    # base coordonates for the base of the right to left diagonal
    l = min(c[0]+1, gridSize[0]-c[1])
    # the distance the cursor will have to travel to see the entire diagonal
    # to the tip or the side of the grid
    for i in range(l):
        try:
            if grid[c[0]-i][c[1]+i] == player: chain += 1
            # goes thru all the point in the digonal, and check if they belong to the player
            else: chain = 0
            if chain == winLenght: return True
        except IndexError: chain = 0
        # if the point dosn't exist, catch the error, and make 'chain' = 0

    # check left to right diagonal
    c = originalCoord
    # create a copy of 'originalCoord', to be used in the next 10 lines of code
    chain = 0
    # initiate the counter for the lenght of uninterupted line of the player's pieces
    l = min(c[0]+1,c[1]+1)
    # distance the cursor will have to travel to get to the base of the grid
    c = [c[0]-l+1, c[1]-l+1]
    # base coordonates for the base of the right to left diagonal
    l = min(gridSize[0]-c[0],gridSize[1]-c[1])
    # the distance the cursor will have to travel to see the entire diagonal to 
    # the top or the side of the grid
    for i in range(l):
        try:
            if grid[c[0]+i][c[1]+i] == player: chain += 1
            # goes thru all the point in the digonal, and check if they belong to the player
            else: chain = 0
            if chain == winLenght: return True
            # stop the fonction and return True if ther is an uniterupted line
            # of the player's piece
        except IndexError: chain = 0
        # if the point doesn't exist, catch the error, and reset 'chain' to 0
    return False

def getGridDimentions() -> list:
    '''Get dimention for the grid from the players'''
    while True:
        try:
            width = int(input('Width of the board : '))
            if width < 5:
                print('Please enter a number higher or equal to 5'); continue
            break
        except ValueError:
            print('Please enter a number higher or equal to 5'); continue
    while True:
        try:
            lenght = int(input('Lenght of the board : '))
            if lenght < 4:
                print('Please enter a number higher or equal to 4'); continue
            break
        except ValueError:
            print('Please enter a number higher or equal to 4'); continue
    return [lenght,width]

def getPlayerSymbols(index: int) -> str:
    '''Get symbol for a player'''
    while True:
        symbol =  input(f'Player {index+1}, please input your symbol : ')
        if symbol in ['', ' ']:
            print("Can't use this symbol, please input a valid symbol"); continue
        break
    return symbol

def getCoord(grid, playing, gridSize) -> int:
    while True:
        try:
            coord = int(input(f"Player {playing+1} : "))
        except ValueError: print('Wrong input, try again'); continue
        # input is something other than a number
        if coord not in range(1,gridSize[1]+1): print('Wrong input, try again'); continue 
        # input is not out of bound of the grid
        fullCollumns = list(filter(lambda x: len(grid[x-1])==gridSize[0], [i for i in range(1,gridSize[1]+1)]))
        # list of full collumn 
        if coord in fullCollumns: print('Full collumn, please inpyt another collumn'); continue
        # if the collumn selected is full, ask the player for another input
        break
    return coord, fullCollumns

def endOfGame() -> None:
    while True:
        stop = input('Continue ? (Y/N) : ').lower()
        if stop == 'y': return 
        if stop == 'n': exit('See you later :)')
        else: print('Wrong input, please try again')

def main():
    while True: #SessionLoop
        gridSize = getGridDimentions()
        if gridSize[0]*gridSize[1] < 7*6: winLenght = 3
        # if the chozen size of the grid is smaller than the regular one, make the required
        # winning lenght smaller
        elif gridSize[0]*gridSize[1] > 7*6: winLenght = 5
        # if the chozen size of the gris is smaller than the regulat one, make the required
        # winning lenght smaller
        else : winLenght = 4
        grid = [[] for _ in range(gridSize[1])]
        # create the empty 2D grid
        symbols = [getPlayerSymbols(0), getPlayerSymbols(1)]
        # store player's symbol 
        playing  = 0
        # the position of the playing player symbol in 'symbols'

        while True: # GameLoop
            printGrid(grid, gridSize, symbols)
            
            coord, fullCollumns = getCoord(grid, playing, gridSize)

            grid[coord - 1].append(playing)
            # adds the player's piece to the collumn inputed
            if (rowIsWin(len(grid[coord - 1])-1, playing, grid, winLenght, gridSize) or
                columnsIsWin(grid[coord - 1], playing, winLenght) or
                diagonalIsWin(coord, playing, grid, winLenght,gridSize)):

                printGrid(grid, gridSize, symbols)
                print(f'Player {playing+1} won !')
                break

            if fullCollumns == [i for i in range(1, gridSize[1]+1)]:
                printGrid(grid)
                print('All collumns are full, this is a tie.')
                break

            playing = (playing + 1) % 2
            # switch player (0 to 1 and 1 to 0)
        endOfGame()
        
main()