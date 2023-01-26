from status import StatusInformation, PlayerStatus, MonsterStatus

class Formulas:

    def attacked(self, pwr, armr, hp, var):
        damage = pwr - armr
        health = hp - damage
        var.setHP(health)
        print(" | %s was attacked and took %d damage! | " % (var.getName(), damage))
