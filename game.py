import random
from batter import Batter
from pitcher import Pitcher



class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

def bigPrint(strng):
    print bcolors.WARNING + strng + bcolors.ENDC;

class Game:

    def __init__(self, team1, team2):
        self.t1 = team1;
        self.t2 = team2;
        self.battingTeam = 0;
        self.currOuts = 0;
        self.bases = 4*[None]; #initialize bases
        self.score = [0,0];

    def doAtBat(self, pitcher, batter):
        self.bases[0] = batter;
        adjWalkP = pitcher.WKP / Pitcher.WKP * batter.wkp;
        if (random.random() <= adjWalkP):
            self.walk();
            return;
        adjBatAvg = pitcher.BAA / Pitcher.BAA * batter.batavg;
        if (random.random() <= adjBatAvg): #hit
            event = random.random();
            if (event <= batter.hrp / batter.batavg):
                self.advRunners(4); #home run
                return;
            event -= batter.hrp / batter.batavg;
            if (event <= batter.doublep / batter.batavg):
                self.advRunners(2); #double
                return;
            event -= batter.doublep / batter.batavg;
            if (event <= batter.triplep / batter.batavg):
                self.advRunners(3); #triple
                return;
            self.advRunners(1); #otherwise just a single
        else: #out
            if (random.random() <= batter.sop): #strikeout
                self.currOuts += 1;
                return;
            if (random.random() <= .2): #flyout
                self.flyOut();
                return;
            else:
                self.groundOut(); #groundout
                return;

    def walk(self):
        i = 0;
        while(i <= 3 and self.bases[i] != None):
            i += 1; #finding force
        if (i >= 4): #if force at third base run gets scored
            self.scoreRun();
        i = 3;
        while (i > 0): #advance all runners one base
            self.bases[i] = self.bases[i-1];
            i -= 1;
        self.bases[0] = None; #set current batter to none

    def advRunners(self, num):
        i = 3;
        while ( i > 0 ):
            if (self.bases[i] != None):
                if (i + num >= 4):
                    self.scoreRun();
                else:
                    self.bases[i+num] = self.bases[i];
                    self.bases[i] = None;
            i -= 1;
        if (num < 4):
            self.bases[num] = self.bases[0];
        else:
            self.scoreRun();
        self.bases[0] = None;
        return


    def flyOut(self):
        self.currOuts += 1;

    def groundOut(self):
        i = 0;
        while (self.bases[i] != None and i < 3):
            i += 1; #finding force
        if (i == 4):
            i -= 1;
        if (i > 0):
            if (random.random() < .5): #double play
                self.bases[i] = None;
                self.bases[i-1] = None;
                self.currOuts += 2;
                self.advRunners(1); #simulate rest of players running
                return;
        self.bases[i] = None;
        self.advRunners(1);
        self.currOuts += 1;

    def doInning(self):
        self.currOuts = 0;
        self.battingTeam = 1;
        for i in range(4):
            self.bases[i] = None;
        while (self.currOuts < 3):
            self.doAtBat(self.t1.getCurrentPitcher(), self.t2.getCurrentBatter());
            self.t2.advanceBatter();
            self.t1.pitchAtBat();
        self.currOuts = 0;
        self.battingTeam = 0;
        for i in range(4):
            self.bases[i] = None;
        while (self.currOuts < 3):
            self.doAtBat(self.t2.getCurrentPitcher(), self.t1.getCurrentBatter());
            self.t1.advanceBatter();
            self.t2.pitchAtBat();
        return;

    def scoreRun(self):
        if (self.currOuts < 3):
            self.score[self.battingTeam] += 1;
        return;

    def printGame(self):
        print("%s: %d \t %s: %d" % (self.t1.name.strip('\n'), self.score[0], self.t2.name.strip('\n'), self.score[1]));

    def reset(self):
        self.score = [0, 0];
        self.t1.reset();
        self.t2.reset();
        for i in range(4):
            self.bases[i] = None;






