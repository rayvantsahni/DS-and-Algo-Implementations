import java.util.*;

class InsertionSort
{
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        int current, j;

        for (int i = 0; i < n; i++) {
            current = arr[i];

            j = i - 1;
            while (j >= 0 && current < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = current;
        }
    }


    public static void main(String[] args) {
        int[] array = {5,8,4,11,17,2,15};
        insertionSort(array);
        System.out.println(Arrays.toString(array));
    }
}