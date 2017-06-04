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
        adjWalkP = pitcher.WKP / Pitcher.WKP * batter.wkp;
        if (random.random() <= adjWalkP):
            self.walk(batter);
            return;
        adjBatAvg = pitcher.BAA / Pitcher.BAA * batter.batavg;
        if (random.random() <= adjBatAvg): #hit
            event = random.random();
            if (event <= batter.hrp / batter.batavg):
                self.advRunners(4, batter); #home run
                return;
            event -= batter.hrp / batter.batavg;
            if (event <= batter.doublep / batter.batavg):
                self.advRunners(2, batter); #double
                return;
            event -= batter.doublep / batter.batavg;
            if (event <= batter.triplep / batter.batavg):
                self.advRunners(3, batter); #triple
                return;
            self.advRunners(1, batter); #otherwise just a single
        else: #out or walk
            if (random.random() <= batter.sop):
                self.currOuts += 1;
                return;
            if (random.random() <= .5):
                self.flyOut();
                return;
            else:
                self.groundOut();
                return;

    def walk(self, batter):
        i = 0;
        while(self.bases[i] != None and i < 3):
            i += 1; #finding force
        if (i == 3):
            self.scoreRun();
            i -= 1;
        while (i > 0):
            self.bases[i+1] = self.bases[i];
            i -= 1;
        self.bases[1] = batter;

    def advRunners(self, num, batter):
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
            self.bases[num] = batter;
        else:
            self.scoreRun();
        return


    def flyOut(self):
        self.currOuts += 1;

    def groundOut(self):
        self.currOuts += 1;

    def doInning(self):
        self.currOuts = 0;
        self.battingTeam = 1;
        while (self.currOuts < 3):
            self.doAtBat(self.t1.getCurrentPitcher(), self.t2.getCurrentBatter());
            self.t2.advanceBatter();
            self.t1.pitchAtBat();
        self.currOuts = 0;
        self.battingTeam = 0;
        while (self.currOuts < 3):
            self.doAtBat(self.t2.getCurrentPitcher(), self.t1.getCurrentBatter());
            self.t1.advanceBatter();
            self.t2.pitchAtBat();
        return;

    def scoreRun(self):
        self.score[self.battingTeam] += 1;
        return;

    def printGame(self):
        print("%s: %d \t %s: %d" % (self.t1.name.strip('\n'), self.score[0], self.t2.name.strip('\n'), self.score[1]));

    def reset(self):
        self.score = [0, 0];
        self.t1.reset();
        self.t2.reset();






