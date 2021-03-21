import java.text.MessageFormat;
import java.util.Arrays;

public class Main
{
    public static void bubbleSort(int[] arr) {
        bubbleSort(arr, 0, arr.length - 1);
    }

    public static void bubbleSort(int[] arr, int startIndex, int endIndex) {
        if (startIndex == endIndex || endIndex == -1)
            return;

        if (arr[startIndex] > arr[startIndex + 1])
            swap(arr, startIndex, startIndex + 1);
        bubbleSort(arr, startIndex + 1, endIndex);  // equivalent to the Inner Loop

        bubbleSort(arr, startIndex, endIndex - 1);  // equivalent to the Outer Loop
    }

    private static void swap(int[] arr, int firstIndex, int secondIndex) {
        if (firstIndex == secondIndex) return;

        int temp = arr[firstIndex];
        arr[firstIndex] = arr[secondIndex];
        arr[secondIndex] = temp;
    }

    public static void main(String[] args) {
	    int[] arr = {6,8,2,3,4,1,5,4,8};
        System.out.println(MessageFormat.format("Before Sorting: {0}", Arrays.toString(arr)));

        bubbleSort(arr);
        System.out.println(MessageFormat.format("After Sorting: {0}", Arrays.toString(arr)));
    }
}
