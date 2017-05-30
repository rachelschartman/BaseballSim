class Batter:

	batavg = 0
	wkp = 0
	doublep = 0
	triplep = 0
	hrp = 0

	def __init__(self, batstring):
            (self.name, stats) = batstring.split(":")
            stats = stats.split(",")
            self.batavg = float(stats[0])
            self.wkp = float(stats[1])
            self.hrp = float(stats[2])
            self.doublep = float(stats[3])
            self.triplep = float(stats[4])
