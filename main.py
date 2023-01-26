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
    while player.getHP() > 0:
            print("A monster appears!")
            monster.generateSlime()
            print("What will you do? \n1. Fight \n2. Run")
            choice = input()
            if choice == "1":
                player.setHP(player.getMaxHP())
                combatSystem(player, monster)
            elif choice == "2":
                print("You have escaped!")
                break



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
        print("Name: %s \nHealth: %d \n" % (monster.getName(), monster.getHP()))
        print("What will you do? \n1. Attack \n2. Flee \n")
        print("Name: %s \nHealth: %d" % (player.getName(), player.getHP()))
        choice = input()
        if choice == "1":
            calc.attacked(player.getPWR(), monster.getARMR(), monster.getHP(), monster)
            calc.attacked(monster.getPWR(), player.getARMR(), player.getHP(), player)
            if monster.getHP() <= 0:
                print("You have defeated %s" % (monster.getName()))
                break
            elif player.getHP() <= 0:
                print("You died")
                break
        elif choice == "2":
            print("You fled!")
            break


while True:
    main()
    print("Continue? \n1. Yes\n2. No")
    choice = input()
    if choice == "1":
        continue
    else:
        break