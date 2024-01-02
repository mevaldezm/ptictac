import collections
from random import choice

CELLS = 9 
ROWS  = 3 
COLS = 3 

Mark = collections.namedtuple('Mark', ['Empty','Cross', 'Nought'])
Winner = collections.namedtuple('Winner', ['Nobody', 'Game', 'User', 'Draw'])


class GameOptions:
    user_mark = None
    game_mark = None
    starter = None


class Tictac:
    grid = []
    user_mark = None
    game_mark = None
    cols = ['A', 'B', 'C']
    
    @property
    def usermark(self):
        return self.user_mark
    
    def  marktowinner(self, mark):
         if self.user_mark == mark:
             return Winner.User
         elif self.game_mark == mark:
             return Winner.Game
         else:
             return Winner.Nobody

    def placemarks(self, usermark):
        pass
    def __init__(self):
        
        m = [' ', 'X', 'O']
        w = [ z for z in range(4)]
        self._marks = Mark._make(m)
        self._winners = Winner._make(w)
        
        for r in range(ROWS):
            self.grid.append([ self._marks.Empty for c in range(COLS)])

    def play(self):
        for c in range(CELLS):
            row = choice(range(ROWS))
            col = choice(range(COLS))
            if self.grid[row][col] == self._marks.Empty:
                self.grid[row][col] = self.game_mark
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
                
    def checkwinner():
        pass
    def reset(self):
        pass
    def rightpad():
        pass
    def print(self):
        print(self.grid)

def main():
    tic = Tictac()
    tic.setmarks('X')
    tic.play()
    tic.print()

if __name__=="__main__":
    main()