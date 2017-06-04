import numpy as np

class Pitcher:


    BAA = 0
    WKP = 0

    def __init__(self, pitstr):
        (self.name, stats) = pitstr.split(":");
        stats = stats.split(",");
        self.BAA = float(stats[0]);
        self.WKP = float(stats[1]);
        self.maxpitches = np.random.normal(float(stats[2]), float(stats[3]));
        self.pitches = 0;

    def doAtBat(self):
        self.pitches += np.random.binomial(6, 0.478) + 1; #binom w/ 1 added has expected val of 3.87 (MLB avg)
        return (self.pitches >= self.maxpitches);
        #binomial distribution with a success probability of
        #.478. expected value (or average)
        #e(v) of a binomial is p*n p=.478,n=6
    def reset(self):
        self.pitches = 0;
