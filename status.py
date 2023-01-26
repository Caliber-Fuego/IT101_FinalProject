class StatusInformation:
    def __init__(self):
        self.name = ""
        self.pwr = 0
        self.armr = 0
        self.con = 0
        self.lck = 0
        self.total = self.pwr + self.armr + self.con + self.lck
        self.win = 0
        self.maxhp = 100 + (self.con * 1.7)
        self.hp = self.maxhp


class PlayerStatus(StatusInformation):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.exp = 0
        self.maxexp = 100

    def generatePlayer(self):
        self.pwr = float(input("PWR: "))
        self.armr = float(input("ARMR: "))
        self.con = float(input("CON: "))
        self.lck = float(input("LCK: "))
        self.maxhp = 100 + (self.con * 1.7)

    #        self.pwr, self.armr, self.con, self.lck = [float(n) for n in input().split()]
    #        code above was to test if whether this is a better way to input numbers

    def printStats(self):
        test = "PWR: %s \nARMR: %s \nCON %s \nLCK %s" % (self.pwr, self.armr, self.con, self.lck)
        print(test.strip())
        testtotal = [self.pwr, self.armr, self.con, self.lck]
        self.total = sum(testtotal)
        print("Total:", self.total)

    def checkTotal(self):
        return self.total

    # Setters
    def setName(self, name):
        self.name = name

    def setHP(self, health):
        self.hp = health
        return self.hp

    # Getters
    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getMaxHP(self):
        return self.maxhp

    def getPWR(self):
        return self.pwr

    def getARMR(self):
        return self.armr

    def getCON(self):
        return self.con

    def getLCK(self):
        return self.lck


class MonsterStatus(StatusInformation):
    def __init__(self):
        super().__init__()
        self.art = ""

    def generateSlime(self):
        self.name = "Slime"
        self.pwr = 10
        self.armr = 4
        self.con = 5
        self.lck = 1
        self.maxhp = 50 + (self.con * 1.7)
        self.hp = self.maxhp
        self.art = "　　　　 人\n" \
                   "　　　(　ﾟーﾟ)"

    def setHP(self, health):
        self.hp = health
        return self.hp

    # Getters
    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getPWR(self):
        return self.pwr

    def getARMR(self):
        return self.armr

    def getCON(self):
        return self.con

    def getLCK(self):
        return self.lck

    def getArt(self):
        return self.art
