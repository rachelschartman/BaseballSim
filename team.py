from pitcher import Pitcher
from batter import Batter

class Team:

    def __init__(self, fname):
        f = open(fname,'r')
        self.name = f.readline()
        self.lineupPos = 0
        self.lineup = []
        self.pitchers = []
        f.readline();
        for i in range(0, 9):
            self.lineup.append(Batter(f.readline()))
        for i in range(0,9):
            print self.lineup[i].name

        
