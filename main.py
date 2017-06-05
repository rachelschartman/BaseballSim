from pitcher import Pitcher
from batter import Batter
from team import Team
from game import Game
import random

Pitcher.WKP = .08717;
Pitcher.BAA = .250;
numGames = 10000;
T1 = Team("team1.txt");
T2 = Team("team2.txt");
G = Game(T1, T2);
tally = [0, 0, 0];
scoreTally = [0, 0];
for j in range(numGames):
    G.reset();
    for i in range(9):
        G.doInning();
    if (G.score[0] > G.score[1]):
        tally[0] += 1;
    elif (G.score[1] > G.score[0]):
        tally[1] += 1;
    else:
        tally[2] += 1;
    scoreTally[0] += G.score[0];
    scoreTally[1] += G.score[1];

scoreTally[0] = float(scoreTally[0]) / numGames;
scoreTally[1] = float(scoreTally[1]) / numGames;
print("%s: %d (%.2f%%)     %s: %d (%.2f%%)     ties: %d (%.2f%%)" % (G.t1.name.strip("\n"), tally[0], float(tally[0])/numGames * 100, G.t2.name.strip("\n"), tally[1], float(tally[1])/numGames * 100, tally[2], float(tally[2])/numGames * 100));
print("%s: %.3f     %s: %.3f" % (G.t1.name.strip("\n"), scoreTally[0], G.t2.name.strip("\n"), scoreTally[1]));
