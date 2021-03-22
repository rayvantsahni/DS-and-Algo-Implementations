import java.util.ArrayList;

public class Main 
{
    public static void printSubsequence(String word, int startIndex, ArrayList<String> subsequences) {
        if (startIndex == word.length()) {
            subsequences.add("");
            return;
        }

        printSubsequence(word, startIndex + 1, subsequences);

        int listSize = subsequences.size();
        for (int i = 0; i < listSize; i++)
            subsequences.add(word.charAt(startIndex) + subsequences.get(i));

    }

    public static void main(String[] args) {
        String word = "abc";
        int numberOfSubsequences = (int) Math.pow(2, word.length());
        ArrayList<String> subsequences = new ArrayList<>(numberOfSubsequences);

        printSubsequence(word, 0, subsequences);
        System.out.println(subsequences);
    }
}
