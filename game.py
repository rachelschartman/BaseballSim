import random



class Game:

    def __init__(self, team1, team2):
        self.t1 = team1;
        self.t2 = team2;
        self.currOuts = 0;
        self.bases = 4*[None]; #initialize bases
        self.score = (0,0);
    
    def doAtBat(pitcher, batter):
        adjBatAvg = pitcher.BAA / Pitcher.BAA * batter.batavg;
        if (random.random() <= adjBatAvg): #hit
            
        else: #out or walk
