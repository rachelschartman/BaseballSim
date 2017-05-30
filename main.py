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
for i in range(9):
    G.doInning();
G.printGame();

