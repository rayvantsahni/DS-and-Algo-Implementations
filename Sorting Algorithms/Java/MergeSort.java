import java.text.MessageFormat;
import java.util.Arrays;

public class Main
{
    public static void mergeSort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
    }

    public static void mergeSort(int[] arr, int left, int right) {
        if (left >= right)
            return;

        int middle = left + (right - left ) / 2;
        mergeSort(arr, left, middle); 
        mergeSort(arr, middle + 1, right);

        merge(arr, left, right);
    }

    private static void merge(int[] arr, int left, int right) {
        int middle = left + (right - left) / 2;
        int leftIndex = left;
        int rightIndex = middle + 1;
        int sortedArrayIndex = 0;
        int[] sortedArray = new int[right - left + 1];

        while (leftIndex <= middle && rightIndex <= right) {
            if (arr[leftIndex] <= arr[rightIndex])
                sortedArray[sortedArrayIndex++] = arr[leftIndex++];
            else
                sortedArray[sortedArrayIndex++] = arr[rightIndex++];
        }

        while (leftIndex <= middle)
            sortedArray[sortedArrayIndex++] = arr[leftIndex++];
        while (rightIndex <= right)
            sortedArray[sortedArrayIndex++] = arr[rightIndex++];

        for (int i = 0; i < sortedArray.length; i++)
            arr[left + i] = sortedArray[i];

    }

    public static void main(String[] args) {
        int[] arr = {6,4,3,9,1,8,5,7};
        System.out.println(MessageFormat.format("Before Sorting: {0}", Arrays.toString(arr)));

        mergeSort(arr);
        System.out.println(MessageFormat.format("After Sorting: {0}", Arrays.toString(arr)));
    }
}
