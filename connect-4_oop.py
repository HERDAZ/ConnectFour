class Board:
    '''Define the class 'Board' '''
    def __init__(self):
        while True:
            try:
                width = int(input('Width of the board : '))
                if width < 5: print('Please enter a number higher or equal to 5'); continue
                self.width = width
                break
            except ValueError: print('Please enter a number higher or equal to 5'); continue
            # ask for another input if 'width' isn't a number
        while True: # LenghtChoosingLoop
            try:
                lenght = int(input('Lenght of the board : '))
                if lenght < 4: print('Please enter a number higher or equal to 4'); continue
                self.lenght = lenght
                break
            except ValueError: print('Please enter a number higher or equal to 4'); continue
            # ask for another input if 'width' isn't a number
        if width*lenght < 7*6: self.winLenght = 3
        elif width*lenght > 7*6: self.winLenght = 5
        else: self.winLenght = 4

        self.grid = [[] for _ in range(width)]

    def print(self) -> None:
        '''Print the grid in the CLI'''
        for i in range(self.width):
        # prints row's numbers
            print(f' {i+1}{" "*(2-len(str(i+1)))}', end='')
        print('')
        for i in (abs(y) for y in range(-self.lenght, 0)):
        # make if so 'i' will iterate form 'self.lenght' to 0
            print('|', end='')
            for y in self.grid:
            # print each row, and places the corresponding symbol
                if len(y) >= i: print('',playerList[y[i-1]].symbol, end='|')
                else: print('  ', end='|')
            print('')

    def checkForWin(self, index:int, coord: int) -> bool:
        '''Check if the player playing won, by scanning the row, collumn and both diagonal
        affected by the play'''
        # check if the collumn is a win
        collumn = self.grid[coord]
        if len(collumn) >= self.winLenght:
            chain = 0
            # variable to stock the uninterputed line
            for i in range(len(collumn)):
                if collumn[i] == index: chain += 1
                else: chain = 0
                if chain == self.winLenght: return True

        # check if the row is a win
        row = len(self.grid[coord])-1
        chain = 0
        # variable to stock the uninterputed line
        for i in range(self.width):
            try:
                if self.grid[i][row] == index: chain += 1
                else: chain = 0
                # only pass the 'try' if the point is a player's point
            except IndexError: chain = 0; continue
            if chain == self.winLenght: return True

        # check if the right to left diagonal is a win
        originalCoord = [coord, len(self.grid[coord])-1]
        # convert the 1 dimention coord of the line played into the 2 dimentional coord
        # of the played point
        c = originalCoord
        # create a copy of 'originalCoord', to be used in the next 10 lines of code
        chain = 0
        l = min(self.width-c[0],c[1]+1)
        # the distance the cursor will have to travel to get to the base of the grid
        c = [c[0]+l-1, c[1]-l+1]
        # create the base coodinate for the right to left diagonal
        l = min(c[0]+1, self.lenght-c[1])
        # the distance the cursor will have to travel to see the entire diagonal
        # to the tip of the grid
        for i in range(l):
            try:
                if self.grid[c[0]-i][c[1]+i] == index: chain += 1
                else: chain = 0
                if chain == self.winLenght: return True
            except IndexError: chain = 0
            # if the point doesn't exist, catch the error, and make 'chain' = 0

        # check if the left to right diagonal is a win
        c = originalCoord
        # create a copy of 'originalCoord', to be used in the next 10 lines of code
        chain = 0
        # initiate the counter for the lenght of uninterupted line of the index's pieces
        l = min(c[0]+1,c[1]+1)
        # the distance the cursor will have to travel to get to the base of the grid
        c = [c[0]-l+1, c[1]-l+1]
        # create the base coordonates for the left to right diagonal
        l = min(self.lenght-c[0], self.width-c[1])
        # the distance the cursor will have to travel to see the entire diagonal to 
        # the top of the grid
        for i in range(l):
            try:
                if self.grid[c[0]+i][c[1]+i] == index: chain += 1
                # check if the point at 'grid[c[1]+i][c[0]+i]' is one of the index's
                # piece, and add 1 to 'chain' if so
                else: chain = 0
                if chain == self.winLenght: return True
                # stop the fonction and return True if ther is an uniterupted line
                # of the index's piece
            except IndexError: chain = 0
            # if the point dosn't exist, catch the error, and make 'chain' = 0
        return False
    

class Player:
    '''Define the class 'Player' '''
    def __init__(self, index: int):
        self.index = index
        self.tie = False
        while True:
            symbol =  input(f'Player {self.index+1}, please input your symbol : ')
            if symbol in ['', ' ']: print("Can't use this symbol, please input a valid symbol"); continue
            # verifiy if they are non visible character, if so, ask for another input
            if len(symbol) > 1: print("Symbols can only be ONE character, please input a valid symbol"); continue
            # verify if the input is one characher long, if not, ask for another input
            self.symbol = symbol
            break
    def play(self):
        while True:
            try:
                fullCollumns = list(filter(lambda x: len(grid.grid[x-1])==grid.lenght, [i for i in range(1,grid.width+1)]))
                if fullCollumns == [i for i in range(1, grid.width+1)]: self.tie = True; return
                # if all the collumn are full, 'self.tie' = True, and break out of the while
                coord = int(input(f"Player {self.index+1} : "))
                # get input from player
                if coord not in range(1,grid.width+1): print('Invalid input, please input a valid collumn'); continue
                # ask for another input if 
                if coord in fullCollumns: print('Full collumn, please input another collumn'); continue
                # if 'coord' doesn't have the right value, make the player input his play one more time

            except ValueError: print('Input unundestandable, please try again'); continue
            break
        grid.grid[coord-1].append(self.index)
        # add the index of the player to the grid
        self.win = grid.checkForWin(self.index, coord-1)
        # check if the player won, and put the bool in this variable

while True: #SessionLoop
    grid = Board()
    # innitiate the board
    playerList = [Player(0),Player(1)]
    # list where we initiate both player with their index
    playing = 0
    # varaible to store the position in 'playerlist' of the player playing
    # It will switch between 0 and 1 to alternate the player
    while True: #GameLoop
        grid.print()
        player = playerList[playing]
        player.play()
        if player.tie:
            grid.print()
            print('This game is a tie, well played to both player !')
            break
            # break to get out of the GameLoop and into the BetweenGameLoop
        if player.win:
            grid.print()
            print(f'Player {playing + 1} won !')
            break
            # break to get out of the GameLoop and into the BetweenGameLoop
        playing = (playing + 1) % 2
        # switch 'playing' from 1 to 0 or 0 to 1
    while True: # BetweenGameLoop
        stop = input('Continue playing ? (Y/N) : ').lower()
        # get choice from player to either continue playing, or stop
        if stop not in 'yn' or len(stop) != 1: print('Input unundestandable, please try again'); continue
        else: break
    if stop == 'n': break
    else: continue
    
print('See you next time :)')