import java.io.*;
import java.util.Scanner;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;

class PresidentialECVoteSim {

  static void printFinalResults(String candidateWithMostVotes, Integer candidateWithMostVotesTotal, String candidateWithLeastVotes, Integer candidateWithLeastVotesTotal) {
  // printFinalResults()
    System.out.println("\n================== RESULTS ==================\n");

    // If candidateWithMostVotes does not have at least 270 electoral votes, then they have
    // not won the presidency, and the vote will be sent to the House of Rep.
    if (candidateWithMostVotesTotal >= 270) {
      System.out.println(candidateWithMostVotes + " won the presidency with " + candidateWithMostVotesTotal + " votes!");
    } else {
      System.out.println("Neither candidate has obtained 270 votes! The House of Representatives will vote on the next president.");
      System.out.println(candidateWithMostVotes + " came in top with " + candidateWithMostVotesTotal + " votes!");
    }

    System.out.println(candidateWithLeastVotes + " got " + candidateWithLeastVotesTotal + " votes.");

    System.out.println("\n===========================================");
  }

  public static void main(String[] args) {

    // Lines 9-43 parses the contents from the .CSV file, and adds them into the electoralCollegeMap hashmap
    String file = "./USElectoralMap.csv";
    BufferedReader reader = null;
    String line = "";

    HashMap<String, Integer> electoralCollegeMap = new HashMap<String, Integer>();    // Will store each state with their number of votes

    try {
      // Iterates through entire .CSV file until its empty
      reader = new BufferedReader(new FileReader(file));
      while ((line = reader.readLine()) != null) {
        String[] parts = line.split(",");

        // Divides the contents of the .CSV file into two parts: state and electoralVote
        String state = parts[0].trim();
        String electoralVoteStr = parts[1].trim();

        // If the contents of the .CSV file are not empty, insert them into the electoralCollegeMap hashmap, but exclude the .CSV file's header
        if (!state.equals("") && !state.equals("state") && !electoralVoteStr.equals("")
            && !electoralVoteStr.equals("vote")) {
          Integer electoralVoteInt = Integer.parseInt(electoralVoteStr);
          electoralCollegeMap.put(state, electoralVoteInt);
        }
      }
    } catch (Exception e) {     // Print exception if error is found
      e.printStackTrace();
    } finally {
      try {
        reader.close();           // Close the reader buffer when done
      } catch (IOException e) {
        e.printStackTrace();
      }
    }

    // candidateVoteCount hashmap stores the total votes for each candidate
    HashMap<String, Integer> candidateVoteCount = new HashMap<String, Integer>();

    Scanner getInput = new Scanner(System.in);

    System.out.println("\nWelcome to the Presidential Electoral College Vote Simulator! (created by Bryan Chan 2023)\n");

    System.out.print("Enter candidate #1 name: ");
    String candidateOne = getInput.nextLine();
    System.out.print("Enter candidate #2 name: ");
    String candidateTwo = getInput.nextLine();

    System.out.println(
        "\nFor the following states, enter who won using 1 (" + candidateOne + ") or 2 (" + candidateTwo + ").");
    System.out.println("***For example: Who won Texas (40 electoral votes): 1***");
    System.out.println("\n==========================================\n");

    candidateVoteCount.put(candidateOne, 0);
    candidateVoteCount.put(candidateTwo, 0);

    Integer stateCount = 1;   // Displays state count

    for (Map.Entry<String, Integer> state : electoralCollegeMap.entrySet()) {

      Boolean getUserInput = true;
      while (getUserInput) {
        System.out.print("[" + stateCount + "] Who won " + state.getKey() + " (" + state.getValue() + " electoral votes): ");

        try {
          Integer choice = getInput.nextInt();
          // if the user inputs 1, then add the current state's electoral vote into
          // the candidate's value in the electoralCollegeMap hashmap
          if (choice == 1) {
            candidateVoteCount.replace(candidateOne, candidateVoteCount.get(candidateOne) + state.getValue());
            getUserInput = false;
          // if the user inputs 2, then add the current state's electoral vote into
          // the candidate's value in the electoralCollegeMap hashmap
          } else if (choice == 2) {
            candidateVoteCount.replace(candidateTwo, candidateVoteCount.get(candidateTwo) + state.getValue());
            getUserInput = false;
          }
          else {
            System.out.println("\nTry again.");
            getUserInput = true;
          }
        } catch (Exception e) {
          // if the user enters an integer other than 1 or 2, then the system will ask for
          // the user's input again
          // System.out.println("\nTry again.");
          System.out.println("\nInvalid input (non-interger)!\nTry again.\n");
          getInput.nextLine();
          getUserInput = true;
        }  
      }
      stateCount++;
    }


    // Find out who has the most votes
    String candidateWithMostVotes = "";
    Integer candidateWithMostVotesTotal = 0;
    // Find out who has the least votes
    String candidateWithLeastVotes = "";
    Integer candidateWithLeastVotesTotal = 0;

    // sets candidateWithMostVotes to candidateOne if candidateOne has more votes than candidateTwo
    if (candidateVoteCount.get(candidateOne) > candidateVoteCount.get(candidateTwo)) {
      candidateWithMostVotes = candidateOne;
      candidateWithMostVotesTotal = candidateVoteCount.get(candidateOne);
      candidateWithLeastVotes = candidateTwo;
      candidateWithLeastVotesTotal = candidateVoteCount.get(candidateTwo);

    // sets candidateWithMostVotes to candidateTwo if candidateTwo has more votes than candidateOne
    } else if (candidateVoteCount.get(candidateTwo) > candidateVoteCount.get(candidateOne)) {
      candidateWithMostVotes = candidateTwo;
      candidateWithMostVotesTotal = candidateVoteCount.get(candidateTwo);
      candidateWithLeastVotes = candidateOne;
      candidateWithLeastVotesTotal = candidateVoteCount.get(candidateOne);
    }

    // Prints final result
    printFinalResults(candidateWithMostVotes, candidateWithMostVotesTotal, candidateWithLeastVotes, candidateWithLeastVotesTotal);
    
  }
}
