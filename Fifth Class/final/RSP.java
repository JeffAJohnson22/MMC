import java.util.Random;
import java.util.Scanner;

/**
 * A Rock Scissors Paper game.
 */
public class RSP {
    
    private static final String ROCK = "r";
    private static final String SCISSORS = "s";
    private static final String PAPER = "p";
    
    /**
     * Main method to run the Rock Scissors Paper game.
     * 
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String playerChoice = "";
        
        // Input validation loop
        while (true) {
            System.out.print("Enter (r)ock, (s)cissors, or (p)aper: ");
            playerChoice = scanner.nextLine().toLowerCase().trim();
            
            if (playerChoice.equals(ROCK) || playerChoice.equals(SCISSORS) || playerChoice.equals(PAPER)) {
                break;
            }
            System.out.println("Try again.");
        }
        
        // Generate computer's choice
        String[] choices = {ROCK, SCISSORS, PAPER};
        String computerChoice = choices[new Random().nextInt(3)];
        
        // Determine the winner and display the result
        if (playerChoice.equals(computerChoice)) {
            System.out.println("It's a tie!");
        } else if ((playerChoice.equals(ROCK) && computerChoice.equals(SCISSORS)) ||
                   (playerChoice.equals(PAPER) && computerChoice.equals(ROCK)) ||
                   (playerChoice.equals(SCISSORS) && computerChoice.equals(PAPER))) {
            System.out.println("You win! Computer chose " + computerChoice);
        } else {
            System.out.println("You lose! Computer chose " + computerChoice);
        }
        
        scanner.close();
    }
}