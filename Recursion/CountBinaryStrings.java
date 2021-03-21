public class Main
{
    public static int countBinaryStrings(int n) {
        if (n == 1)
            return 2;
        if (n == 2)
            return 3;
        return countBinaryStrings(n - 1) + countBinaryStrings(n - 2);
    }

    public static void main(String[] args) {
        int stringLength = 9;
        System.out.println(countBinaryStrings(stringLength));
    }
}
