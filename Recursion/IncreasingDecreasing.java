public class Main
{
    public static void decreasing(int n) {
        if (n == 1) {
            System.out.println(n);
            return;
        }

        System.out.print(n + " ");
        decreasing(n - 1);
    }

    public static void increasing(int n) {
        increasing(1, n);
    }

    public static void increasing(int n, int target) {
        if (n == target) {
            System.out.println(n);
            return;
        }

        System.out.print(n + " ");
        increasing(n + 1, target);
    }

    public static void main(String[] args) {
        int n = 7;
        System.out.print("Increasing --> ");
        increasing(n);
        System.out.print("Decreasing --> ");
        decreasing(n);

    }
}
