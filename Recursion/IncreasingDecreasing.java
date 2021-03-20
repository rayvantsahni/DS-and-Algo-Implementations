public class Main
{
    public static void decreasing(int n) {
        if (n == 0)
            return;
        System.out.print(n + " ");
        decreasing(n - 1);
    }

    public static void increasing(int n) {
        if (n == 0)
            return;
        increasing(n - 1);
        System.out.print(n + " ");
    }

    public static void main(String[] args) {
        int n = 7;
        System.out.print("\nIncreasing --> ");
        increasing(n);
        System.out.print("\nDecreasing --> ");
        decreasing(n);

    }
}
