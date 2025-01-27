# this is used to disable python formatting on save
# fmt: off

class ECSimulator():
    def __init__(self):
        self.ECMap = dict()
        self.voteResults = [0, 0]
        self.candidateOne = ""
        self.candidateTwo = ""

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
                self.runSim()

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
                print('\nError! Enter the correct input')

    def runSim(self):
        print('\nRunning simulator...')

        self.candidateOne = input("\nEnter the name for candidate one: ")
        self.candidateTwo = input("Enter the name for candidate two: ")

        print("\nWho won each state?")
        print(f"Enter 1 ({self.candidateOne}) or 2 ({self.candidateTwo}).\n")
        choice = 0
        for state, stateECVoteCnt in self.ECMap.items():
            choice = int(input(f"\tWho won {state} ({stateECVoteCnt}): "))

            # candidate 1
            if choice == 1:
                self.voteResults[0] = self.voteResults[0] + stateECVoteCnt
            # candidate 2
            if choice == 2:
                self.voteResults[1] = self.voteResults[1] + stateECVoteCnt

        # display election results
        self.printElectionResults()

    def addNewState(self, newStateName_p, newStateECVoteCnt_p):
        self.ECMap[newStateName_p] = newStateECVoteCnt_p
        print(f'\n{newStateName_p} has been added with {newStateECVoteCnt_p} votes.')
        self.displayMenu()

    def displayECMap(self):
        stateCount = 1
        print('\nDisplaying EC map: ')
        for state, stateECVoteCnt in self.ECMap.items():
            print(f'\t{stateCount}. {state} ({stateECVoteCnt})')
            stateCount += 1
        self.displayMenu()

    def printElectionResults(self):
        # determine either candidate (cand 1 or cand2) has won at least 270 EC votes
        if self.voteResults[0] < 270 or self.voteResults[1] < 270:
            print("\nNeither candidate has achieved at least 270 votes! The House of Representatives will vote on the winner.")

            print(f"\n{self.candidateOne} has won {self.voteResults[0]} votes.")
            print(f"{self.candidateTwo} has won {self.voteResults[1]} votes.")
            return

        # print election results
        print("\nElection results: ")
        print(f"{self.candidateOne} has won {self.voteResults[0]} votes.")
        print(f"{self.candidateTwo} has won {self.voteResults[1]} votes.")

        # display who won the election
        if self.voteResults[0] > self.voteResults[1]:
            print("\n{self.candidateOne} has won the election!")
        if self.voteResults[1] > self.voteResults[0]:
            print("\n{self.candidateTwo} has won the election!")



def main():
    sim = ECSimulator()
    print('Welcome to the Presidential College Vote Simulator!')

    sim.displayMenu()


if __name__ == "__main__":
    main()
