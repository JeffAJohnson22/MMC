// Optimized java implementation of Bubble sort;

/**
 * JohnsonJeffPA2 demonstrates an optimized implementation of Bubble Sort.
 * @author Your Name
 * @version 1.0
 */
public class JohnsonJeffPA2 {
    /**
     * Sorts an array of integers using the bubble sort algorithm.
     * @param nums the array of integers to sort
     * @return the sorted array
     */
    public static int[] bubbleSortArray(int[] nums) {
        for(int i=0; i<nums.length; i++){
            for(int j = 0; j<nums.length-i-1; j++){
                if(nums[j] > nums[j+1]) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }               
            }
        }
        return nums;        
    }

    /**
     * The main method demonstrates sorting an array using bubbleSortArray.
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};
        int[] sortedArray = bubbleSortArray(myArray);
        System.out.print("Sorted array: ");
        for (int num : sortedArray) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}