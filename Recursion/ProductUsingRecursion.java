public class Main
{
    private static int productHelper(int firstNumber, int secondNumber) {
        if (secondNumber == 1)
            return firstNumber;
        return firstNumber + productHelper(firstNumber, secondNumber - 1);
    }

    public static int product(int firstNumber, int secondNumber) {
        if (firstNumber == 0 || secondNumber == 0)
            return 0;
        if (firstNumber < 0 && secondNumber < 0)
            return productHelper(-Math.min(firstNumber, secondNumber), -Math.max(firstNumber, secondNumber));
        if (firstNumber < 0)
            return productHelper(firstNumber, secondNumber);
        if (secondNumber < 0)
            return productHelper(secondNumber, firstNumber);
        else
            return productHelper(Math.max(firstNumber, secondNumber), Math.min(firstNumber, secondNumber));
    }

    public static void main(String[] args) {
        int a = 80;
        int b = -70;
        System.out.println(product(a, b));
    }
}
