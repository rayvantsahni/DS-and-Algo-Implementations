public class Main
{
    public static String removeCharacter(String word, char toRemove) {
        if (word.length() == 0)
            return word;

        if (word.charAt(0) == toRemove)
            return removeCharacter(word.substring(1), toRemove);
        else
            return word.charAt(0) + removeCharacter(word.substring(1), toRemove);
    }

    public static void main(String[] args) {
        String word = "rayvant";
        char toRemove = 'a';

        System.out.println(removeCharacter(word, toRemove));
    }
}
