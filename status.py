class StatusInformation:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.pwr = 0
        self.armr = 0
        self.con = 0
        self.lck = 0
        self.total = self.pwr + self.armr + self.con + self.lck
        self.win = 0


class PlayerStatus(StatusInformation):
    def __init__(self, name):
        super().__init__(name)
        self.level = 0
        self.exp = 0
        self.maxexp = 100

    def generatePlayer(self):
        self.pwr = float(input())
        self.armr = float(input())
        self.con = float(input())
        self.lck = float(input())

#        self.pwr, self.armr, self.con, self.lck = [float(n) for n in input().split()]
#        code above was to test if whether this is a better way to input numbers

    def printStats(self):
        test = "PWR: %s \nARMR: %s \nCON %s \nLCK %s" % (self.pwr, self.armr, self.con, self.lck)
        print(test.strip())
        testtotal = [self.pwr, self.armr, self.con, self.lck]
        self.total = sum(testtotal)
        print("Total:", self.total)


class MonsterStatus(StatusInformation):
    def __init__(self, name):
        super().__init__(name)