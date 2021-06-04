public class Main
{
    public static void coinToss(int n) {
        coinToss(n, "");
    }

    public static void coinToss(int n, String current) {
        if (n == current.length()) {
            System.out.println(current);
            return;
        }

        coinToss(n, "H" + current);
        coinToss(n, "T" + current);
    }

    public static void main(String[] args) {
        int n = 3;
        coinToss(n);
    }
}
