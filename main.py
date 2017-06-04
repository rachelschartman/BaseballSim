from pitcher import Pitcher
from batter import Batter
from team import Team
from game import Game
import random

Pitcher.WKP = .08717;
Pitcher.BAA = .250;

T1 = Team("team1.txt");
T2 = Team("team2.txt");
G = Game(T1, T2);
tally = [0, 0];
for j in range(1000):
    G.reset();
    for i in range(9):
        G.doInning();
    if (G.score[0] > G.score[1]):
        tally[0] += 1;
    elif (G.score[1] > G.score[0]):
        tally[1] += 1;

print("%s: %d     %s: %d" % (G.t1.name.strip("\n"), tally[0], G.t2.name.strip("\n"), tally[1]));
