class ECSimulator():
    def __init__(self):
        self.ECMap = dict()

    def displayMenu(self):
        option = 0

        while (option != 3):
            print('\nPlease choose an option:')
            print('\t1. Run simulator')
            print('\t2. Enter custom state')
            print('\t3. Display EC map')
            print('\t4. Quit')

            option = int(input('Enter the option: '))

            if option == 1:
                print('\nRunning simulator...')

            elif option == 2:
                newStateName = input('\nEnter new state name: ')
                newStateECVoteCnt = int(
                    input(f'Enter the number of electoral votes for {newStateName}: '))

                self.addNewState(newStateName, newStateECVoteCnt)
            elif option == 3:
                self.displayECMap()
            elif option == 4:
                print('\nGoodbye!')
                exit()
            else:
                print('\nerror! enter the correct input')

    def addNewState(self, newStateName_p, newStateECVoteCnt_p):
        self.ECMap[newStateName_p] = newStateECVoteCnt_p
        print(f'\n{newStateName_p} has been added with {
              newStateECVoteCnt_p} votes.')
        self.displayMenu()

    def displayECMap(self):
        stateCount = 1
        print('\nDisplaying EC map: ')
        for state, stateECVoteCnt in self.ECMap.items():
            print(f'\t{stateCount}. {state} ({stateECVoteCnt})')
            stateCount += 1
        self.displayMenu()


def main():
    sim = ECSimulator()
    print('Welcome to the Presidential College Vote Simulator!')

    sim.displayMenu()


if __name__ == "__main__":
    main()
