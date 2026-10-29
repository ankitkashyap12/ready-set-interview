#!/usr/bin/env python3
"""Generate rich REVISION.md files and metadata registry for all 102 problems."""

from pathlib import Path
import json

# Complete definitions for all 102 problems
PROBLEMS_DATA = [
    # -------------------------------------------------------------
    # 1. LEETCODE PROBLEMS (Folders 1 to 27)
    # -------------------------------------------------------------
    {
        "folder": "0001-two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Hash Map Complement Lookup",
        "lc_number": 1,
        "lc_title": "Two Sum",
        "lc_url": "https://leetcode.com/problems/two-sum/",
        "recall": "Given an array of integers and a target sum, how do you find the indices of the two numbers that add up to target in O(N) time?",
        "concept": "Traverse the array once while maintaining a hash map of seen numbers to their indices. For each element num at index i, check if complement = target - num already exists in the map. If found, return [map[complement], i]. Otherwise, store map[num] = i.",
        "hints": [
            "What value would complete the pair with the current element nums[i]?",
            "Can you look up previously visited values in O(1) time using a hash map before inserting the current one?"
        ],
        "trick": "Query the hash map for complement BEFORE inserting nums[i]. This prevents pairing an element with itself and handles duplicate numbers naturally.",
        "complexity": "Time: O(N) single pass through the array. Space: O(N) auxiliary space to store up to N entries in the hash map.",
        "edge_cases": [
            "Exactly two elements matching target: [3, 3], target = 6.",
            "Negative numbers and zero: [-3, 4, 3, 90], target = 0.",
            "Target sum requires large integer values."
        ]
    },
    {
        "folder": "1-two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Hash Map Complement Lookup",
        "lc_number": 1,
        "lc_title": "Two Sum",
        "lc_url": "https://leetcode.com/problems/two-sum/",
        "recall": "How can you solve Two Sum in O(N) time and O(N) space using one single forward pass?",
        "concept": "Maintain a hash table mapping each visited value to its index. For each number, compute complement = target - num. If complement is in the map, return the stored index and current index. Otherwise, record map[num] = index.",
        "hints": [
            "Do you need to sort the array? Sorting takes O(N log N) and loses original indices unless paired.",
            "Check complement existence before recording the current element."
        ],
        "trick": "Single-pass hash table check-then-insert guarantees you never reuse the same index.",
        "complexity": "Time: O(N) average time for hash table operations. Space: O(N) for the hash map.",
        "edge_cases": [
            "Duplicate values forming target: [3, 3] target 6.",
            "Array with negative values."
        ]
    },
    {
        "folder": "0003-longest-substring-without-repeating-characters",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "topic": "Sliding Window",
        "pattern": "Dynamic Sliding Window with Last Seen Map",
        "lc_number": 3,
        "lc_title": "Longest Substring Without Repeating Characters",
        "lc_url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        "recall": "How do you find the length of the longest substring with all unique characters in linear time?",
        "concept": "Use a sliding window [left, right] and a map storing the last seen index of each character. As right expands, if s[right] was seen at or after left, jump left to lastSeen[s[right]] + 1. Update maxLen = max(maxLen, right - left + 1) and record lastSeen[s[right]] = right.",
        "hints": [
            "Can you expand the window greedily until a duplicate character is encountered?",
            "Instead of shrinking left one step at a time, jump left directly past the previous occurrence of s[right]."
        ],
        "trick": "Always update left with left = max(left, lastSeen[c] + 1) to avoid moving left backwards when encountering an old character from outside the current window.",
        "complexity": "Time: O(N) where N is string length, right pointer visits each char once. Space: O(min(N, M)) where M is the charset size (e.g. 128 for ASCII).",
        "edge_cases": [
            "Empty string: \"\" -> 0.",
            "All identical characters: \"bbbbb\" -> 1.",
            "All distinct characters: \"abcdef\" -> 6.",
            "Repeating characters far apart: \"tmmzuxt\" -> left jump must not move backwards."
        ]
    },
    {
        "folder": "0009-palindrome-number",
        "title": "Palindrome Number",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Half-Number Reversal",
        "lc_number": 9,
        "lc_title": "Palindrome Number",
        "lc_url": "https://leetcode.com/problems/palindrome-number/",
        "recall": "How do you check if an integer is a palindrome without converting it to a string and avoiding integer overflow?",
        "concept": "Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes. Revert only the second half of the number by repeatedly computing revertedNumber = revertedNumber * 10 + x % 10 and x //= 10 until x <= revertedNumber. Then compare x == revertedNumber (even length) or x == revertedNumber // 10 (odd length).",
        "hints": [
            "Can a negative number ever be a palindrome? What about numbers ending with 0?",
            "Do you need to reverse the entire number, or just half of it?"
        ],
        "trick": "Stop reversing when x <= revertedNumber. When the original length is odd, the middle digit is discarded via revertedNumber // 10.",
        "complexity": "Time: O(log10(N)) since we divide by 10 in each step. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Negative numbers: -121 -> false.",
            "Ending in zero: 10 -> false, 100 -> false.",
            "Single digit: 0, 7 -> true."
        ]
    },
    {
        "folder": "0011-container-with-most-water",
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Inward Shrinking Two Pointers",
        "lc_number": 11,
        "lc_title": "Container With Most Water",
        "lc_url": "https://leetcode.com/problems/container-with-most-water/",
        "recall": "How do you find two vertical lines that together with the x-axis hold the most water in O(N) time?",
        "concept": "Start with two pointers at opposite ends (left = 0, right = n - 1). The area is min(height[left], height[right]) * (right - left). Since width decreases as pointers move inward, the only way to find a larger area is to seek a taller boundary by moving the pointer with the smaller height inward.",
        "hints": [
            "Width is maximized at the very ends. What happens to the width as you move pointers inward?",
            "Which pointer should you move inward: the shorter line or the taller line?"
        ],
        "trick": "Always move the pointer pointing to the shorter vertical bar. Keeping the shorter bar and moving the taller bar can only decrease width without any chance of increasing the limiting height.",
        "complexity": "Time: O(N) because left and right converge in N - 1 steps. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Two lines only: [1, 1] -> 1.",
            "Strictly increasing or decreasing heights: [1, 2, 3, 4, 5].",
            "Plateau of equal heights: [4, 4, 4, 4]."
        ]
    },
    {
        "folder": "0015-3sum",
        "title": "3Sum",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Sort + Fixed Pivot + Two Pointers",
        "lc_number": 15,
        "lc_title": "3Sum",
        "lc_url": "https://leetcode.com/problems/3sum/",
        "recall": "How do you find all unique triplets in an array that sum to zero in O(N^2) time without duplicate triplets?",
        "concept": "Sort the array. Iterate pivot i from 0 to n - 3. If nums[i] > 0, stop early (three positive numbers cannot sum to 0). Skip duplicate pivots if nums[i] == nums[i-1]. For each i, run two pointers left = i + 1, right = n - 1. If sum == 0, record triplet and advance both pointers past duplicate values. If sum < 0, advance left; if sum > 0, decrement right.",
        "hints": [
            "Can sorting simplify finding pairs and skipping duplicates?",
            "Fix the first element, then reduce the problem to 2Sum on the remaining sorted sub-array."
        ],
        "trick": "Duplicate elimination: skip duplicate pivots (i > 0 and nums[i] == nums[i-1]) and skip duplicates for left and right after finding a valid triplet.",
        "complexity": "Time: O(N^2) total (O(N log N) sort + O(N) iterations of O(N) two pointers). Space: O(log N) or O(N) for sorting depending on language.",
        "edge_cases": [
            "Fewer than 3 elements: [] or [0, 1] -> [].",
            "All zeros: [0, 0, 0, 0] -> [[0, 0, 0]].",
            "No valid triplets: [-1, -2, -3, 0]."
        ]
    },
    {
        "folder": "0020-valid-parentheses",
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "topic": "Stack",
        "pattern": "LIFO Matching Stack",
        "lc_number": 20,
        "lc_title": "Valid Parentheses",
        "lc_url": "https://leetcode.com/problems/valid-parentheses/",
        "recall": "How do you verify whether every opening bracket has a correctly matched and ordered closing bracket?",
        "concept": "Use a stack. Iterate through characters in the string. When seeing an opening bracket '(', '{', '[', push its corresponding closing bracket ')', '}', ']' onto the stack. When seeing a closing bracket, check if the stack is non-empty and stack.pop() matches it. Return stack.isEmpty() at the end.",
        "hints": [
            "What data structure preserves the Last-In-First-Out nesting order of brackets?",
            "Push the expected closing bracket when you encounter an opening bracket to make comparison trivial."
        ],
        "trick": "Pushing the closing bracket onto the stack instead of opening brackets simplifies the comparison: you just check if c == stack.pop().",
        "complexity": "Time: O(N) scanning string of length N once. Space: O(N) worst case if all opening brackets.",
        "edge_cases": [
            "Odd length string: immediately false.",
            "Starts with closing bracket: \")(\" -> false.",
            "All opening brackets: \"(((\" -> stack not empty -> false."
        ]
    },
    {
        "folder": "0056-merge-intervals",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "topic": "Intervals",
        "pattern": "Sort by Start Time + Greedy Merge",
        "lc_number": 56,
        "lc_title": "Merge Intervals",
        "lc_url": "https://leetcode.com/problems/merge-intervals/",
        "recall": "Given a collection of intervals, how do you merge all overlapping intervals into non-overlapping ones?",
        "concept": "Sort intervals by start time intervals.sort(key=lambda x: x[0]). Initialize merged list with the first interval. For each subsequent interval, if current.start <= merged.last.end, merge by updating merged.last.end = max(merged.last.end, current.end). Otherwise, append current as a new interval.",
        "hints": [
            "If intervals are sorted by start time, when does interval B overlap with interval A?",
            "Keep updating the end of the current merged interval using max(endA, endB)."
        ],
        "trick": "Always use max(merged.last.end, current.end) because an interval may be completely subsumed inside the previous one (e.g. [1, 5] and [2, 3]).",
        "complexity": "Time: O(N log N) dominated by sorting. Space: O(N) to store merged intervals or O(log N) sorting space.",
        "edge_cases": [
            "Single interval: [[1, 4]] -> [[1, 4]].",
            "Interval completely inside another: [[1, 6], [2, 4]] -> [[1, 6]].",
            "Touching boundaries: [[1, 4], [4, 5]] -> [[1, 5]]."
        ]
    },
    {
        "folder": "0075-sort-colors",
        "title": "Sort Colors",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Dutch National Flag (3-Way Partitioning)",
        "lc_number": 75,
        "lc_title": "Sort Colors",
        "lc_url": "https://leetcode.com/problems/sort-colors/",
        "recall": "How do you sort an array with values 0, 1, and 2 in-place in a single pass without using a sorting library?",
        "concept": "Maintain three pointers: low = 0 (boundary for 0s), mid = 0 (current element), high = n - 1 (boundary for 2s). While mid <= high: if nums[mid] == 0, swap(nums[low], nums[mid]), low++, mid++; if nums[mid] == 1, mid++; if nums[mid] == 2, swap(nums[mid], nums[high]), high-- (do not increment mid!).",
        "hints": [
            "Can you partition the array into three regions: [0..low-1] are 0s, [low..mid-1] are 1s, [high+1..n-1] are 2s?",
            "When swapping with high, why must mid NOT increment immediately?"
        ],
        "trick": "When swapping nums[mid] with nums[high], the element brought from high has not been examined yet, so keep mid in place to inspect it in the next iteration.",
        "complexity": "Time: O(N) one pass with mid scanning up to high. Space: O(1) strictly in-place.",
        "edge_cases": [
            "All same element: [0, 0, 0] or [2, 2, 2].",
            "Already sorted: [0, 1, 2].",
            "Reverse sorted: [2, 1, 0]."
        ]
    },
    {
        "folder": "0098-validate-binary-search-tree",
        "title": "Validate Binary Search Tree",
        "difficulty": "Medium",
        "topic": "Trees",
        "pattern": "DFS Valid Range Propagation / Inorder Traversal",
        "lc_number": 98,
        "lc_title": "Validate Binary Search Tree",
        "lc_url": "https://leetcode.com/problems/validate-binary-search-tree/",
        "recall": "How do you verify whether a binary tree satisfies the BST invariant across all nodes, not just immediate children?",
        "concept": "A node's value must be strictly greater than all nodes in its left subtree and strictly less than all in its right subtree. Recurse with bounds: validate(node, low, high). For node: check low < node.val < high, then validate(node.left, low, node.val) and validate(node.right, node.val, high). Alternatively, do an inorder traversal and ensure strictly increasing values.",
        "hints": [
            "Does checking node.left.val < node.val < node.right.val suffice? Why not?",
            "Pass down the valid minimum and maximum bounds (low, high) as you traverse."
        ],
        "trick": "Use Long or null objects for low and high bounds to handle nodes whose values equal Integer.MIN_VALUE or Integer.MAX_VALUE.",
        "complexity": "Time: O(N) visits each node once. Space: O(H) recursion stack where H is tree height (O(log N) balanced, O(N) skewed).",
        "edge_cases": [
            "Node values equal to INT_MIN or INT_MAX: [2147483647].",
            "Duplicate values: [2, 2, 2] -> false (BST requires strict inequality).",
            "Valid local children but invalid ancestor: [5, 1, 4, null, null, 3, 6]."
        ]
    },
    {
        "folder": "0104-maximum-depth-of-binary-tree",
        "title": "Maximum Depth of Binary Tree",
        "difficulty": "Easy",
        "topic": "Trees",
        "pattern": "DFS Post-Order Recursion / BFS Level Order",
        "lc_number": 104,
        "lc_title": "Maximum Depth of Binary Tree",
        "lc_url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/",
        "recall": "How do you compute the maximum depth (number of nodes along longest root-to-leaf path) of a binary tree?",
        "concept": "Base case: if root is null, depth is 0. Recursively compute leftDepth = maxDepth(root.left) and rightDepth = maxDepth(root.right). The maximum depth is 1 + max(leftDepth, rightDepth).",
        "hints": [
            "What is the depth of an empty tree?",
            "If you know the max depths of left and right subtrees, what is the depth of the parent?"
        ],
        "trick": "Post-order bottom-up calculation: 1 + max(maxDepth(left), maxDepth(right)) solves the problem in 2 lines.",
        "complexity": "Time: O(N) visits every node once. Space: O(H) stack depth where H is tree height.",
        "edge_cases": [
            "Empty tree: root is null -> 0.",
            "Single node: root only -> 1.",
            "Skewed tree (linked list structure): depth is N."
        ]
    },
    {
        "folder": "0112-path-sum",
        "title": "Path Sum",
        "difficulty": "Easy",
        "topic": "Trees",
        "pattern": "DFS Root-to-Leaf Path Recursion",
        "lc_number": 112,
        "lc_title": "Path Sum",
        "lc_url": "https://leetcode.com/problems/path-sum/",
        "recall": "How do you check if a binary tree has a root-to-leaf path such that the sum of values along the path equals targetSum?",
        "concept": "Base case: if root is null, return false. Subtract root.val from targetSum. If the current node is a leaf (left == null and right == null), check if remaining targetSum == 0. Otherwise, recurse on left and right subtrees: hasPathSum(root.left, targetSum) || hasPathSum(root.right, targetSum).",
        "hints": [
            "What defines a leaf node? A node with NO children.",
            "Instead of accumulating sum, subtract root.val from targetSum as you descend."
        ],
        "trick": "A path must go all the way to a leaf. If a node has only one child, you cannot claim a match at the missing child.",
        "complexity": "Time: O(N) visits each node once in the worst case. Space: O(H) call stack height.",
        "edge_cases": [
            "Empty tree: root == null -> false (even if targetSum == 0).",
            "Negative node values and negative targets.",
            "Single node matching target: [5], target = 5 -> true."
        ]
    },
    {
        "folder": "0121-best-time-to-buy-and-sell-stock",
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Single Pass Running Minimum (Prefix Min)",
        "lc_number": 121,
        "lc_title": "Best Time to Buy and Sell Stock",
        "lc_url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "recall": "How do you maximize profit from choosing a single day to buy and a later day to sell stock in O(N) time and O(1) space?",
        "concept": "Maintain minPrice seen so far (initialized to infinity) and maxProfit (initialized to 0). Iterate through prices: minPrice = min(minPrice, price), and maxProfit = max(maxProfit, price - minPrice). Return maxProfit.",
        "hints": [
            "If you sell on day i, what price would have given you the best profit?",
            "Track the minimum price seen so far as you iterate through the list."
        ],
        "trick": "Buying must happen BEFORE selling. Updating minPrice before calculating potential profit ensures correct chronological ordering.",
        "complexity": "Time: O(N) single loop over prices. Space: O(1) constant extra variables.",
        "edge_cases": [
            "Strictly decreasing prices: [7, 6, 4, 3, 1] -> 0 profit.",
            "Single day: [5] -> 0 profit.",
            "All identical prices: [3, 3, 3] -> 0."
        ]
    },
    {
        "folder": "0125-valid-palindrome",
        "title": "Valid Palindrome",
        "difficulty": "Easy",
        "topic": "Two Pointers",
        "pattern": "Two Pointers from Ends with Filter",
        "lc_number": 125,
        "lc_title": "Valid Palindrome",
        "lc_url": "https://leetcode.com/problems/valid-palindrome/",
        "recall": "How do you determine if a string is a palindrome considering only alphanumeric characters and ignoring cases in O(1) extra space?",
        "concept": "Use two pointers left = 0, right = s.length() - 1. While left < right: skip non-alphanumeric chars at left with left++, and at right with right--. Once both point to alphanumeric chars, compare Character.toLowerCase(s[left]) with Character.toLowerCase(s[right]). If mismatch, return false; otherwise advance both.",
        "hints": [
            "Can you avoid allocating a new filtered string by using two pointers directly?",
            "Use isLetterOrDigit / isalnum to skip punctuation and spaces."
        ],
        "trick": "Advance pointers inward over non-alphanumeric characters while ensuring left < right to prevent out-of-bounds indexing.",
        "complexity": "Time: O(N) single traversal of the string. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Empty string or string with only spaces/punctuation: \" \" -> true.",
            "Single character: \"a\" -> true.",
            "Case sensitivity: \"0P\" -> false ('0' vs 'p')."
        ]
    },
    {
        "folder": "0146-lru-cache",
        "title": "LRU Cache",
        "difficulty": "Medium",
        "topic": "Design / Cache",
        "pattern": "Hash Map + Doubly Linked List",
        "lc_number": 146,
        "lc_title": "LRU Cache",
        "lc_url": "https://leetcode.com/problems/lru-cache/",
        "recall": "How do you design a Least Recently Used (LRU) Cache with get and put operations both running in O(1) average time?",
        "concept": "Combine a Hash Map (mapping key -> Node) and a Doubly Linked List (with dummy head and dummy tail). The node stores both key and value. get(key): look up in map; if found, move node to head (most recent) and return val. put(key, val): if key exists, update val and move node to head. If new, create node, add to head, insert in map. If capacity exceeded, remove LRU node at tail.prev from both list and map.",
        "hints": [
            "Hash map gives O(1) lookup, but how can you reorder elements in O(1) time?",
            "A doubly linked list allows removing any node in O(1) if you have its direct reference."
        ],
        "trick": "Dummy head and dummy tail nodes eliminate edge cases for empty list and head/tail boundary updates. Store key inside Node so when evicting tail.prev, you can delete map[node.key] in O(1).",
        "complexity": "Time: O(1) average for both get and put. Space: O(capacity) for the hash map and doubly linked list nodes.",
        "edge_cases": [
            "Capacity 1: evicts on every insert if unique key.",
            "Updating existing key value also marks it as most recently used.",
            "Repeated gets of the same key."
        ]
    },
    {
        "folder": "0167-two-sum-ii-input-array-is-sorted",
        "title": "Two Sum II - Input Array Is Sorted",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Opposite Ends Converging Pointers",
        "lc_number": 167,
        "lc_title": "Two Sum II - Input Array Is Sorted",
        "lc_url": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/",
        "recall": "Given a 1-indexed sorted array, how do you find two numbers that sum to target in O(N) time and O(1) space?",
        "concept": "Initialize left = 0, right = n - 1. Compute currentSum = numbers[left] + numbers[right]. If currentSum == target, return [left + 1, right + 1]. If currentSum < target, increment left to increase the sum. If currentSum > target, decrement right to decrease the sum.",
        "hints": [
            "The array is already sorted! How can you leverage sorted order to eliminate candidates?",
            "If the sum of extremes is too small, which pointer must move?"
        ],
        "trick": "Sorted monotonicity guarantees correctness: if numbers[left] + numbers[right] > target, numbers[right] cannot pair with ANY index >= left, so right can safely be decremented.",
        "complexity": "Time: O(N) since each step moves one pointer closer. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Negative numbers: [-1, 0], target = -1.",
            "Duplicate elements: [2, 2], target = 4.",
            "Remember 1-based indexing in return value."
        ]
    },
    {
        "folder": "0215-kth-largest-element-in-an-array",
        "title": "Kth Largest Element in an Array",
        "difficulty": "Medium",
        "topic": "Sorting & Heap",
        "pattern": "Min-Heap of Size K / Quickselect",
        "lc_number": 215,
        "lc_title": "Kth Largest Element in an Array",
        "lc_url": "https://leetcode.com/problems/kth-largest-element-in-an-array/",
        "recall": "How do you find the kth largest element in an unsorted array without fully sorting the array?",
        "concept": "Approach 1 (Min-Heap): Maintain a min-heap of size k. For each num in array, push to heap. If heap size > k, pop the minimum. At the end, heap.peek() is the kth largest element. Approach 2 (Quickselect): Partition array around random pivot until pivot index is n - k in O(N) average time.",
        "hints": [
            "Do you need to sort all N elements if you only care about the top K?",
            "A min-heap of size K keeps the K largest elements seen so far; its root is the smallest of those K."
        ],
        "trick": "Using a MIN-heap of size K keeps the K largest numbers, so the root is the kth largest. Heap size never exceeds K + 1.",
        "complexity": "Time: O(N log K) with min-heap, or O(N) average with Quickselect. Space: O(K) for the min-heap.",
        "edge_cases": [
            "k == 1: maximum element.",
            "k == n: minimum element.",
            "Array with many duplicates: [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4."
        ]
    },
    {
        "folder": "0217-contains-duplicate",
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Hash Set Early Exit",
        "lc_number": 217,
        "lc_title": "Contains Duplicate",
        "lc_url": "https://leetcode.com/problems/contains-duplicate/",
        "recall": "How do you check if any value appears at least twice in an array in linear time?",
        "concept": "Traverse the array while adding elements to a Hash Set. If set.add(num) returns false (or if num is already in set), return true immediately. If loop finishes without duplicates, return false.",
        "hints": [
            "What data structure provides O(1) average membership checking?",
            "Can you return true immediately as soon as a duplicate is seen?"
        ],
        "trick": "Early return upon first duplicate gives best-case O(1) time without reading the entire array.",
        "complexity": "Time: O(N) average. Space: O(N) auxiliary space for the hash set.",
        "edge_cases": [
            "All unique: [1, 2, 3, 4] -> false.",
            "Immediate duplicate: [1, 1, 1] -> true.",
            "Single element: [1] -> false."
        ]
    },
    {
        "folder": "217-contains-duplicate",
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Hash Set Early Exit",
        "lc_number": 217,
        "lc_title": "Contains Duplicate",
        "lc_url": "https://leetcode.com/problems/contains-duplicate/",
        "recall": "How to determine if an integer array contains any duplicate values in O(N) time?",
        "concept": "Insert elements into a hash set. If an element is already present in the set, a duplicate exists; return true. Otherwise return false after processing all elements.",
        "hints": [
            "Sort vs Hash Set trade-off: Sort is O(N log N) time and O(1) space; Hash Set is O(N) time and O(N) space.",
            "In Java, set.add(num) returns false if the item was already present, allowing a single lookup-and-insert step."
        ],
        "trick": "set.contains or !set.add(num) enables instant early exit on first duplicate found.",
        "complexity": "Time: O(N) average. Space: O(N) for set.",
        "edge_cases": [
            "Empty or 1 element: false.",
            "Immediate duplicate: [1, 1, 1] -> true.",
            "All distinct negative & positive numbers: [-1, 2, -3, 4] -> false."
        ]
    },
    {
        "folder": "0238-product-of-array-except-self",
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "topic": "Arrays & Hashing",
        "pattern": "Prefix & Suffix Products",
        "lc_number": 238,
        "lc_title": "Product of Array Except Self",
        "lc_url": "https://leetcode.com/problems/product-of-array-except-self/",
        "recall": "How do you calculate the product of all elements except nums[i] for each index in O(N) without using the division operator?",
        "concept": "The product of all elements except nums[i] is (prefix product of elements before i) * (suffix product of elements after i). Pass 1: compute prefix products into output array res[i] = res[i-1] * nums[i-1]. Pass 2: maintain a running right product suffixProduct from right to left, multiplying res[i] *= suffixProduct, then suffixProduct *= nums[i].",
        "hints": [
            "Can you break the product for index i into two parts: elements to its left and elements to its right?",
            "Use the output array to store left products first, then multiply right products on the fly."
        ],
        "trick": "Using the result array itself to store prefix products achieves O(1) auxiliary space (excluding output array).",
        "complexity": "Time: O(N) two linear passes. Space: O(1) auxiliary space (output array does not count as extra space).",
        "edge_cases": [
            "Array with one zero: all elements become 0 except the zero index.",
            "Array with two or more zeros: all elements become 0.",
            "Negative numbers."
        ]
    },
    {
        "folder": "0283-move-zeroes",
        "title": "Move Zeroes",
        "difficulty": "Easy",
        "topic": "Two Pointers",
        "pattern": "Slow & Fast Two Pointers (In-place Write)",
        "lc_number": 283,
        "lc_title": "Move Zeroes",
        "lc_url": "https://leetcode.com/problems/move-zeroes/",
        "recall": "How do you move all zeros to the end of an array in-place while maintaining the relative order of non-zero elements?",
        "concept": "Maintain slow pointer insertPos = 0. Iterate fast pointer through array. Whenever nums[fast] != 0, swap nums[insertPos] with nums[fast] (or assign nums[insertPos] = nums[fast]) and increment insertPos. If using assignment, fill remaining indices from insertPos to n - 1 with 0.",
        "hints": [
            "Can you shift all non-zero elements forward to an insertion pointer?",
            "Swapping nums[insertPos] with nums[fast] handles both compaction and trailing zeros in one pass."
        ],
        "trick": "Swapping nums[insertPos] with nums[fast] whenever nums[fast] != 0 automatically moves zeros forward without a second loop.",
        "complexity": "Time: O(N) single pass. Space: O(1) in-place.",
        "edge_cases": [
            "No zeros: [1, 2, 3] -> [1, 2, 3].",
            "All zeros: [0, 0, 0] -> [0, 0, 0].",
            "Zeros already at end: [1, 2, 0, 0]."
        ]
    },
    {
        "folder": "0347-top-k-frequent-elements",
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "topic": "Sorting & Heap",
        "pattern": "Bucket Sort / Min-Heap by Frequency",
        "lc_number": 347,
        "lc_title": "Top K Frequent Elements",
        "lc_url": "https://leetcode.com/problems/top-k-frequent-elements/",
        "recall": "How do you find the k most frequent elements in an array in strictly better than O(N log N) time?",
        "concept": "Count frequencies using a hash map. Then use Bucket Sort where index represents frequency (0 to N). List<Integer>[] buckets = new List[n + 1]. Place each number into buckets[freq]. Iterate buckets from index N down to 0, collecting elements until k elements are gathered.",
        "hints": [
            "Frequencies are bounded between 1 and N. Does this allow linear-time bucket sorting?",
            "Array of lists where index = frequency avoids comparison-based sorting."
        ],
        "trick": "Bucket sort index corresponds to frequency. Since max frequency is N, iterating from bucket N down to 1 gives O(N) time.",
        "complexity": "Time: O(N) to count frequencies, populate buckets, and collect top k. Space: O(N) for map and buckets.",
        "edge_cases": [
            "k equals number of unique elements.",
            "All elements have frequency 1.",
            "Negative numbers as values."
        ]
    },
    {
        "folder": "0611-valid-triangle-number",
        "title": "Valid Triangle Number",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Sort + Reverse Pivot + Two Pointers",
        "lc_number": 611,
        "lc_title": "Valid Triangle Number",
        "lc_url": "https://leetcode.com/problems/valid-triangle-number/",
        "recall": "How do you count the number of triplets that can form a valid triangle (a + b > c) in O(N^2) time?",
        "concept": "Sort the array. The triangle condition simplifies: if sorted a <= b <= c, we only need to verify a + b > c. Fix the largest side k from n - 1 down to 2. Set left = 0, right = k - 1. If nums[left] + nums[right] > nums[k], then ALL elements from left to right - 1 also satisfy the condition with right, so add (right - left) to count and decrement right. Otherwise, increment left.",
        "hints": [
            "If sorted a <= b <= c, which triangle inequality is the ONLY one you need to check?",
            "Fix the largest side c = nums[k] and use two pointers for a and b."
        ],
        "trick": "When nums[left] + nums[right] > nums[k], every element from left to right - 1 paired with nums[right] also exceeds nums[k], contributing (right - left) valid triangles in O(1).",
        "complexity": "Time: O(N^2) (sorting O(N log N) + outer loop running N times with two pointers O(N)). Space: O(log N) sorting space.",
        "edge_cases": [
            "Array with zeros: sides with length 0 can never form a triangle.",
            "Fewer than 3 elements: return 0.",
            "All equal elements: [2, 2, 2, 2]."
        ]
    },
    {
        "folder": "0875-koko-eating-bananas",
        "title": "Koko Eating Bananas",
        "difficulty": "Medium",
        "topic": "Binary Search",
        "pattern": "Binary Search on Answer Range",
        "lc_number": 875,
        "lc_title": "Koko Eating Bananas",
        "lc_url": "https://leetcode.com/problems/koko-eating-bananas/",
        "recall": "How do you find the minimum integer speed k to eat all bananas within h hours?",
        "concept": "The eating speed k has a monotonic feasibility property: if speed k works, any speed > k also works. Binary search speed in range [1, max(piles)]. For candidate speed mid, compute total hours = sum(ceil(pile / mid)). If hours <= h, mid is feasible; try smaller speed by setting high = mid. If hours > h, speed is too slow; set low = mid + 1.",
        "hints": [
            "Is the feasibility function monotonic with respect to eating speed k?",
            "Ceiling division of pile / k can be computed as (pile + k - 1) // k."
        ],
        "trick": "Compute ceiling division without floating point inaccuracy: (pile + mid - 1) // mid. Watch out for 32-bit integer overflow when summing total hours (use 64-bit long in Java/C++).",
        "complexity": "Time: O(N log(max(piles))) where N is length of piles. Space: O(1) auxiliary space.",
        "edge_cases": [
            "h == piles.length: speed must be max(piles).",
            "Very large pile values: total hours can overflow 32-bit int.",
            "Single pile: return ceil(pile[0] / h)."
        ]
    },
    {
        "folder": "1448-count-good-nodes-in-binary-tree",
        "title": "Count Good Nodes in Binary Tree",
        "difficulty": "Medium",
        "topic": "Trees",
        "pattern": "DFS with Running Path Maximum",
        "lc_number": 1448,
        "lc_title": "Count Good Nodes in Binary Tree",
        "lc_url": "https://leetcode.com/problems/count-good-nodes-in-binary-tree/",
        "recall": "In a binary tree, how do you count nodes where no node on the path from root to that node has a greater value?",
        "concept": "Run a DFS passing the running maximum maxSoFar along the path from root. For current node: if node.val >= maxSoFar, this node is good (count = 1), and update currentMax = max(maxSoFar, node.val). Recurse on left and right children with currentMax. Return count + dfs(left, currentMax) + dfs(right, currentMax).",
        "hints": [
            "What information does a child need from its ancestors to decide if it is 'good'?",
            "Pass down the maximum value seen so far along the current root-to-node path."
        ],
        "trick": "Root is always good because there are no ancestors. Update path max as max(maxSoFar, node.val) before descending.",
        "complexity": "Time: O(N) visits each node once. Space: O(H) recursion stack where H is tree height.",
        "edge_cases": [
            "All node values identical: every node is good.",
            "Strictly decreasing tree: only root is good.",
            "Negative node values: initialize maxSoFar with root.val, not 0."
        ]
    },
    {
        "folder": "268-missing-number",
        "title": "Missing Number",
        "difficulty": "Easy",
        "topic": "Bit Manipulation",
        "pattern": "XOR Cancellation / Gauss Sum",
        "lc_number": 268,
        "lc_title": "Missing Number",
        "lc_url": "https://leetcode.com/problems/missing-number/",
        "recall": "Given an array containing n distinct numbers in the range [0, n], how do you find the one missing number in O(N) time and O(1) space?",
        "concept": "Approach 1 (XOR): XOR all numbers from 0 to n and XOR all numbers in the array. Since x ^ x = 0 and x ^ 0 = x, all present numbers cancel out, leaving exactly the missing number. Approach 2 (Gauss Sum): expectedSum = n * (n + 1) // 2. Missing = expectedSum - sum(nums).",
        "hints": [
            "What happens when you XOR a number with itself?",
            "XORing indices 0..n and array elements together cancels out everything except the missing value."
        ],
        "trick": "XOR avoids any possibility of integer overflow that could occur with Gauss sum on large n.",
        "complexity": "Time: O(N) single pass. Space: O(1) constant extra memory.",
        "edge_cases": [
            "Missing 0: [1, 2, 3] -> 0.",
            "Missing n: [0, 1, 2] -> 3.",
            "Single element: [0] -> 1, [1] -> 0."
        ]
    },
    {
        "folder": "53-maximum-subarray",
        "title": "Maximum Subarray",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "Kadane's Algorithm",
        "lc_number": 53,
        "lc_title": "Maximum Subarray",
        "lc_url": "https://leetcode.com/problems/maximum-subarray/",
        "recall": "How do you find the contiguous subarray with the largest sum in O(N) time and O(1) space?",
        "concept": "Kadane's Algorithm: Maintain currentSum and maxSum initialized to nums[0]. For each subsequent number x: currentSum = max(x, currentSum + x). Update maxSum = max(maxSum, currentSum). If currentSum becomes negative, resetting to x means abandoning a dragged-down prefix.",
        "hints": [
            "If your running sum is negative, does extending it help any future subarray?",
            "At each step, decide: start a new subarray at nums[i], or extend the existing one?"
        ],
        "trick": "Initialize both currentSum and maxSum to nums[0] (not 0) to correctly handle arrays with all negative numbers.",
        "complexity": "Time: O(N) single linear pass. Space: O(1) constant space.",
        "edge_cases": [
            "All negative numbers: [-3, -1, -5] -> -1.",
            "Single element: [1] -> 1, [-2] -> -2.",
            "Alternating signs: [5, -3, 5] -> 7."
        ]
    },

    # -------------------------------------------------------------
    # 2. ALGOEXPERT PROBLEMS (Folders 28 to 51)
    # -------------------------------------------------------------
    {
        "folder": "ArrayOfProducts",
        "title": "Array of Products",
        "difficulty": "Medium",
        "topic": "Arrays & Hashing",
        "pattern": "Prefix & Suffix Running Products",
        "lc_number": 238,
        "lc_title": "Product of Array Except Self",
        "lc_url": "https://leetcode.com/problems/product-of-array-except-self/",
        "recall": "How do you compute an array of products where output[i] is the product of every other element without division?",
        "concept": "Build the product of all elements to the left of i into products[i]. Then traverse backwards, maintaining a running rightProduct and multiplying products[i] *= rightProduct. Each element ends up as (product of left elements) * (product of right elements).",
        "hints": [
            "Think of the product at index i as two halves: everything to the left of i, and everything to the right of i.",
            "Fill the array with left running products first, then multiply right running products on a second backwards pass."
        ],
        "trick": "Keep running rightProduct in a single variable during the backwards pass to avoid allocating a second suffix array.",
        "complexity": "Time: O(N) two linear passes. Space: O(N) for the output array (O(1) auxiliary space).",
        "edge_cases": [
            "Arrays containing a single zero or multiple zeros.",
            "Two element array [a, b] -> [b, a].",
            "Arrays containing negative numbers."
        ]
    },
    {
        "folder": "BestSeat",
        "title": "Best Seat",
        "difficulty": "Medium",
        "topic": "Arrays & Hashing",
        "pattern": "Contiguous Zero Block Maximization (Midpoint)",
        "lc_number": 849,
        "lc_title": "Maximize Distance to Closest Person",
        "lc_url": "https://leetcode.com/problems/maximize-distance-to-closest-person/",
        "recall": "In a row of theater seats (0 is empty, 1 is occupied), which seat maximizes your distance to the closest person on either side?",
        "concept": "Scan the array to identify every contiguous sequence of 0s bounded by 1s. For each empty segment starting at left and ending at right (where seats[left-1] == 1 and seats[right] == 1), the length of available space is right - left. The most isolated seat in this segment is the integer midpoint (left + right - 1) // 2. Track the segment with the maximum length and return its midpoint.",
        "hints": [
            "You want to maximize the minimum distance to occupied seats on both sides.",
            "Find the longest contiguous run of zeros bounded by 1s; your best choice is sitting right in the middle."
        ],
        "trick": "The best seat in a contiguous block of zeros between indices left and right - 1 is located at (left + right - 1) // 2. If no zeros exist, return -1.",
        "complexity": "Time: O(N) single linear scan of seats. Space: O(1) constant extra variables.",
        "edge_cases": [
            "No empty seats (all 1s): return -1.",
            "Single empty seat: [1, 0, 1] -> seat 1.",
            "Multiple contiguous zero blocks of equal length: return the first one encountered."
        ]
    },
    {
        "folder": "BubbleSort",
        "title": "Bubble Sort",
        "difficulty": "Easy",
        "topic": "Sorting",
        "pattern": "Adjacent Element Swapping with Early Termination",
        "lc_number": 912,
        "lc_title": "Sort an Array",
        "lc_url": "https://leetcode.com/problems/sort-an-array/",
        "recall": "How does Bubble Sort work, and how can it achieve O(N) best-case time on already sorted inputs?",
        "concept": "Repeatedly step through the array, compare adjacent elements, and swap them if they are in the wrong order. After the k-th pass, the k-th largest element has 'bubbled up' to its correct final position at the end. Use a boolean isSorted flag: if an entire pass completes without a single swap, terminate early.",
        "hints": [
            "Each pass bubbles the next largest unsorted element to the end of the array.",
            "Can you detect if the array is already sorted to stop immediately?"
        ],
        "trick": "Reduce the inner loop limit by 1 on each pass (counter = 0..n-1) and break if isSorted remains true.",
        "complexity": "Time: O(N^2) average and worst case, O(N) best case with swapped flag. Space: O(1) in-place.",
        "edge_cases": [
            "Already sorted array: finishes in 1 pass O(N).",
            "Reverse sorted array: triggers maximum swaps N*(N-1)/2.",
            "Single element array."
        ]
    },
    {
        "folder": "CombinationSum",
        "title": "Combination Sum",
        "difficulty": "Medium",
        "topic": "Backtracking",
        "pattern": "Backtracking with Unbounded Element Reuse",
        "lc_number": 39,
        "lc_title": "Combination Sum",
        "lc_url": "https://leetcode.com/problems/combination-sum/",
        "recall": "How do you find all unique combinations of candidate numbers that sum to a target when each number may be used an unlimited number of times?",
        "concept": "Sort candidates. Use recursive backtracking: backtrack(startIndex, currentCombination, remainingTarget). If remainingTarget == 0, save a copy of currentCombination. If remainingTarget < 0, return. Loop index i from startIndex to len(candidates) - 1: add candidates[i] to combination, recurse with same index i (allowing reuse) and remainingTarget - candidates[i], then backtrack by popping candidates[i].",
        "hints": [
            "Can you choose to either include candidates[i] again or move to candidates[i+1]?",
            "Sorting candidates allows early termination of the loop when candidates[i] > remainingTarget."
        ],
        "trick": "Passing startIndex = i into the recursive call allows unlimited reuse of the current element while preventing duplicate combinations in different orders.",
        "complexity": "Time: O(2^T) where T is target / min(candidates). Space: O(T) maximum recursion depth.",
        "edge_cases": [
            "Target smaller than minimum candidate: returns empty list.",
            "Single candidate dividing target evenly: candidates=[2], target=6 -> [[2, 2, 2]].",
            "Ensure combinations returned are deep copies of current state."
        ]
    },
    {
        "folder": "FirstDuplicateValue",
        "title": "First Duplicate Value",
        "difficulty": "Medium",
        "topic": "Arrays & Hashing",
        "pattern": "In-place Sign Flipping (Index as Hash Key)",
        "lc_number": 287,
        "lc_title": "Find the Duplicate Number",
        "lc_url": "https://leetcode.com/problems/find-the-duplicate-number/",
        "recall": "Given an array of integers between 1 and n inclusive, how do you find the first duplicate value in O(N) time and O(1) auxiliary space?",
        "concept": "Since values are bounded in [1, n], map each value val = abs(array[i]) to index val - 1. Check the sign of array[val - 1]: if array[val - 1] < 0, then val has been seen before; return val immediately as the first duplicate! Otherwise, mark it seen by negating array[val - 1] = -array[val - 1].",
        "hints": [
            "The values are between 1 and n, matching the array indices [0, n - 1].",
            "Can you use the sign of array[value - 1] as a visited marker without allocating a set?"
        ],
        "trick": "Always use abs(array[i]) to get the original number value, because preceding elements may have already been negated.",
        "complexity": "Time: O(N) single pass with early exit. Space: O(1) in-place sign modification.",
        "edge_cases": [
            "No duplicates: return -1.",
            "Multiple duplicates: return the one whose second appearance has the minimum index.",
            "All elements duplicate: [2, 1, 5, 2, 3, 3, 4] -> returns 2."
        ]
    },
    {
        "folder": "LongestPeak",
        "title": "Longest Peak",
        "difficulty": "Medium",
        "topic": "Arrays & Hashing",
        "pattern": "Peak Detection & Bidirectional Expansion",
        "lc_number": 845,
        "lc_title": "Longest Mountain in Array",
        "lc_url": "https://leetcode.com/problems/longest-mountain-in-array/",
        "recall": "How do you find the length of the longest peak (strictly increasing then strictly decreasing subarray of length >= 3) in O(N) time?",
        "concept": "A peak occurs at index i if array[i-1] < array[i] and array[i] > array[i+1]. Iterate i from 1 to n - 2 to find peaks. When a peak is found, expand leftwards while array[left-1] < array[left], and rightwards while array[right+1] < array[right]. The peak length is right - left + 1. Update longestPeak = max(longestPeak, peakLength) and jump i directly to right to maintain linear time.",
        "hints": [
            "First identify true peaks: elements strictly greater than both immediate neighbors.",
            "Once a peak is identified, expand two pointers outwards as far as the slopes remain strictly decreasing."
        ],
        "trick": "Jump the outer loop index i = right after exploring a peak, because no intermediate index along a decreasing slope can be a new peak.",
        "complexity": "Time: O(N) because each element is visited at most a constant number of times. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Array length < 3: cannot form a peak -> return 0.",
            "Strictly increasing or strictly decreasing array: no peak -> return 0.",
            "Flat plateaus [1, 2, 2, 1]: not a valid peak."
        ]
    },
    {
        "folder": "MajorityElement",
        "title": "Majority Element",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Boyer-Moore Voting Algorithm",
        "lc_number": 169,
        "lc_title": "Majority Element",
        "lc_url": "https://leetcode.com/problems/majority-element/",
        "recall": "How do you find the majority element (element appearing more than n/2 times) in O(N) time and O(1) space?",
        "concept": "Boyer-Moore Voting: Maintain candidate and count = 0. For each num in array: if count == 0, set candidate = num. If num == candidate, increment count; otherwise decrement count. Since the majority element appears more than N/2 times, its count will strictly overcome all other elements combined.",
        "hints": [
            "Think of pairing distinct elements to cancel each other out.",
            "If the majority element has frequency > n/2, can all minority elements combined cancel it completely?"
        ],
        "trick": "Resetting candidate when count == 0 guarantees that the majority element survives cancellations.",
        "complexity": "Time: O(N) single pass. Space: O(1) constant extra memory.",
        "edge_cases": [
            "Array with 1 element: return array[0].",
            "Majority element barely exceeding half: [2, 2, 1, 1, 2]."
        ]
    },
    {
        "folder": "MergeOverlappinIntervals",
        "title": "Merge Overlapping Intervals",
        "difficulty": "Medium",
        "topic": "Intervals",
        "pattern": "Sort by Start Time + Greedy Merge",
        "lc_number": 56,
        "lc_title": "Merge Intervals",
        "lc_url": "https://leetcode.com/problems/merge-intervals/",
        "recall": "How do you merge overlapping intervals into an optimal set of disjoint intervals?",
        "concept": "Sort intervals by start value. Initialize result with the first interval. For each subsequent interval, if its start <= currentMerged.end, merge by setting currentMerged.end = max(currentMerged.end, nextInterval.end). If its start > currentMerged.end, append nextInterval to result.",
        "hints": [
            "Sorting by start time ensures any potentially overlapping intervals appear adjacent in the list.",
            "Watch out for an interval that is completely contained within the previous one."
        ],
        "trick": "Always use max(currentMerged.end, nextInterval.end) so a shorter contained interval does not shrink the end.",
        "complexity": "Time: O(N log N) for sorting. Space: O(N) for output array.",
        "edge_cases": [
            "Intervals already non-overlapping.",
            "One giant interval subsuming all others: [[1, 10], [2, 3], [4, 5]].",
            "Intervals touching at endpoints: [[1, 2], [2, 3]] -> [[1, 3]]."
        ]
    },
    {
        "folder": "MergeSort",
        "title": "Merge Sort",
        "difficulty": "Medium",
        "topic": "Sorting",
        "pattern": "Divide and Conquer (Merge Step)",
        "lc_number": 912,
        "lc_title": "Sort an Array",
        "lc_url": "https://leetcode.com/problems/sort-an-array/",
        "recall": "How does Merge Sort guarantee stable O(N log N) worst-case time sorting?",
        "concept": "Divide: find midpoint mid = len // 2 and recursively sort left half and right half. Conquer: merge the two sorted halves into a combined sorted array by comparing elements using two pointers i and j, copying the smaller element to output.",
        "hints": [
            "Break the list into two halves until length <= 1, then merge two sorted halves.",
            "Merging two sorted lists of total size N takes linear O(N) time."
        ],
        "trick": "Use <= when comparing left[i] <= right[j] to ensure stability (preserving original relative order of equal elements).",
        "complexity": "Time: O(N log N) in all cases (best, average, worst). Space: O(N) auxiliary space for merging.",
        "edge_cases": [
            "Empty or 1 element: base case.",
            "Already sorted: still executes O(N log N) divisions and merges.",
            "All identical values."
        ]
    },
    {
        "folder": "MergeSort2",
        "title": "Merge Sort (Optimized Auxiliary Array)",
        "difficulty": "Medium",
        "topic": "Sorting",
        "pattern": "Divide & Conquer with In-place Buffer Swapping",
        "lc_number": 912,
        "lc_title": "Sort an Array",
        "lc_url": "https://leetcode.com/problems/sort-an-array/",
        "recall": "How can Merge Sort be optimized to avoid creating new sub-arrays at every recursive call?",
        "concept": "Allocate a single auxiliary array of size N upfront. Alternating roles between main array and auxiliary array across recursive levels avoids reallocating memory. Merge elements from auxiliary array back into main array in-place.",
        "hints": [
            "Can you allocate only one auxiliary buffer upfront and alternate roles between source and destination?",
            "Pass startIdx and endIdx indices instead of slicing sub-arrays."
        ],
        "trick": "Passing auxiliary array and swapping source/destination arrays at alternating recursion depths reduces memory allocations from O(N log N) to O(N).",
        "complexity": "Time: O(N log N). Space: O(N) auxiliary space allocated exactly once.",
        "edge_cases": [
            "Odd length arrays.",
            "Large arrays where slicing memory overhead causes performance degradation."
        ]
    },
    {
        "folder": "MonotonicArray",
        "title": "Monotonic Array",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Single Pass Non-Decreasing / Non-Increasing Check",
        "lc_number": 896,
        "lc_title": "Monotonic Array",
        "lc_url": "https://leetcode.com/problems/monotonic-array/",
        "recall": "How do you verify whether an array is monotonic (entirely non-increasing or non-decreasing) in a single pass?",
        "concept": "Maintain two boolean flags: isNonDecreasing = true and isNonIncreasing = true. Iterate through adjacent elements from i = 1 to n - 1. If array[i] < array[i-1], isNonDecreasing = false. If array[i] > array[i-1], isNonIncreasing = false. At the end, return isNonDecreasing || isNonIncreasing.",
        "hints": [
            "An array is monotonic if it never increases OR if it never decreases.",
            "Track both possibilities simultaneously in a single pass."
        ],
        "trick": "Early break when neither flag is true: if (!isNonDecreasing && !isNonIncreasing) return false.",
        "complexity": "Time: O(N) single pass. Space: O(1) constant memory.",
        "edge_cases": [
            "Arrays of length 0, 1, or 2 are always monotonic.",
            "All identical values: [1, 1, 1] -> true.",
            "Flat plateaus with direction change: [1, 2, 2, 3, 2] -> false."
        ]
    },
    {
        "folder": "MoveToEnd",
        "title": "Move Element To End",
        "difficulty": "Easy",
        "topic": "Two Pointers",
        "pattern": "Converging Two Pointers (In-place Swap)",
        "lc_number": 27,
        "lc_title": "Remove Element",
        "lc_url": "https://leetcode.com/problems/remove-element/",
        "recall": "How do you move all instances of a target integer to the end of an array in-place without preserving relative order?",
        "concept": "Use two pointers: left = 0, right = len - 1. While left < right: decrement right while array[right] == toMove and left < right. If array[left] == toMove, swap(array[left], array[right]). Increment left. Repeat until pointers cross.",
        "hints": [
            "Does the problem require maintaining the relative order of other elements? No!",
            "Point left at candidates to move away and right at non-target elements to swap with."
        ],
        "trick": "Always check left < right inside the inner while loop when moving the right pointer backwards.",
        "complexity": "Time: O(N) linear time, each element examined once. Space: O(1) in-place swaps.",
        "edge_cases": [
            "All elements equal to target toMove: no swaps performed.",
            "Target toMove not present in array: no swaps performed.",
            "Array with all targets already at the end."
        ]
    },
    {
        "folder": "NonConstructibleChange",
        "title": "Non-Constructible Change",
        "difficulty": "Easy",
        "topic": "Greedy",
        "pattern": "Sorted Greedy Change Invariant",
        "lc_number": 330,
        "lc_title": "Patching Array",
        "lc_url": "https://leetcode.com/problems/patching-array/",
        "recall": "Given an array of positive coin values, what is the minimum sum of money that you CANNOT make change for?",
        "concept": "Sort the coins in ascending order. Maintain currentChangeCreated = 0 (representing the ability to make all change from 1 to currentChangeCreated). For each coin: if coin > currentChangeCreated + 1, you can NEVER form currentChangeCreated + 1; return currentChangeCreated + 1 immediately! Otherwise, add coin to currentChangeCreated. If all coins processed, return currentChangeCreated + 1.",
        "hints": [
            "If you can create all change values from 1 to C, and your next coin is V: what happens if V > C + 1?",
            "Sort the coins first so you process them in increasing order."
        ],
        "trick": "Invariant: with coins up to index i, you can create all values in [1, C]. If coin <= C + 1, your reachable range expands to [1, C + coin]. If coin > C + 1, C + 1 is permanently unreachable.",
        "complexity": "Time: O(N log N) dominated by sorting coins. Space: O(1) or O(log N) sorting space.",
        "edge_cases": [
            "Empty coins array: return 1.",
            "First coin > 1: [2] -> return 1.",
            "Consecutive powers of 2: [1, 2, 4, 8] -> returns 16."
        ]
    },
    {
        "folder": "QuickSort",
        "title": "Quick Sort",
        "difficulty": "Medium",
        "topic": "Sorting",
        "pattern": "Pivot Partitioning Divide and Conquer",
        "lc_number": 912,
        "lc_title": "Sort an Array",
        "lc_url": "https://leetcode.com/problems/sort-an-array/",
        "recall": "How does Quick Sort partition an array around a pivot, and how do you prevent worst-case O(N^2) stack depth?",
        "concept": "Choose pivot (e.g. array[startIdx]). Partition elements such that all elements <= pivot are placed to its left, and all > pivot to its right. Swap pivot into its final position. To optimize stack space, always recurse into the smaller sub-array first and use tail-call iteration for the larger sub-array.",
        "hints": [
            "Place the pivot into its correct final position, then recursively sort left and right sub-arrays.",
            "Recurse on the smaller partition first to guarantee O(log N) maximum stack depth."
        ],
        "trick": "Always recurse on the smaller sub-array first; this bounds recursion depth to O(log N) even in worst-case partitions.",
        "complexity": "Time: O(N log N) average, O(N^2) worst case if already sorted without random pivot. Space: O(log N) stack space.",
        "edge_cases": [
            "All identical values: 3-way partition helps prevent degradation to O(N^2).",
            "Already sorted array."
        ]
    },
    {
        "folder": "SmallestDifference",
        "title": "Smallest Difference",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Two Sorted Arrays Two Pointers",
        "lc_number": 1200,
        "lc_title": "Minimum Absolute Difference",
        "lc_url": "https://leetcode.com/problems/minimum-absolute-difference/",
        "recall": "Given two non-empty arrays of integers, how do you find the pair of numbers (one from each array) whose absolute difference is closest to zero?",
        "concept": "Sort both arrays. Initialize ptrOne = 0, ptrTwo = 0. Compare arrayOne[ptrOne] and arrayTwo[ptrTwo]. Calculate currentDiff = abs(first - second). If currentDiff < smallestDiff, update smallestDiff and bestPair. If first < second, increment ptrOne (to bring it closer to second). If second < first, increment ptrTwo. If first == second, difference is 0 (return immediately!).",
        "hints": [
            "Sort both arrays so you can walk through them monotonically.",
            "Whichever pointer points to the smaller value should be incremented to decrease the gap."
        ],
        "trick": "Advance the pointer of the smaller value. Moving the larger pointer would only increase the distance.",
        "complexity": "Time: O(N log N + M log M) to sort both arrays + O(N + M) two-pointer pass. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Exact match exists: diff == 0 returns immediately.",
            "Negative numbers: abs() correctly handles distances between negative values.",
            "Arrays of different lengths."
        ]
    },
    {
        "folder": "SortedSquaredArray",
        "title": "Sorted Squared Array",
        "difficulty": "Easy",
        "topic": "Two Pointers",
        "pattern": "Opposite Ends Pointers Filling Result from Back",
        "lc_number": 977,
        "lc_title": "Squares of a Sorted Array",
        "lc_url": "https://leetcode.com/problems/squares-of-a-sorted-array/",
        "recall": "Given a sorted array of integers that may contain negative numbers, how do you return an array of their squares, also in sorted order, in O(N) time?",
        "concept": "Since the input is sorted, the largest squares must come from either the most negative numbers at the left end or the largest positive numbers at the right end. Initialize left = 0, right = n - 1, and fill result array from index n - 1 down to 0. In each step: compare abs(array[left]) with abs(array[right]). Place the larger square at result[idx], and advance that pointer inward.",
        "hints": [
            "Where can the largest square in the array come from? Only from the extreme left or extreme right!",
            "Fill the output array backwards from largest to smallest."
        ],
        "trick": "Filling from back to front (index n-1 down to 0) avoids needing to reverse the output array.",
        "complexity": "Time: O(N) single pass through the array. Space: O(N) for the result array.",
        "edge_cases": [
            "All negative numbers: [-5, -3, -1] -> squares are reversed.",
            "All positive numbers: [1, 2, 3] -> squares remain in original order.",
            "Mix of negative and positive with zeros: [-4, 0, 1, 4]."
        ]
    },
    {
        "folder": "SpiralMatrixTraversal",
        "title": "Spiral Matrix Traversal",
        "difficulty": "Medium",
        "topic": "Matrix",
        "pattern": "4-Boundary Shrinking Loop",
        "lc_number": 54,
        "lc_title": "Spiral Matrix",
        "lc_url": "https://leetcode.com/problems/spiral-matrix/",
        "recall": "How do you traverse an N x M 2D matrix in spiral order (clockwise from top-left) in O(N*M) time without visiting any cell twice?",
        "concept": "Define four boundaries: startRow = 0, endRow = n - 1, startCol = 0, endCol = m - 1. While startRow <= endRow and startCol <= endCol: 1. Traverse top row from startCol to endCol; 2. Traverse right col from startRow + 1 to endRow; 3. If startRow < endRow, traverse bottom row from endCol - 1 down to startCol; 4. If startCol < endCol, traverse left col from endRow - 1 down to startRow + 1. Shrink boundaries: startRow++, endRow--, startCol++, endCol--.",
        "hints": [
            "Track 4 moving boundaries: top, bottom, left, right.",
            "Ensure you do not double-traverse single-row or single-column matrices by checking startRow < endRow and startCol < endCol before the return loops."
        ],
        "trick": "Boundary checks (startRow < endRow and startCol < endCol) before moving left and moving up prevent duplicate traversals in non-square matrices.",
        "complexity": "Time: O(N * M) visits every cell exactly once. Space: O(1) auxiliary space (excluding result list).",
        "edge_cases": [
            "Single row matrix: [[1, 2, 3, 4]].",
            "Single column matrix: [[1], [2], [3]].",
            "1x1 matrix: [[1]]."
        ]
    },
    {
        "folder": "SweetAndSavoury",
        "title": "Sweet and Savoury",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Split by Sign + Two Pointers Bounded Optimization",
        "lc_number": 1099,
        "lc_title": "Two Sum Less Than K",
        "lc_url": "https://leetcode.com/problems/two-sum-less-than-k/",
        "recall": "Given sweet dishes (< 0) and savoury dishes (> 0), how do you pair one sweet and one savoury dish such that their combined flavour <= target and is as close to target as possible?",
        "concept": "Separate dishes into sweet dishes (negatives) and savoury dishes (positives). Sort sweet dishes by absolute value (or sort sweet ascending and savoury ascending). Use two pointers: sweetIdx = 0, savouryIdx = 0. Compute totalFlavour = sweet[sweetIdx] + savoury[savouryIdx]. If totalFlavour <= target, this is a feasible candidate; update bestPair if target - totalFlavour is smaller, then try to increase flavour by incrementing savouryIdx. If totalFlavour > target, savoury is too strong; decrement savouryIdx or advance sweetIdx.",
        "hints": [
            "Sweet dishes are negative, savoury are positive. You need exactly one of each.",
            "Sort both lists and use two pointers to find the closest sum <= target."
        ],
        "trick": "Only candidate pairs with combined sum <= target are valid. Among valid candidates, minimize target - combinedSum.",
        "complexity": "Time: O(N log N) to sort sweet and savoury arrays + O(N) two-pointer scan. Space: O(N) to separate dishes.",
        "edge_cases": [
            "No sweet dishes or no savoury dishes available: return [0, 0].",
            "No pair has sum <= target: return [0, 0].",
            "Exact match: combined flavour == target gives immediate optimal solution."
        ]
    },
    {
        "folder": "TournamentWinner",
        "title": "Tournament Winner",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Hash Map Score Tallying & Running Best",
        "lc_number": 2284,
        "lc_title": "Sender With Largest Word Count",
        "lc_url": "https://leetcode.com/problems/sender-with-largest-word-count/",
        "recall": "In a round-robin tournament where 1 indicates home team win and 0 away team win (3 points per win), how do you determine the tournament winner?",
        "concept": "Maintain a hash table of scores and track currentBestTeam initialized to empty string. For each match i with [homeTeam, awayTeam] and result results[i]: winningTeam = (results[i] == 1) ? homeTeam : awayTeam. scores[winningTeam] += 3. If scores[winningTeam] > scores[currentBestTeam], update currentBestTeam = winningTeam. Return currentBestTeam.",
        "hints": [
            "Translate each match result into the name of the winning team.",
            "Update scores in a hash map and maintain the leader on the fly to avoid a second pass."
        ],
        "trick": "Tracking currentBestTeam on the fly avoids scanning the entire scores map at the end.",
        "complexity": "Time: O(N) where N is number of competitions. Space: O(K) where K is number of unique teams.",
        "edge_cases": [
            "Single competition.",
            "Ensure points are awarded to awayTeam when result == 0."
        ]
    },
    {
        "folder": "TransposeMatrix",
        "title": "Transpose Matrix",
        "difficulty": "Easy",
        "topic": "Matrix",
        "pattern": "Row-to-Column Swapping [i][j] -> [j][i]",
        "lc_number": 867,
        "lc_title": "Transpose Matrix",
        "lc_url": "https://leetcode.com/problems/transpose-matrix/",
        "recall": "How do you flip a matrix over its main diagonal, switching row and column indices for non-square matrices?",
        "concept": "For a matrix of size R x C, its transpose has dimensions C x R. Allocate transposedMatrix of size C x R. Loop col from 0 to C - 1 and row from 0 to R - 1: transposedMatrix[col][row] = matrix[row][col]. Return transposedMatrix.",
        "hints": [
            "The element at row r and column c moves to row c and column r.",
            "For non-square matrices (R != C), the dimensions flip: a 2x3 matrix becomes a 3x2 matrix."
        ],
        "trick": "Output dimensions must be cols x rows, not rows x cols.",
        "complexity": "Time: O(R * C) visits every cell once. Space: O(R * C) to store the transposed matrix.",
        "edge_cases": [
            "1xN or Nx1 single vector matrix.",
            "Square matrices (where in-place transpose is possible, but general case requires new matrix)."
        ]
    },
    {
        "folder": "TripleSum",
        "title": "Triple Sum",
        "difficulty": "Medium",
        "topic": "Two Pointers",
        "pattern": "Sort + Fixed Element + Two Pointers (3Sum)",
        "lc_number": 15,
        "lc_title": "3Sum",
        "lc_url": "https://leetcode.com/problems/3sum/",
        "recall": "How do you find all triplets in an array that sum to a given target value in O(N^2) time?",
        "concept": "Sort the array. Iterate i from 0 to n - 3. Set left = i + 1, right = n - 1. While left < right: currentSum = array[i] + array[left] + array[right]. If currentSum == target, append [array[i], array[left], array[right]], increment left, decrement right. If currentSum < target, increment left. If currentSum > target, decrement right.",
        "hints": [
            "Sorting the array turns the 3-variable problem into N iterations of 2Sum.",
            "Use two pointers converging from both ends of the remaining sub-array."
        ],
        "trick": "Sorted array allows deterministic pointer movements: sum too small means left must advance; sum too large means right must decrement.",
        "complexity": "Time: O(N^2) total (O(N log N) sort + O(N) iterations of O(N) two pointers). Space: O(N) to store triplets.",
        "edge_cases": [
            "Target sum negative or zero.",
            "Array with fewer than 3 elements: return empty list.",
            "No triplet equals target."
        ]
    },
    {
        "folder": "TwoSum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Hash Set / Map Complement Lookup",
        "lc_number": 1,
        "lc_title": "Two Sum",
        "lc_url": "https://leetcode.com/problems/two-sum/",
        "recall": "How do you find two distinct numbers in an array that sum to a given target?",
        "concept": "Use a hash set to store seen numbers. For each num in array, compute potentialMatch = target - num. If potentialMatch is in the hash set, return [potentialMatch, num]. Otherwise, add num to hash set.",
        "hints": [
            "For each number x, what number y do you need such that x + y = target?",
            "Store visited numbers in a hash table for instant O(1) membership checks."
        ],
        "trick": "Checking set membership before inserting the current number ensures we never pair a number with itself.",
        "complexity": "Time: O(N) average time. Space: O(N) auxiliary space for the hash set.",
        "edge_cases": [
            "Target can be formed by two identical numbers if array contains both: [3, 3] target 6.",
            "No pair sums to target: return empty array."
        ]
    },
    {
        "folder": "ValidateSubsequence",
        "title": "Validate Subsequence",
        "difficulty": "Easy",
        "topic": "Two Pointers",
        "pattern": "Greedy Sequence Pointer Matching",
        "lc_number": 392,
        "lc_title": "Is Subsequence",
        "lc_url": "https://leetcode.com/problems/is-subsequence/",
        "recall": "How do you determine if a sequence is a valid subsequence of an array (appears in the same relative order)?",
        "concept": "Initialize seqIdx = 0. Iterate through array with arrIdx = 0. Whenever array[arrIdx] == sequence[seqIdx], increment seqIdx. If seqIdx == sequence.length at any point, all subsequence elements were found in order; return true. If loop finishes and seqIdx < sequence.length, return false.",
        "hints": [
            "A subsequence preserves relative order but does not need to be contiguous.",
            "Move a pointer through sequence only when a match is found in array."
        ],
        "trick": "Early return: if seqIdx == sequence.length, return true immediately without scanning the rest of the array.",
        "complexity": "Time: O(N) where N is array length. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Sequence longer than array: immediately false.",
            "Identical array and sequence: true.",
            "Empty sequence: always true."
        ]
    },
    {
        "folder": "ZeroSumSubArray",
        "title": "Zero Sum Subarray",
        "difficulty": "Medium",
        "topic": "Arrays & Hashing",
        "pattern": "Prefix Sum Frequency / Set",
        "lc_number": 560,
        "lc_title": "Subarray Sum Equals K",
        "lc_url": "https://leetcode.com/problems/subarray-sum-equals-k/",
        "recall": "How do you check if an array contains a contiguous subarray that sums to zero in O(N) time?",
        "concept": "Maintain a running prefixSum and a hash set of seen prefix sums, initialized with {0}. For each num in nums: prefixSum += num. If prefixSum is already in the set, then the elements between that previous occurrence and the current index sum to zero; return true! Otherwise, add prefixSum to set. If loop finishes, return false.",
        "hints": [
            "If prefix sum at index i equals prefix sum at index j (i < j), what is the sum of subarray [i+1..j]?",
            "Remember to initialize your set with 0 to catch subarrays starting at index 0."
        ],
        "trick": "A subarray sum(A[i..j]) equals prefixSum[j] - prefixSum[i-1]. If prefixSum[j] == prefixSum[i-1], the sum is 0. Initializing the set with 0 covers subarrays starting at index 0.",
        "complexity": "Time: O(N) single pass. Space: O(N) to store prefix sums in a set.",
        "edge_cases": [
            "Single element 0: [0] -> true.",
            "The entire array sums to zero: [-1, 1] -> true.",
            "No zero sum subarray: [1, 2, 3] -> false."
        ]
    }
]

print("Loaded canonical + AlgoExpert:", len(PROBLEMS_DATA))
