# Longest Substring Without Repeating Characters

- **Problem Number**: #003
- **Difficulty**: Medium
- **Topic**: Sliding Window
- **Pattern**: Dynamic Sliding Window with Last Seen Map
- **LeetCode Equivalent**: [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Active recall
How do you find the length of the longest substring with all unique characters in linear time?

## Core idea
Use a sliding window [left, right] and a map storing the last seen index of each character. As right expands, if s[right] was seen at or after left, jump left to lastSeen[s[right]] + 1. Update maxLen = max(maxLen, right - left + 1) and record lastSeen[s[right]] = right.

## Hints
- **Hint 1**: Can you expand the window greedily until a duplicate character is encountered?
- **Hint 2**: Instead of shrinking left one step at a time, jump left directly past the previous occurrence of s[right].

## Pattern
**Pattern**: Dynamic Sliding Window with Last Seen Map
Use when: Sliding Window problems require efficient traversal or optimal sub-structure.

## Trick
Always update left with left = max(left, lastSeen[c] + 1) to avoid moving left backwards when encountering an old character from outside the current window.

## Complexity
Time: O(N) where N is string length, right pointer visits each char once. Space: O(min(N, M)) where M is the charset size (e.g. 128 for ASCII).

## Edge cases
- Empty string: "" -> 0.
- All identical characters: "bbbbb" -> 1.
- All distinct characters: "abcdef" -> 6.
- Repeating characters far apart: "tmmzuxt" -> left jump must not move backwards.
