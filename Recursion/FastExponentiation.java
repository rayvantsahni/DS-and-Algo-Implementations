import java.text.MessageFormat;
import java.util.Scanner;

public class Main
{
    public static int power(int base, int exponent) {
        if (exponent == 0 || base == 1)
            return 1;

        int half = power(base, exponent / 2);
        return half * half * ((exponent & 1) == 1 ? base : 1);
    }

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);

        System.out.print("Base.. ");
	    int base = scanner.nextInt();

	    System.out.print("Exponent.. ");
        int exponent = scanner.nextInt();

        System.out.println(MessageFormat.format("{0}^{1} = {2}", base, exponent, power(base, exponent)));
    }
}
