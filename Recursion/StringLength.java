class StringLength
{
    public static int lengthOfString(String word, int index) {
        if (index == word.length() - 1)
            return 1;
        return 1 + lengthOfString(word, index + 1);
    }

    public static void main(String[] args) {
        String word = args[0];
        System.out.println(lengthOfString(word, 0));
    }
}
