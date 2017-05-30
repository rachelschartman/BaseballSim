import random



class Game:

    def __init__(self, team1, team2):
        self.t1 = team1;
        self.t2 = team2;
        self.currOuts = 0;
        self.bases = 4*[None]; #initialize bases
        self.score = (0,0);
    
    def doAtBat(self, pitcher, batter):
        adjBatAvg = pitcher.BAA / Pitcher.BAA * batter.batavg;
        if (random.random() <= adjBatAvg): #hit
            event = random.random();
            if (event <= batter.hrp / batter.batavg):
                self.advRunners(4); #home run
                return;
            event -= batter.hrp / batter.batavg;
            if (event <= doublep / batter.batavg):
                self.advRunners(2); #double
                return;
            event -= batter.doublep / batter.batavg;
            if (event <= batter.triplep / batter.batavg):
                self.advRunners(3); #triple
                return;
            self.advRunners(1); #otherwise just a single
        else: #out or walk
            event = random.random();
            
