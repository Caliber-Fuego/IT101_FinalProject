from status import StatusInformation, PlayerStatus, MonsterStatus


def main():
    name = input("Enter your name: ")
    player = PlayerStatus(name)
    playerGenerate(player)



def playerGenerate(player):
    while True:
        try:
            print("Input the STR, ARMR, CON, LCK, of your player in order:")
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