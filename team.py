from pitcher import Pitcher
from batter import Batter

class Team:

    def __init__(self, fname):
        f = open(fname,'r');
        self.name = f.readline();
        self.lineupPos = 0;
        self.currPitcher = 0;
        self.lineup = [];
        self.pitchers = [];
        f.readline();
        for i in range(9):
            self.lineup.append(Batter(f.readline()));
        f.readline();
        for i in range(2):
            self.pitchers.append(Pitcher(f.readline()));

    def getCurrentBatter(self):
        return self.lineup[self.lineupPos];

    def advanceBatter(self):
        self.lineupPos = (self.lineupPos + 1) % 9;
        return

    def getCurrentPitcher(self):
        return self.pitchers[self.currPitcher];

    def pitchAtBat(self):
        if self.pitchers[self.currPitcher].doAtBat():
            self.currPitcher += 1;
        return

    def reset(self):
        lineupPos = 0;
        self.currPitcher = 0;
        self.pitchers[0].reset();
        self.pitchers[1].reset();


