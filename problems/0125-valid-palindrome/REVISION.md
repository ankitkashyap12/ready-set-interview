# Valid Palindrome

- **Problem Number**: #014
- **Difficulty**: Easy
- **Topic**: Two Pointers
- **Pattern**: Two Pointers from Ends with Filter
- **LeetCode Equivalent**: [LC 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## Active recall
How do you determine if a string is a palindrome considering only alphanumeric characters and ignoring cases in O(1) extra space?

## Core idea
Use two pointers left = 0, right = s.length() - 1. While left < right: skip non-alphanumeric chars at left with left++, and at right with right--. Once both point to alphanumeric chars, compare Character.toLowerCase(s[left]) with Character.toLowerCase(s[right]). If mismatch, return false; otherwise advance both.

## Hints
- **Hint 1**: Can you avoid allocating a new filtered string by using two pointers directly?
- **Hint 2**: Use isLetterOrDigit / isalnum to skip punctuation and spaces.

## Pattern
**Pattern**: Two Pointers from Ends with Filter
Use when: Two Pointers problems require efficient traversal or optimal sub-structure.

## Trick
Advance pointers inward over non-alphanumeric characters while ensuring left < right to prevent out-of-bounds indexing.

## Complexity
Time: O(N) single traversal of the string. Space: O(1) auxiliary space.

## Edge cases
- Empty string or string with only spaces/punctuation: " " -> true.
- Single character: "a" -> true.
- Case sensitivity: "0P" -> false ('0' vs 'p').
