# Valid Parentheses

- **Problem Number**: #007
- **Difficulty**: Easy
- **Topic**: Stack
- **Pattern**: LIFO Matching Stack
- **LeetCode Equivalent**: [LC 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Active recall
How do you verify whether every opening bracket has a correctly matched and ordered closing bracket?

## Core idea
Use a stack. Iterate through characters in the string. When seeing an opening bracket '(', '{', '[', push its corresponding closing bracket ')', '}', ']' onto the stack. When seeing a closing bracket, check if the stack is non-empty and stack.pop() matches it. Return stack.isEmpty() at the end.

## Hints
- **Hint 1**: What data structure preserves the Last-In-First-Out nesting order of brackets?
- **Hint 2**: Push the expected closing bracket when you encounter an opening bracket to make comparison trivial.

## Pattern
**Pattern**: LIFO Matching Stack
Use when: Stack problems require efficient traversal or optimal sub-structure.

## Trick
Pushing the closing bracket onto the stack instead of opening brackets simplifies the comparison: you just check if c == stack.pop().

## Complexity
Time: O(N) scanning string of length N once. Space: O(N) worst case if all opening brackets.

## Edge cases
- Odd length string: immediately false.
- Starts with closing bracket: ")(" -> false.
- All opening brackets: "(((" -> stack not empty -> false.
