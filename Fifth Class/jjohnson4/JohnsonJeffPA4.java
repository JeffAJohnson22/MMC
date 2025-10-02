import java.io.BufferedInputStream;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;

/**
 * JohnsonJeffPA4
 * Reads integers from standard input, inserts them into a LinkedList in ascending order,
 * and prints the final sorted list. Input ends when the user types "done"
 *
 * <p>Non-integer tokens (other than "done") are ignored so input can be forgiving.</p>
 *
 * @author Jeff Johnson
 * @version 1.1
 * @since Week 4 of CSC6301
 */
public final class JohnsonJeffPA4 {

    /**
     * Program entry point. Continuously reads tokens from stdin; inserts integers into
     * a sorted LinkedList; stops on "done"; then prints the list.
     *
     * @param args command-line arguments 
     */
    public static void main(String[] args) {
        // LinkedList<Integer> — reuses Java’s built-in list implementation instead of writing your own:
        LinkedList<Integer> sortedList = new LinkedList<>();

        System.out.println("Enter integers. Type 'done' when ready.");
        // Scanner + BufferedInputStream(System.in) — reuses Java’s tokenization + buffering pattern for robust stdin reading
        try (Scanner scanner = new Scanner(new BufferedInputStream(System.in))) {
            while (scanner.hasNext()) {
                if (scanner.hasNextInt()) {
                    int number = scanner.nextInt();
                    insertSorted(sortedList, number);
                    System.out.println("Added " + number + " (current size: " + sortedList.size() + ")");
                } else {
                    String token = scanner.next();
                    if ("done".equalsIgnoreCase(token)) {
                        break;
                    } else {
                        // Keeps reading; ignore minor noise.
                        System.out.println("Ignoring non-integer token: '" + token + "'");
                    }
                }
            }
        }

        // Output
        if (sortedList.isEmpty()) {
            System.out.println("\nNo numbers were entered.");
        } else {
            System.out.println("\nSorted list (" + sortedList.size() + " total):");
            printSpaceSeparated(sortedList);
        }
    }

    /**
     * Inserts {@code value} into {@code list} while maintaining ascending sort order.
     * This uses a {@link ListIterator} to avoid random-access calls on {@link LinkedList}.
     *
     * @param list  a non-null LinkedList kept in ascending order
     * @param value the integer to insert
     * @throws NullPointerException if {@code list} is null
     */
    private static void insertSorted(LinkedList<Integer> list, int value) {
        if (list == null) throw new NullPointerException("list cannot be null");

        ListIterator<Integer> it = list.listIterator();
        while (it.hasNext()) {
            if (value <= it.next()) {
                // Step back one position and insert before the larger/equal element we just saw.
                it.previous();
                it.add(value);
                return;
            }
        }
        // If we reached the end, append.
        it.add(value);
    }

    /**
     * Prints list elements space-separated followed by a newline.
     *
     * @param list a list of integers (may be empty)
     */
    private static void printSpaceSeparated(LinkedList<Integer> list) {
        StringBuilder sb = new StringBuilder();
        for (Integer n : list) {
            sb.append(n).append(' ');
        }
        System.out.println(sb.toString().trim());
    }
}
