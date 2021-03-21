import java.text.MessageFormat;

public class Main
{
//    public static int waysToClimb(int n) {  // steps = 3
//        if (n == 1 || n == 2)
//            return n;
//        if (n == 3)
//            return 1 + waysToClimb(n - 1) + waysToClimb(n - 2);
//        return waysToClimb(n - 1) + waysToClimb(n -2) + waysToClimb(n - 3);
//    }

    public static int waysToClimbStaircase(int n, int k) {
        if (n < 0)
            return 0;
        if (n == 0 || n == 1)
            return 1;
        else {
            int numberOfWays = 0;
            for (int i = 1; i <= k; i++)
                numberOfWays += waysToClimbStaircase(n - i, k);
            return numberOfWays;
        }
    }

    public static void main(String[] args) {
	    int stairCount = 10;
	    int steps = 6;
        System.out.println(MessageFormat.format("Number of Ways to Climb: {0}", waysToClimbStaircase(stairCount, steps)));
    }
}
