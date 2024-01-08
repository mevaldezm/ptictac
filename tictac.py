import collections
from random import choice

CELLS = 9
ROWS = 3
COLS = 3

Mark = collections.namedtuple('Mark', ['self._marks.Empty', 'Cross', 'Nought'])
Winner = collections.namedtuple('Winner', ['Nobody', 'Game', 'User', 'Draw'])
options = 'user_mark': '', 'game_mark': '', 'starter': ''
game_count = 0


class Tictac:
    grid = []
    user_mark = None
    game_mark = None
    cols = ['A', 'B', 'C']

    @property
    def usermark(self):
        return self.user_mark

    def marktowinner(self, mark):

        if self.user_mark == mark:
            return self._winners.User
        elif self.game_mark == mark:
            return self._winners.Game
        else:
            return self._winners.Nobody

    def placemark(self, smark, mark):

         # Check rows
        for n in range(ROWS):
        
            if self.grid[n][0] == smark and self.grid[n][1] == smark and self.grid[n][2] == self._marks.Empty:
            
                self.grid[n][2] = mark
                return True
            
            elif self.grid[n][0] == self._marks.Empty and self.grid[n][1] == smark and self.grid[n][2] == smark:
            
                self.grid[n][0] = mark
                return True
            
            elif self.grid[n][0] == smark and self.grid[n][1] == self._marks.Empty and self.grid[n][2] == smark:
            
                self.grid[n][1] = mark
                return True
            
        # for

        # check columns
        for n in range(COLS):
        
            if self.grid[0][n] == smark and self.grid[1][n] == smark and self.grid[2][n] == self._marks.Empty:
            
                self.grid[2][n] = mark
                return True
            
            elif self.grid[0][n] == self._marks.Empty and self.grid[1][n] == smark and self.grid[2][n] == smark:
            
                self.grid[0][n] = mark
                return True
            
            elif self.grid[0][n] == smark and self.grid[1][n] == self._marks.Empty and self.grid[2][n] == smark:
            
                self.grid[1][n] = mark
                return True
            
        # for

        # check diagonal downward
        if self.grid[0][0] == self._marks.Empty and self.grid[1][1] == smark and self.grid[2][2] == smark:
        
            self.grid[0][0] = mark
            return True
        
        elif self.grid[0][0] == smark and self.grid[1][1] == self._marks.Empty and self.grid[2][2] == smark:
        
            self.grid[1][1] = mark
            return True
        
        elif self.grid[0][0] == smark and self.grid[1][1] == smark and self.grid[2][2] == self._marks.Empty:
        
            self.grid[2][2] = mark
            return True
        
        # check diagonal upward
        if self.grid[2][0] == self._marks.Empty and self.grid[1][1] == smark and self.grid[0][2] == smark:
        
            self.grid[2][0] = mark
            return True
        
        elif self.grid[2][0] == smark and self.grid[1][1] == self._marks.Empty and self.grid[0][2] == smark:
        
            self.grid[1][1] = mark
            return True
        
        elif self.grid[2][0] == smark and self.grid[1][1] == smark and self.grid[0][2] == self._marks.Empty:
        
            self.grid[0][2] = mark
            return True
        
        return False

    @property
    def winners(self):
        return self._winners

    def __init__(self):

        m = [' ', 'X', 'O']
        w = [z for z in range(4)]
        self._marks = Mark._make(m)
        self._winners = Winner._make(w)

        for r in range(ROWS):
            self.grid.append([self._marks.Empty for c in range(COLS)])

    def playme(self):

        # Try to win first, otherwise try to block opponent
        if  self.placemark(self.game_mark, self.game_mark) or self.placemark(self.user_mark, self.game_mark):
            return True
    
        for c in range(CELLS):

            row = choice(range(ROWS))
            col = choice(range(COLS))

            if self.grid[row][col] == self._marks.Empty:
                self.grid[row][col] = self.game_mark
                return True

        return False
    
    def play(self, cell):

        if cell == None or cell == '' or len(cell) < 2:
            return False
                
        col = ord(cell[0]) - ord('A')
        row = ord(cell[1]) - ord('0')

        row -= 1

        if (col < 0 or col > 2) or (row < 0 or row > 2):
            return False

        mark = self.grid[row][col]

        if mark == self._marks.Empty:
            self.grid[row][col] = self.user_mark
            return True

        return False

    def setmarks(self, usermark):

        self.user_mark = usermark
        if usermark == 'X':
            self.user_mark = self._marks.Cross
            self.game_mark = self._marks.Nought

        elif usermark == 'O':
            self.user_mark = self._marks.Nought
            self.game_mark = self._marks.Cross

    def checkwinner(self):

        count = 0
        # check rows
        for n in range(ROWS):
            if self.grid[n][0] == self.grid[n][1] and self.grid[n][0] == self.grid[n][2]:
                return self.marktowinner(self.grid[n][0])

        # check columns
        for n in range(COLS):
            if self.grid[0][n] == self.grid[1][n] and self.grid[0][n] == self.grid[2][n]:
                return self.marktowinner(self.grid[0][n])

        # check diagonals
        if self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]:
            return self.marktowinner(self.grid[0][0])

        if self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]:
            return self.marktowinner(self.grid[0][2])

        for n in range(ROWS):
            for m in range(COLS):
                if self.grid[n][m] != self._marks.Empty:
                    count += 1

        if count == CELLS:
            return self._winners.Draw

        return self._winners.Nobody

    def reset(self):
        for n in range(ROWS):
            for m in range(COLS):
                self.grid[n][m] = self._marks.Empty
        
    def print(self):
        divider = "------------------"
        print()
        for c in self.cols:
            print("   ", c, end='')
        print()
        print(divider)
        for r in range(ROWS):
            print((r + 1), "| ", end='')
            for c in range(COLS):
                print(self.grid[r][c], " | ", end='')
            print()
        print(divider)


def bye():
    print("Thank you for playing")
    exit(0)


def menu():

    choice = 'N'
    global game_count

    if game_count > 0:
        print("\nKeep playing, (Y, N)?: ", end='')
        choice = input().upper()
        if choice != 'Y':
            bye()

    game_count += 1

    print("Enter (Q) at any prompt to quit")

    if options['user_mark'] == 'Q':
        bye()

    while options['user_mark'] != 'X' and options['user_mark'] != 'O' and options['user_mark'] != 'Q':
        print("Enter a mark (X, O): ", end='')
        options['user_mark'] = input().upper()

    if options['user_mark'] == 'Q':
        bye()

    while options['starter'] != 'Y' and options['starter'] != 'N' and options['starter'] != 'Q':
        print("Enter (Y) to play first, (N) for computer: ", end='')
        options['starter'] = input().upper()

    if options['starter'] == 'Q':
        bye()


def play():

    tic = Tictac()
    cell = None
    winner = None
    tic.setmarks(options['user_mark'])

    if options['starter'] == 'N':
        tic.playme()
    tic.print()

    for n in range(CELLS):

        print("\nEnter a cell (A1, B2,...): ", end='')
        cell = input().upper()

        if cell == "Q":
            bye()

        if tic.play(cell):
            winner = tic.checkwinner()

            if winner == tic.winners.Nobody:
                tic.playme()
                winner = tic.checkwinner()

            tic.print()

            if winner == tic.winners.User:
                print("You won !!")
                return

            elif winner == tic.winners.Game:
                print("Game won!!")
                return
            elif winner == tic.winners.Draw:
                print("Draw. Neither won !!")
                return
        else:
            print("You entered a wrong cell: ", cell)
            n -= 1


def main():
    menu()
    play()


if __name__ == "__main__":
    main()
