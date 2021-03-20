import java.text.MessageFormat;
import java.util.Arrays;

public class Main {
    public static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    public static void quickSort(int[] arr, int left, int right) {
        if (left >= right)
            return;
        
        int randomIndex = left + (int)(Math.random() * (right - left + 1));
        swap(arr, randomIndex, right);
        int pivotIndex = right;
        int partitionIndex = left;
        
        for (int i = left; i < right; i++)
            if (arr[i] <= arr[pivotIndex])
                swap(arr, i, partitionIndex++);

        swap(arr, partitionIndex, right);

        quickSort(arr, left, partitionIndex - 1);
        quickSort(arr, partitionIndex + 1, right);
    }

    private static void swap(int[] arr, int firstIndex, int secondIndex) {
        if (firstIndex == secondIndex)
            return;
        int temp = arr[firstIndex];
        arr[firstIndex] = arr[secondIndex];
        arr[secondIndex] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {8,1,2,4,9,7,6,3};
        System.out.println(MessageFormat.format("Before Sorting: {0}",Arrays.toString(arr)));

        quickSort(arr);
        System.out.println(MessageFormat.format("After Sorting: {0}",Arrays.toString(arr)));
    }
}
