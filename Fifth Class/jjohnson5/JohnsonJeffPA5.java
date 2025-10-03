import java.io.BufferedInputStream;
import java.util.Scanner;
import java.util.Stack;
import java.util.Collections;

/**
 * JohnsonJeffPA5
 * Reads integers from standard input, inserts them into a Stack in ascending order,
 * and prints the final sorted list. Input ends when the user types "done"
 *
 * <p>Non-integer tokens (other than "done") are ignored so input can be forgiving.</p>
 *
 * @author Jeff Johnson
 * @version 1.1
 * @since Week 5 of CSC6301
 */
public final class JohnsonJeffPA5 {

    /**
     * Program entry point. Continuously reads tokens from stdin; inserts integers into
     * a Stack; stops on "done"; then prints the sorted stack.
     *
     * @param args command-line arguments 
     */
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        System.out.println("Enter integers. Type 'done' when ready.");
        try (Scanner scanner = new Scanner(new BufferedInputStream(System.in))) {
            while (scanner.hasNext()) {
                if (scanner.hasNextInt()) {
                    int number = scanner.nextInt();
                    stack.push(number);
                    System.out.println("Added " + number + " (current size: " + stack.size() + ")");
                } else {
                    String token = scanner.next();
                    if ("done".equalsIgnoreCase(token)) {
                        break;
                    } else {
                        System.out.println("Ignoring non-integer token: '" + token + "'");
                    }
                }
            }
        }

        // Output
        if (stack.isEmpty()) {
            System.out.println("\nNo numbers were entered.");
        } else {
            // Sort the stack for display
            Collections.sort(stack);
            System.out.println("\nSorted list (" + stack.size() + " total):");
            printSpaceSeparated(stack);
        }
    }

    /**
     * Prints stack elements space-separated followed by a newline.
     *
     * @param stack a stack of integers (may be empty)
     */
    private static void printSpaceSeparated(Stack<Integer> stack) {
        StringBuilder sb = new StringBuilder();
        for (Integer n : stack) {
            sb.append(n).append(' ');
        }
        System.out.println(sb.toString().trim());
    }
}