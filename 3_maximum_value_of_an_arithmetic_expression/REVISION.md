# Maximum Value of an Arithmetic Expression

- **Problem Number**: #088
- **Difficulty**: Hard
- **Topic**: Dynamic Programming
- **Pattern**: Interval DP / Matrix Chain Placing Parentheses
- **LeetCode Equivalent**: [LC 241: Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

## Active recall
Given an arithmetic expression with numbers and +, -, * operators, how do you parenthesize it to maximize its final value?

## Core idea
Maintain two 2D tables: minVal[i][j] and maxVal[i][j] for the sub-expression from number i to number j. For expression length s = 1 to n: for each start i and end j = i + s: iterate split point k between i and j - 1. Compute all 4 combinations of minVal and maxVal around operator at k (min*min, min*max, max*min, max*max). Update maxVal[i][j] and minVal[i][j] with overall max and min. Return maxVal[0][n-1].

## Hints
- **Hint 1**: Why do we need BOTH minimum and maximum values? Because multiplying two negative numbers can yield a large positive number!
- **Hint 2**: Solve sub-expressions in increasing order of length (interval DP).

## Pattern
**Pattern**: Interval DP / Matrix Chain Placing Parentheses
Use when: Dynamic Programming problems require efficient traversal or optimal sub-structure.

## Trick
Always track both minimum and maximum values for each sub-expression because subtraction of a minimum or multiplication of two negative minimums can produce a maximum.

## Complexity
Time: O(N^3) where N is number of digits. Space: O(N^2) for min and max DP tables.

## Edge cases
- Expression with single number: maxVal[0][0] = digit.
- All subtraction operators: double negatives flip signs.
- Multiplication of negative values.
