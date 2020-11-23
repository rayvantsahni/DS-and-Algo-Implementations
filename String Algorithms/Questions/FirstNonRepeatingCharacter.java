import java.util.*;
import java.text.*;

class NonRepeating
{
    public static char getFirstNonRepeatingCharacter(String s) {
        if (s.length() == 1)
            return s.charAt(0);

        HashMap<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i) ;
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s.length(); i++)
            if (counter.get(s.charAt(i)) == 1)
                return s.charAt(i);

        return '_';
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string:");
        String string = scanner.nextLine();
        System.out.println(MessageFormat.format("First Non Repeating Character: {0}", getFirstNonRepeatingCharacter(string)));
    }
}