import java.util.*;

class BubbleSort
{
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        int temp;
        boolean isSorted = true;

        for (int i = 0; i < n; i++) {  // loops over all the elements of the array until the whole array is sorted
            isSorted = true;  // works as a flag to check whether the array still has any out of order elements

            for (int j = 1; j < n - i; j++)  // loops over the elements of the unsorted part of the array
                if (arr[j - 1] > arr[j]) {  // checks the consecutive elements in the array to see if they are out of order relative to each other
                    swap(arr, j - 1, j);  // if adjacent elements are out of order they are swapped
                    isSorted = false;  // indicates that the array is still not fully sorted and we need to further iterate to sort the array
                }

            if (isSorted)  // checks if the array has been sorted already or not
                return;  // if the array is sorted prematurely, i.e before we iterate over all elements to place them in their correct positions
        }
    }


    // swaps two adjacent elements to restore relative ordering amongst them
    private static void swap(int[] arr, int left, int right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
    }


    public static void main(String[] args) {
        int[] array = {27, 15, 1, 22, 8, 26, 13};

        bubbleSort(array);  // does not return anything but instead modifies the original array, since Bubble Sort is an INPLACE sorting algorithm
        System.out.println(Arrays.toString(array));
    }
}







