import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

class Solution {
    /**
     * Approach 1: Stack using standard Stack class
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;
        Stack<Character> paranthesisStack = new Stack<>();
        char[] paranthesis = s.toCharArray();
        for (char bracket : paranthesis) {
            if (bracket == '{' || bracket == '[' || bracket == '(') {
                paranthesisStack.push(bracket);
            } else {
                if (paranthesisStack.isEmpty()) {
                    return false;
                }
                char lastBracket = paranthesisStack.pop();
                if (bracket == '}' && lastBracket != '{') {
                    return false;
                }
                if (bracket == ')' && lastBracket != '(') {
                    return false;
                }
                if (bracket == ']' && lastBracket != '[') {
                    return false;
                }
            }
        }
        return paranthesisStack.isEmpty();
    }

    /**
     * Approach 2: Lightweight Primitive Array Stack (Ultra High Performance)
     * Avoids object boxing overhead of Character wrapper and synchronization of java.util.Stack.
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public boolean isValidFast(String s) {
        if (s.length() % 2 != 0) return false;
        char[] stack = new char[s.length()];
        int top = -1;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack[++top] = ')';
            } else if (c == '{') {
                stack[++top] = '}';
            } else if (c == '[') {
                stack[++top] = ']';
            } else {
                if (top == -1 || stack[top--] != c) {
                    return false;
                }
            }
        }
        return top == -1;
    }
}