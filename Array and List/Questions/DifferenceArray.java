import java.util.Arrays;
import java.util.Scanner;

class Main
{
    public static void incrementInArray(int[] arr, int size, int[] q) {
        arr[q[0]]++;
        if (q[1] >= size)
            arr[size - 1]--;
        else
            arr[q[1] + 1]--;
    }

    public static void displayResultArray(int[] arr, int size) {
        for (int i = 1; i < size; i++)
            arr[i] += arr[i - 1];
        System.out.println(Arrays.toString(arr));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter array size: ");
        int arraySize = scanner.nextInt();  // length of array
        int[] arr = new int[arraySize];

        System.out.print("Enter number of queries: ");
        int n = scanner.nextInt();  // number of queries

        System.out.println("Enter ranges now..");
        while (n-- > 0)
            incrementInArray(arr, arraySize, new int[] {scanner.nextInt(), scanner.nextInt()});

        displayResultArray(arr, arraySize);
    }
}
