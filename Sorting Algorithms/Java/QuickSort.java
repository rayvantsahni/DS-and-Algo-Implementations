import java.util.*;

class QuickSort
{
    public static void quickSort(int[] arr, int start, int end) {
        if (start >= end)
            return;

        int randomIndex = random(start, end);
        swap(arr, randomIndex, end);
        int pivot = end;
        int partitionPoint = start;

        for (int i = start; i < end; i++) {
            if (arr[i] <= arr[pivot]) {
                swap(arr, i, partitionPoint);
                partitionPoint++;
            }
        }

        swap(arr, partitionPoint, end);

        quickSort(arr, start, partitionPoint - 1);
        quickSort(arr, partitionPoint + 1, end);
    }


    private static int random(int max, int min) {
        return (int) (Math.random() * (max - min + 1) + min);
    }


    private static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }


    public static void main(String[] args) {
        int[] array = {20, 5, 10, 25, 19, 16, 4, 0, 2, 11};
        quickSort(array, 0, array.length - 1);
        System.out.println(Arrays.toString(array));
    }
}