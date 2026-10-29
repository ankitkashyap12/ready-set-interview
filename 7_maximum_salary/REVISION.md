# Maximum Salary (Largest Number)

- **Problem Number**: #101
- **Difficulty**: Medium
- **Topic**: Greedy & Custom Sort
- **Pattern**: Concatenation Comparator Sort (ab vs ba)
- **LeetCode Equivalent**: [LC 179: Largest Number](https://leetcode.com/problems/largest-number/)

## Active recall
How do you arrange a list of integers to form the largest possible combined number?

## Core idea
Greedy pairwise comparison: for two numbers a and b (as strings), compare concatenation a + b versus b + a. If a + b > b + a, a should come before b. Sort all numbers using this custom comparator in descending order, then concatenate. If the largest element is '0', the result is '0'.

## Hints
- **Hint 1**: Does comparing single digits work? (e.g. 2 vs 21: 221 > 212, so 2 comes first).
- **Hint 2**: Compare concatenated strings: sort by whether a + b > b + a.

## Pattern
**Pattern**: Concatenation Comparator Sort (ab vs ba)
Use when: Greedy & Custom Sort problems require efficient traversal or optimal sub-structure.

## Trick
Transitivity: the comparison (a + b) > (b + a) defines a strict weak ordering, guaranteeing a globally optimal arrangement.

## Complexity
Time: O(N log N * K) where K is max string length. Space: O(N) to store string representations.

## Edge cases
- All zeros: ['0', '0'] -> return '0' (not '00').
- Numbers with common prefixes: '9' vs '91' -> '991' > '919'.
