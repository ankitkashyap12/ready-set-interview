# Palindrome Number

- **Problem Number**: #004
- **Difficulty**: Easy
- **Topic**: Math & Number Theory
- **Pattern**: Half-Number Reversal
- **LeetCode Equivalent**: [LC 9: Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Active recall
How do you check if an integer is a palindrome without converting it to a string and avoiding integer overflow?

## Core idea
Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes. Revert only the second half of the number by repeatedly computing revertedNumber = revertedNumber * 10 + x % 10 and x //= 10 until x <= revertedNumber. Then compare x == revertedNumber (even length) or x == revertedNumber // 10 (odd length).

## Hints
- **Hint 1**: Can a negative number ever be a palindrome? What about numbers ending with 0?
- **Hint 2**: Do you need to reverse the entire number, or just half of it?

## Pattern
**Pattern**: Half-Number Reversal
Use when: Math & Number Theory problems require efficient traversal or optimal sub-structure.

## Trick
Stop reversing when x <= revertedNumber. When the original length is odd, the middle digit is discarded via revertedNumber // 10.

## Complexity
Time: O(log10(N)) since we divide by 10 in each step. Space: O(1) auxiliary space.

## Edge cases
- Negative numbers: -121 -> false.
- Ending in zero: 10 -> false, 100 -> false.
- Single digit: 0, 7 -> true.
