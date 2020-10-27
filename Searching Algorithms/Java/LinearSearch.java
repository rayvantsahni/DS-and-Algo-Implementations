class LinearSearch
{
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++)
            if (arr[i] == target)
                return i;

        return -1;
    }


    public static void main(String[] args) {
        int[] array = {9,3,2,8,4,6,0,7,1};
        System.out.println(linearSearch(array, 7));
    }
}