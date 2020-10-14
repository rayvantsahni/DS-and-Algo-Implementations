import java.util.*;

class SelectionSort
{
    public static void selectionSort(int[] arr) {
        int minValueIndex;
        int temp;
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {  // keeps track of the starting position of the unsorted part of the array, i.e the position where the next smallest element should be put
            minValueIndex = i;  // takes the first element of the unsorted array as the minimum until finds a smaller element
            for (int j = i + 1; j < n; j++)  // loops through all elements of the unsorted part of the array to look for the minimum element
                if (arr[j] < arr[minValueIndex])  // checks if a particular element is smaller than the minimum till now
                    minValueIndex = j;  // stores the index of the minimum element till now

            // swapping the minimum element found in the unsorted part of the array with the first element of the unsorted array such that it becomes a part of the sortedd array
            temp = arr[i];
            arr[i] = arr[minValueIndex];
            arr[minValueIndex] = temp;

        }
    }


    public static void main(String[] args) {
        int[] array = {14,37,1,2,45,24,18,49,9};

        selectionSort(array);  // does not return anything but instead modifies the original array, since Selection Sort is an INPLACE sorting algorithm
        System.out.println(Arrays.toString(array));
    }
}
