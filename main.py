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
    while True:
        print("A monster appears!")
        monster.generateSlime()
        print("What will you do? \n1. Fight \n2. Run")
        choice = input()
        if choice == "1":
            #TODO: add turn number fix the combat system (add health reduction for player, end combat if either side gets 0 hp)
            while True:
                print("Name:", monster.getName(),"\nHealth:", monster.getHP())
                print("What will you do? \n1. Attack \n2. Flee")
                choice = input()
                if choice == "1":
                    calc.attacked(player.getPWR(), monster.getARMR(), monster.getHP(), monster)
                elif choice == "2":
                    print("You have escaped!")
                    break
        elif choice == "2":
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




main()