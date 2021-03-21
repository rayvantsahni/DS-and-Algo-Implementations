public class Main
{
    public static int binarySearch(int[] arr, int target) {
        return binarySearch(arr, target, 0, arr.length - 1);
    }

    public static int binarySearch(int[] arr, int target, int left, int right) {
        int middle = left + (right - left) / 2;
        if (left > right)
            return -1;
        if (arr[middle] == target)
            return middle;
        else if (target < arr[middle])
            return binarySearch(arr, target, left, middle - 1);
        else if (target > arr[middle])
            return binarySearch(arr, target, middle + 1, right);
        return -1;
    }

    public static void main(String[] args) {
	    int[] arr = {1,3,4,5,6,8,9};
	    int toFind = 8;
        System.out.println(binarySearch(arr, toFind));
    }
}
