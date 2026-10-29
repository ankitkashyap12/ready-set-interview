import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        return optimizedJumpMap(s);
    }

    /**
     * Approach 1: Sliding Window with Direct Index Jumping (Optimal)
     * Instead of shrinking the window one character at a time using a Set,
     * store the last seen position of each character. When a duplicate is seen,
     * jump the left pointer directly past the previous occurrence.
     * Time Complexity: O(n) - exactly n iterations.
     * Space Complexity: O(min(m, n)) or O(1) for standard ASCII table (128 chars).
     */
    int optimizedJumpMap(String s) {
        if (s == null || s.length() == 0) return 0;
        int[] lastIndex = new int[128];
        Arrays.fill(lastIndex, -1);
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (lastIndex[c] >= left) {
                left = lastIndex[c] + 1; // Direct jump
            }
            lastIndex[c] = right;
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }

    /**
     * Approach 2: Sliding Window with HashSet (Standard)
     * Expands right pointer and contracts left pointer one by one.
     * Time Complexity: O(2n) = O(n)
     * Space Complexity: O(min(m, n))
     */
    int optimizedSlidingWindow(String s) {
        int left = 0;
        int right = 0;
        if (s.length() == 0)
            return 0;

        int maxSize = 0;
        Set<Character> seenChar = new HashSet<>();
        for (right = 0; right < s.length(); right++) {
            while (seenChar.contains(s.charAt(right))) {
                seenChar.remove(s.charAt(left));
                left++;
            }
            seenChar.add(s.charAt(right));
            maxSize = Math.max(maxSize, right - left + 1);
        }
        return maxSize;
    }

    /**
     * Approach 3: Brute Force
     * Time Complexity: O(n^2)
     * Space Complexity: O(n)
     */
    int bruteSlidingWindow(String s) {
        int len = s.length();
        if (len == 0)
            return 0;

        Set<Character> uniqueCharInSubStr = new HashSet<>();
        int maxSize = 0;
        for (int firstPt = 0; firstPt < len; firstPt++) {
            char startChar = s.charAt(firstPt);
            uniqueCharInSubStr.add(startChar);
            int secondPt = firstPt + 1;
            StringBuilder sb = new StringBuilder();
            sb.append(startChar);
            while (secondPt < len && uniqueCharInSubStr.add(s.charAt(secondPt))) {
                sb.append(s.charAt(secondPt));
                secondPt++;
            }
            uniqueCharInSubStr.clear();
            maxSize = Math.max(maxSize, sb.toString().length());
        }
        return maxSize;
    }
}