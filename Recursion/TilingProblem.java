//Dimensions of the Wall are - N * 4
//Dimensions of One Tile is - 4 * 1 or 1 * 4

import java.text.MessageFormat;

public class Main
{
    public static int numberOfWays(int n) {
        if (n < 4)
            return 1;
        return numberOfWays(n - 1) + numberOfWays(n - 4);
    }

    public static void main(String[] args) {
        int lengthOfWall = 15;
        System.out.println(MessageFormat.format("Number of Ways to Tile the Wall: {0}", numberOfWays(lengthOfWall)));
    }
}
