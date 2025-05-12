# this is used to disable python formatting on save
# fmt: off

"""
    HOW TO RUN THE SIMULATOR:
        1. Make sure venv is activated!!!
            a. To do this, Enter the following command: 
                source venv/bin/activate

        2. Enter "python3.9 main.py" to run simulator
"""

import requests

class ECSimulator():
    def __init__(self):
        self.ECMap = dict()
        self.voteResults = [0, 0]
        self.candidateOne = ""
        self.candidateTwo = ""
        self.API_URL = "https://cs499-api.onrender.com/api" 

    def displayMenu(self):
        """
        desc: 
            Displays menu prompt
        """
        self.extractECMap()

        option = 0

        while (option != 3):
            print('\nPlease choose an option:')
            print('\t1. Run simulator')
            print('\t2. Enter custom state')
            print('\t3. Display EC map')
            print('\t4. Quit')
            # for testing #
            print('\t5. *test* candidate one wins')
            print('\t6. *test* candidate two wins')

            try:
                option = int(input('Enter the option: '))

                if option == 1:
                    self.runSim()
                elif option == 2:
                    self.addNewState()
                elif option == 3:
                    self.displayECMap()
                elif option == 4:
                    print('\nGoodbye!')
                    exit()
                ##################                          # for testing
                elif option == 5:
                    self.testCandidateOne()
                elif option == 6:
                    self.testCandidateTwo()
                ##################
                else:
                    print('\nError! Enter the correct input')
            except ValueError:
                print('ERROR: Please use the acceptable inputs (1, 2, 3, 4, 5, 6).')

    def runSim(self):
        """
        desc: 
            Starts the simulator
        """

        print('\nRunning simulator...')

        self.candidateOne = input("\nEnter the name for candidate one: ")
        self.candidateTwo = input("Enter the name for candidate two: ")

        print("\nWho won each state?")
        print(f"Enter 1 ({self.candidateOne}), 2 ({self.candidateTwo}) or 0 to return to the menu.\n")

        choice = 0
        for state, stateECVoteCnt in self.ECMap.items():

            ECVoteSuccessful = False

            while ECVoteSuccessful != True:
                try:
                    choice = int(input(f"\tWho won {state} ({stateECVoteCnt}): "))
                    # candidate 1
                    if choice == 1:
                        self.voteResults[0] = self.voteResults[0] + stateECVoteCnt
                    # candidate 2
                    elif choice == 2:
                        self.voteResults[1] = self.voteResults[1] + stateECVoteCnt
                    # to return to the menu
                    elif choice == 0:
                        self.displayMenu()
                    # raise error if invalid input
                    else:
                        raise ValueError
                    ECVoteSuccessful = True
                except ValueError:
                    print('Error: Please enter acceptable input (1, 2 or 0 to return to the menu).')

        # display election results
        self.printElectionResults()

    def addNewState(self):
        """
        desc: 
            allows the user to add a new state to ECMap
        """
        addedNewState = False

        while addedNewState is not True:
            try:
                newStateName = input('\nEnter new state name: ')
                newStateECVoteCnt = int(input(f'Enter the number of electoral votes for {newStateName}: '))
                addedNewState = True
            except ValueError:
                print('Error: Please enter acceptable input.')

        self.ECMap[newStateName] = newStateECVoteCnt

        print(f'\n{newStateName} has been added with {newStateECVoteCnt} votes.')

        self.displayMenu()

    def displayECMap(self):
        """
        desc: 
            shows contents of electoral college map
        """

        print('\nDisplaying EC map: ')
        stateCount = 1

        for state, stateECVoteCnt in self.ECMap.items():
            print(f'\t{stateCount}. {state} ({stateECVoteCnt})')
            stateCount += 1

        self.displayMenu()

    def printElectionResults(self):
        """
        desc: 
            prints election results in a formatted manner
        """

        # determine either candidate (cand 1 or cand2) has won at least 270 EC votes
        if self.voteResults[0] < 270 and self.voteResults[1] < 270:
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
            print(f"\n{self.candidateOne} has won the election!")
        if self.voteResults[1] > self.voteResults[0]:
            print(f"\n{self.candidateTwo} has won the election!")

    def extractECMap(self):
        """
        desc: 
            makes a GET request to MongoDB, and extracts contents of statesList into ECMap dictionary (hash map)
        """

        # make GET request to MongoDB
        extractECMapURL = self.API_URL

        # print('\nLoading...')
        res = requests.get(extractECMapURL)

        # error handling
        if res.status_code == 200:
            data = res.json()  # list

            # formats contents of res into list (array) format
            statesList = data[0]["states"]

            # extracts contents of statesList into ECMap dictionary (hash map)
            for state in statesList:
                self.ECMap[state["state"]] = state["electoral_votes"]
            # print('\nDone.')
        else:
            print('Error: ', res.status_code)

    # for testing purposes #
    def testCandidateOne(self):
        self.voteResults[0] = 300
        self.voteResults[1] = 0
        self.printElectionResults()

    def testCandidateTwo(self):
        self.voteResults[1] = 300
        self.voteResults[0] = 0
        self.printElectionResults()

def main():
    print('\nNOTE: Program may take a moment to load due to the slow initial run time of Render (the web service provider).')

    print('\nLoading...')

    sim = ECSimulator()
    print('\nWelcome to the Presidential College Vote Simulator!')

    sim.displayMenu()

if __name__ == "__main__":
    main()