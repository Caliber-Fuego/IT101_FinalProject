from status import StatusInformation, PlayerStatus, MonsterStatus
from combat import Formulas

calc = Formulas()


def main():
    name = input("Enter your name: ")
    player = PlayerStatus()
    monster = MonsterStatus()
    player.setName(name)
    while True:
        playerGenerate(player)
        if player.checkTotal() > 25:
            print("Total stats is greater than 25!")
        else:
            break
    while player.hp > 0:
        print("A monster appears!")
        monster.generateSlime(player.win)
        print("What will you do? \n1. Fight \n2. Run \n3. Check Stats")
        choice = input()
        if choice == "1":
            player.setHP(player.getMaxHP())
            combatSystem(player, monster)
        elif choice == "2":
            print("You have escaped!")
            break
        elif choice == "3":
            player.printStats()


def playerGenerate(player):
    while True:
        try:
            print("Input the STR, ARMR, CON, LCK, of your player in order: "
                  "\n(Note: the total of the stats must be exactly 25 or below that)")
            player.generatePlayer()
            player.printStats()
            print("Is this the stats you want? \n1. Yes \n2. No")
            choice = input()
            if choice == "2":
                print("\n")
            elif choice == "1":
                break
        except ValueError:
            print("Please input only a single integer")
            pass


def combatSystem(player, monster):
    while True:
        print(monster.getArt())
        print("Name: %s \nHealth: %d \n" % (monster.name, monster.hp))
        print("Name: %s \nHealth: %d \n" % (player.name, player.hp))
        print("What will you do? \n1. Attack \n2. Flee")

        choice = input()
        if choice == "1":
            calc.attacked(player.pwr, monster.armr, monster.hp, monster.lck, monster)
            calc.attacked(monster.pwr, player.armr, player.hp, player.lck, player)
            if monster.hp <= 0:
                print("You have defeated %s" % (monster.name))
                player.setWIN(player.win + 1)
                calc.expoints(monster.xpdrop, player.exp, player)
                if player.exp >= player.maxexp:
                    sp = 2
                    player.setLVL(player.level + 1)
                    player.setmaxEXP(player.maxexp * 1.5)
                    print("%s is now level %d!" % (player.name, player.level))
                    while sp != 0:
                        statadd(player)
                        sp -= 1
                else:
                    pass

                break
            elif player.hp <= 0:
                print("You died")
                break
        elif choice == "2":
            print("You fled!")
            break


def statadd(player):
    print("Choose 2 stats to increase! \n1. PWR \n2. ARMR \n3. CON \n4. LCK")
    choice = input()
    if choice == "1":
        player.setPWR(player.pwr + 1)

    elif choice == "2":
        player.setARMR(player.armr + 1)

    elif choice == "3":
        player.setCON(player.con + 1)

    elif choice == "4":
        player.setLCK(player.lck + 1)


while True:
    main()
    print("Continue? \n1. Yes\n2. No")
    choice = input()
    if choice == "1":
        continue
    else:
        break
