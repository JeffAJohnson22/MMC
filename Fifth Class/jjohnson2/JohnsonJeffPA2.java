/**
 * Demonstrates an optimized implementation of Bubble Sort.
 * @author Jeff Johnson
 * @version 1.0.0
 * @since Week 2 of CSC6301
 */
public class JohnsonJeffPA2 {
    /**
     * Sorts an array of integers using the bubble sort algorithm.
     * @param nums the array of integers to sort
     * @return the sorted array
     * @since Week 2 of CSC6301
     */
    public static int[] bubbleSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            boolean swapped = false;
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                System.out.println("Array is sorted");
                break;
            }
        }
        return array;
    }

    /**
     * The main method demonstrates sorting an array using bubbleSortArray.
     * @param args command-line arguments (not used)
     * @since Week 2 of CSC6301
     */
    public static void main(String[] args) {
        int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};
        int[] sortedArray = bubbleSort(myArray);
        System.out.print("Sorted array: ");
        for (int num : sortedArray) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}