import java.text.MessageFormat;

public class Main
{
    public static void towerOfHanoi(int N, char source, char destination, char temp) {
        if (N == 1) {
            System.out.println(MessageFormat.format("1 moved from {0} to {1}", source, destination));
            return;
        }

        towerOfHanoi(N - 1, source, temp, destination);
        System.out.println(MessageFormat.format("{0} moved from {1} to {2}", N, source, destination));
        towerOfHanoi(N - 1, temp, destination, source);
    }

    public static void main(String[] args) {
        int towerLength = 3;
        char source = 'A';
        char temp = 'B';
        char destination = 'C';

        towerOfHanoi(towerLength, source, destination, temp);
    }
}
