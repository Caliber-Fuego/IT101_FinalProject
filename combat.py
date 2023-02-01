from status import StatusInformation, PlayerStatus, MonsterStatus
import random

class Formulas:

    def attacked(self, pwr, armr, hp, lck, var):
        damage = max(0, pwr - armr)
        health = hp - damage
        dodgeRoll = random.randint(0, 100)

        if dodgeRoll <= lck:
            print(" | %s successfully dodged the attack! | " % (var.name))
        else:
            var.setHP(health)
            print(" | %s was attacked and took %d damage! | " % (var.name, damage))

    def expoints(self, xpdrop, playerxp, player):
        addexp = playerxp + xpdrop
        print("You have received %d exp!" % (xpdrop))
        player.setEXP(addexp)

    def monster_strengthening(self, monster, win):
        monster.setPWR(monster.pwr + (win/2))
        monster.setARMR(monster.armr + (win/2))
        monster.setCON(monster.con + (win/2))
        monster.setLCK(monster.lck + (win/2))







