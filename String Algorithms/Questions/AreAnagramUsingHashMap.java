import java.util.*;
import java.text.MessageFormat;

class Anagram
{
    public static boolean areAnagram(String word1, String word2) {

        if (word1.length() != word2.length())
            return false;

        if ((word1.length() == 0) && (word2.length() == 0))
            return true;

        HashMap<Character, Integer> counter1 = new HashMap<>();
        HashMap<Character, Integer> counter2 = new HashMap<>();

        for (int i = 0; i < word1.length(); i++) {
            char c = word1.charAt(i);
            counter1.put(c, counter1.getOrDefault(c, 0) + 1);

            c = word2.charAt(i);
            counter2.put(c, counter2.getOrDefault(c, 0) + 1);
        }


        return counter1.equals(counter2);
    }



    public static void main(String[] args) {
        String word1 = "integral";
        String word2 = "triangle";

        System.out.println(areAnagram(word1, word2));
        System.out.println(MessageFormat.format("''{0}'' and ''{1}'' are {2}", word1, word2, areAnagram(word1, word2) ? "Anagrams" : "NOT Anagrams"));
    }
}
