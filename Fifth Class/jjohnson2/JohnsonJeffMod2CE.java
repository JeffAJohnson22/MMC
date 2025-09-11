import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        System.out.println("This program computes the square of an Integer.");
        System.out.println();
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an Integer: ");
        int n = sc.nextInt();
        int acc = 0;
        int odd = 1;
        for (int i = 0; i < n; i++) {
            acc += odd;
            odd += 2;
        }
        sc.close();
        System.out.println("The square of " + n + " is " + acc);
    }
}

