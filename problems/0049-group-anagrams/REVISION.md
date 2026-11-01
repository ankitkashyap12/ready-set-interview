# Group Anagrams

- **Problem Number**: #049
- **Difficulty**: Medium
- **Topic**: Arrays & Hashing
- **Pattern**: Canonical Signature Hashing
- **LeetCode Equivalent**: [LC 49: Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **Frequently Asked**: Yes

## Active recall
Given an array of strings, how do you group all anagrams together into sublists efficiently?

## Core idea
Anagrams share the exact same character counts. Two primary ways to form a canonical hash map key:
1. **Sorted String Key**: Sort characters of each string (e.g. "eat" -> "aet"). Use the sorted string as the hash map key. Time: O(N * K log K).
2. **Frequency Count Signature Key**: Count frequencies of each character 'a' through 'z' in an array of size 26. Convert the counts into a delimited string signature (e.g. "1#0#0#...#1#0#"). Use this as the map key. Time: O(N * K).

## Hints
- **Hint 1**: What invariant is shared by all words that are anagrams of each other?
- **Hint 2**: If you map each word to its canonical representation (either sorted characters or a 26-element character count tuple), all anagrams will produce the identical key in a hash table.

## Pattern
**Pattern**: Canonical Signature Hashing
Use when: Items belong to equivalence classes defined by permutation-invariant properties.

## Trick
Using a fixed size array of 26 integers to build a count signature achieves linear O(N * K) time complexity, outperforming O(N * K log K) string sorting when strings are long.

## Complexity
Time: O(N * K) using frequency signature or O(N * K log K) using character sorting, where N is the number of strings and K is the maximum length of a string. Space: O(N * K) auxiliary space to store the grouped strings in the hash map.

## Edge cases
- Array with empty strings: strs = [""] -> [[""]].
- Array with single character strings: strs = ["a"] -> [["a"]].
- All words are distinct with no anagrams: each placed in its own individual list.
- All words are anagrams of one another: all grouped into a single list.
