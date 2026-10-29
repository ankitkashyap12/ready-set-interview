# LRU Cache

- **Problem Number**: #015
- **Difficulty**: Medium
- **Topic**: Design / Cache
- **Pattern**: Hash Map + Doubly Linked List
- **LeetCode Equivalent**: [LC 146: LRU Cache](https://leetcode.com/problems/lru-cache/)

## Active recall
How do you design a Least Recently Used (LRU) Cache with get and put operations both running in O(1) average time?

## Core idea
Combine a Hash Map (mapping key -> Node) and a Doubly Linked List (with dummy head and dummy tail). The node stores both key and value. get(key): look up in map; if found, move node to head (most recent) and return val. put(key, val): if key exists, update val and move node to head. If new, create node, add to head, insert in map. If capacity exceeded, remove LRU node at tail.prev from both list and map.

## Hints
- **Hint 1**: Hash map gives O(1) lookup, but how can you reorder elements in O(1) time?
- **Hint 2**: A doubly linked list allows removing any node in O(1) if you have its direct reference.

## Pattern
**Pattern**: Hash Map + Doubly Linked List
Use when: Design / Cache problems require efficient traversal or optimal sub-structure.

## Trick
Dummy head and dummy tail nodes eliminate edge cases for empty list and head/tail boundary updates. Store key inside Node so when evicting tail.prev, you can delete map[node.key] in O(1).

## Complexity
Time: O(1) average for both get and put. Space: O(capacity) for the hash map and doubly linked list nodes.

## Edge cases
- Capacity 1: evicts on every insert if unique key.
- Updating existing key value also marks it as most recently used.
- Repeated gets of the same key.
