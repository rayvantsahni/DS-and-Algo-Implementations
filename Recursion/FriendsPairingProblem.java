import java.text.MessageFormat;

public class Main
{
    public static int friendsPairing(int n) {
        if (n == 1 || n == 2)
            return n;
        return friendsPairing(n - 1) + (C(n - 1, 1) * friendsPairing(n - 2));
    }

    private static int C(int n, int r) {  // nCr
        return factorial(n) / (factorial(r) * factorial(n - r));
    }

    private static int factorial(int n) {
        if (n == 0 || n == 1)
            return 1;

        int product = 1;
        for (int i = 2; i <= n; i++)
            product *= i;
        return product;
    }

    public static void main(String[] args) {
        int numberOfFriends = 5;
        int numberOfWays = friendsPairing(numberOfFriends);
        System.out.println(MessageFormat.format("Number of ways friends can pair up or go solo: {0}", numberOfWays));
    }
}
