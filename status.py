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
        self.level = 1
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
        print("EXP: %d/%d" % (self.exp, self.maxexp))
        print("Victories: %d" % (self.win))

    def checkTotal(self):
        return self.total

    # Setters
    def setName(self, name):
        self.name = name

    def setHP(self, health):
        self.hp = health
        return self.hp

    def setEXP(self, exp):
        self.exp = exp
        return self.exp

    def setmaxEXP(self, maxexp):
        self.maxexp = maxexp
        return self.maxexp

    def setPWR(self, pwr):
        self.pwr = pwr
        return self.pwr

    def setARMR(self, armr):
        self.armr = armr
        return self.armr

    def setCON(self, con):
        self.con = con
        return self.con

    def setLCK(self, lck):
        self.lck = lck
        return self.lck

    def setLVL(self, lvl):
        self.level = lvl
        return self.level

    def setWIN(self, win):
        self.win = win
        return self.win

    def getMaxHP(self):
        self.maxhp = 100 + (self.con * 1.7)
        return self.maxhp

class MonsterStatus(StatusInformation):
    def __init__(self):
        super().__init__()
        self.art = ""
        self.xpdrop = 0

    def generateSlime(self, win):
        self.name = "Slime"
        self.pwr = (10 + (win/2))
        self.armr = (4 + (win/2))
        self.con = (5 + (win/2))
        self.lck = (1 + (win/2))
        self.maxhp = 50 + (self.con * 1.7)
        self.hp = self.maxhp
        self.xpdrop = 50
        self.art = "　　　　 人\n" \
                   "　　　(　ﾟーﾟ)"

    def setHP(self, health):
        self.hp = health
        return self.hp
    def getMaxHP(self):
        self.maxhp = 100 + (self.con * 1.7)
        return self.maxhp

    def getArt(self):
        return self.art


