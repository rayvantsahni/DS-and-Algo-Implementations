import java.util.*;

class ValidParentheses
{
    public static boolean validParentheses(String s) {
        if (s.length() == 0)
            return true;

        if (s.length() == 1)
            return false;

        HashMap<Character, Character> pairs = new HashMap<>();
        pairs.put('{', '}');
        pairs.put('(', ')');
        pairs.put('[', ']');

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (pairs.containsKey(s.charAt(i)))
                stack.push(s.charAt(i));

            else if (s.charAt(i) != pairs.get(stack.pop()))
                return false;
        }

        return stack.empty();

    }
    public static void main(String[] args) {
        String string = "{{}}()[()]";
        System.out.println(validParentheses(string));
    }
}
