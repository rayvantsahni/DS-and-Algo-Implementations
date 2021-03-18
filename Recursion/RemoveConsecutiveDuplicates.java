public class Main 
{

    public static String removeDuplicates(String word) {
        if (word.length() == 1 || word.length() == 0)
            return word;

        if (word.charAt(0) == word.charAt(1))
            return removeDuplicates(word.substring(1));
        else
            return word.charAt(0) + removeDuplicates(word.substring(1));
    }

    public static void main(String[] args) {
	    String word = "aaabcdddaacda";
        System.out.println(removeDuplicates(word));
    }
}
