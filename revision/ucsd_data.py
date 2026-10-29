# 30 UC San Diego Algorithmic Toolbox problems
UCSD_PROBLEMS = [
    {
        "folder": "1_binary_search",
        "title": "Binary Search",
        "difficulty": "Easy",
        "topic": "Binary Search",
        "pattern": "Sorted Array Halving",
        "lc_number": 704,
        "lc_title": "Binary Search",
        "lc_url": "https://leetcode.com/problems/binary-search/",
        "recall": "How do you search for a target value in a sorted array in guaranteed O(log N) time?",
        "concept": "Set low = 0, high = n - 1. While low <= high: mid = low + (high - low) // 2. If a[mid] == target, return mid. If a[mid] < target, target must be in right half (low = mid + 1). If a[mid] > target, target must be in left half (high = mid - 1). Return -1 if not found.",
        "hints": [
            "At each step, compare target with the middle element.",
            "Half of the remaining search space is eliminated in each iteration."
        ],
        "trick": "Compute mid using low + (high - low) // 2 to avoid integer overflow that occurs with (low + high) // 2 in 32-bit languages.",
        "complexity": "Time: O(log N) iterations. Space: O(1) iterative.",
        "edge_cases": [
            "Target not present: returns -1.",
            "Target at index 0 or index n - 1.",
            "Single element array."
        ]
    },
    {
        "folder": "1_fibonacci_number",
        "title": "Fibonacci Number",
        "difficulty": "Easy",
        "topic": "Dynamic Programming",
        "pattern": "Bottom-Up Iterative DP (Two Variables)",
        "lc_number": 509,
        "lc_title": "Fibonacci Number",
        "lc_url": "https://leetcode.com/problems/fibonacci-number/",
        "recall": "How do you calculate F(n) in O(N) time and O(1) space, avoiding exponential recursion?",
        "concept": "F(0) = 0, F(1) = 1. Iteratively compute F(i) = F(i-1) + F(i-2) using two variables: prev2 = 0, prev1 = 1. In each step: curr = prev1 + prev2, prev2 = prev1, prev1 = curr. Return prev1.",
        "hints": [
            "Naive recursion computes the same sub-problems repeatedly, taking O(2^N) time.",
            "You only need the previous two Fibonacci values to compute the next."
        ],
        "trick": "Storing only the last two values reduces space from O(N) to O(1).",
        "complexity": "Time: O(N) additions. Space: O(1) constant variables.",
        "edge_cases": [
            "n = 0: returns 0.",
            "n = 1: returns 1."
        ]
    },
    {
        "folder": "1_maximum_amount_of_gold",
        "title": "Maximum Amount of Gold (0-1 Knapsack)",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "0-1 Knapsack without Repetitions (1D Backward DP)",
        "lc_number": 416,
        "lc_title": "Partition Equal Subset Sum",
        "lc_url": "https://leetcode.com/problems/partition-equal-subset-sum/",
        "recall": "Given knapsack capacity W and gold bar weights, how do you pack the maximum weight of gold where each bar can be taken at most once?",
        "concept": "Classic 0-1 knapsack where value equals weight. Maintain dp[w] = maximum weight attainable with capacity w. Initialize dp array of size W + 1 with 0. For each gold bar of weight barWeight: iterate w from W down to barWeight: dp[w] = max(dp[w], dp[w - barWeight] + barWeight). Return dp[W].",
        "hints": [
            "For each bar, decide whether to include it or skip it.",
            "Iterate capacity w backwards from W down to barWeight to ensure each bar is used at most once."
        ],
        "trick": "Iterating backwards across the capacity dimension in a 1D DP array guarantees 0-1 knapsack semantics (no item reuse) in O(W) space.",
        "complexity": "Time: O(N * W) where N is number of gold bars and W is knapsack capacity. Space: O(W) 1D DP array.",
        "edge_cases": [
            "Capacity W smaller than all bars: returns 0.",
            "Sum of all bars <= W: take all bars.",
            "Single bar fitting capacity."
        ]
    },
    {
        "folder": "1_money_change",
        "title": "Money Change (Greedy)",
        "difficulty": "Easy",
        "topic": "Greedy",
        "pattern": "Canonical Coin Denominations Greedy Choice",
        "lc_number": 860,
        "lc_title": "Lemonade Change",
        "lc_url": "https://leetcode.com/problems/lemonade-change/",
        "recall": "With coins of denominations 10, 5, and 1, how do you make change for amount m with the minimum number of coins?",
        "concept": "For canonical coin systems (like 10, 5, 1), the greedy choice is mathematically guaranteed to be optimal. Take as many 10-coins as possible: count += m // 10, m %= 10. Then take as many 5-coins as possible: count += m // 5, m %= 5. Finally, take remaining amount in 1-coins: count += m.",
        "hints": [
            "Always pick the largest denomination that does not exceed the remaining amount.",
            "Since denominations are multiples (10 = 2*5, 5 = 5*1), the greedy choice is strictly optimal."
        ],
        "trick": "Integer division count = m // 10 + (m % 10) // 5 + (m % 5) computes the answer in O(1) math operations without loops.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "m < 5: all 1-coins.",
            "m exact multiple of 10: only 10-coins."
        ]
    },
    {
        "folder": "1_money_change_again",
        "title": "Money Change Again (Coin Change DP)",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "Unbounded Knapsack / Minimum Steps DP",
        "lc_number": 322,
        "lc_title": "Coin Change",
        "lc_url": "https://leetcode.com/problems/coin-change/",
        "recall": "For non-canonical coin denominations (e.g. 1, 3, 4), why does greedy fail, and how does DP find the minimum coin count?",
        "concept": "Greedy fails for amount 6 with coins [1, 3, 4]: greedy takes 4 + 1 + 1 = 3 coins, while optimal is 3 + 3 = 2 coins! Use Dynamic Programming: dp[m] = min coins to change amount m. Base case: dp[0] = 0. For m from 1 to money: dp[m] = 1 + min(dp[m - coin]) for each coin <= m. Return dp[money].",
        "hints": [
            "Why does greedy fail for amount = 6 with coins {1, 3, 4}?",
            "dp[m] depends on the optimal answers for m - 1, m - 3, and m - 4."
        ],
        "trick": "Initialize dp array with infinity, dp[0] = 0. Sub-problems overlap, making bottom-up DP linear in amount.",
        "complexity": "Time: O(money * number of coin denominations). Space: O(money) DP array.",
        "edge_cases": [
            "money = 0: 0 coins.",
            "money smaller than smallest coin (if 1-coin wasn't present)."
        ]
    },
    {
        "folder": "2_last_digit_of_fibonacci_number",
        "title": "Last Digit of Fibonacci Number",
        "difficulty": "Easy",
        "topic": "Math & DP",
        "pattern": "Pisano Period Modulo 10 (Cycle of 60)",
        "lc_number": 509,
        "lc_title": "Fibonacci Number",
        "lc_url": "https://leetcode.com/problems/fibonacci-number/",
        "recall": "How do you find the last digit of the n-th Fibonacci number for n up to 10^7 without computing large numbers?",
        "concept": "The last digit of F(n) is F(n) % 10. By modular arithmetic, (a + b) % 10 = ((a % 10) + (b % 10)) % 10. Furthermore, the last digits of Fibonacci numbers repeat with a Pisano period of exactly 60! Thus F(n) % 10 = F(n % 60) % 10. We only need to compute up to index n % 60.",
        "hints": [
            "You only care about the units digit in every addition step.",
            "The sequence of last digits of Fibonacci numbers is periodic with period 60."
        ],
        "trick": "Reducing n modulo 60 first reduces computation to at most 60 additions.",
        "complexity": "Time: O(1) or O(min(n, 60)) additions. Space: O(1).",
        "edge_cases": [
            "n = 0: 0.",
            "n = 1: 1.",
            "n very large (e.g. 10^7): n % 60 handles it instantly."
        ]
    },
    {
        "folder": "2_majority_element",
        "title": "Majority Element (Divide & Conquer)",
        "difficulty": "Medium",
        "topic": "Divide & Conquer",
        "pattern": "Divide and Conquer / Boyer-Moore Voting",
        "lc_number": 169,
        "lc_title": "Majority Element",
        "lc_url": "https://leetcode.com/problems/majority-element/",
        "recall": "How do you check if a sequence contains an element appearing strictly more than n/2 times using Divide and Conquer?",
        "concept": "Divide: split array into left and right halves. If a majority element exists in the whole array, it must be the majority element of at least one of the two halves. Recursively find majority candidate of left half and right half. If they agree, that candidate wins. If they disagree, count occurrences of both candidates across the current range and return whichever has count > (high - low + 1) // 2.",
        "hints": [
            "If an element appears more than n/2 times in the whole array, it must appear more than half the time in at least one half.",
            "Recurse on left and right, then compare candidate frequencies in O(N)."
        ],
        "trick": "Recurrence T(N) = 2T(N/2) + O(N) yields O(N log N) time via Master Theorem. Boyer-Moore Voting optimizes this to O(N).",
        "complexity": "Time: O(N log N) for D&C, or O(N) for Boyer-Moore. Space: O(log N) recursion depth.",
        "edge_cases": [
            "No element has frequency > n/2: return -1.",
            "All elements distinct.",
            "Single element array."
        ]
    },
    {
        "folder": "2_maximum_pairwise_product",
        "title": "Maximum Pairwise Product",
        "difficulty": "Easy",
        "topic": "Greedy",
        "pattern": "Single Pass Top-2 Largest Elements",
        "lc_number": 1464,
        "lc_title": "Maximum Product of Two Elements in an Array",
        "lc_url": "https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/",
        "recall": "How do you find the maximum product of two distinct elements in an array in O(N) time without sorting?",
        "concept": "The maximum product of two positive numbers is the product of the two largest numbers. Find max1 and max2 in a single linear pass: maintain max1 = -1, max2 = -1. For each x: if x > max1: max2 = max1, max1 = x; else if x > max2: max2 = x. The maximum pairwise product is (long) max1 * max2.",
        "hints": [
            "Sorting takes O(N log N); can you find the two largest numbers in one pass?",
            "Watch out for 32-bit integer overflow when multiplying two numbers up to 10^5."
        ],
        "trick": "Cast operands to 64-bit integer (long / uint64) before multiplying to avoid 32-bit overflow.",
        "complexity": "Time: O(N) single pass. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Two largest elements are equal: [5, 5, 2] -> max1 = 5, max2 = 5.",
            "Large numbers near 2 * 10^5: product exceeds 2^31 - 1."
        ]
    },
    {
        "folder": "2_maximum_value_of_the_loot",
        "title": "Maximum Value of the Loot (Fractional Knapsack)",
        "difficulty": "Medium",
        "topic": "Greedy",
        "pattern": "Greedy by Value-to-Weight Ratio",
        "lc_number": None,
        "lc_title": "Fractional Knapsack",
        "lc_url": "https://leetcode.com/problems/maximum-units-on-a-truck/",
        "recall": "Given items with values and weights, and a knapsack of capacity W, how do you maximize total value if fractions of items can be taken?",
        "concept": "Calculate unit value density for each item: density = value / weight. Sort items in descending order of unit density. Greedily take as much of the highest-density item as possible: take = min(item.weight, remainingCapacity). Add take * density to total value, and decrement remainingCapacity -= take. Stop when knapsack is full.",
        "hints": [
            "Since items can be divided continuously, which item gives the most bang for your buck per unit weight?",
            "Sort items by value / weight descending."
        ],
        "trick": "Fractional knapsack admits an optimal greedy solution because we can always fill any remaining fraction with the next densest item.",
        "complexity": "Time: O(N log N) dominated by sorting items. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Total weight of all items <= W: take everything.",
            "Items with zero weight (if permitted) or capacity W = 0.",
            "Use double precision for floating-point values."
        ]
    },
    {
        "folder": "2_partitioning_souvenirs",
        "title": "Partitioning Souvenirs (3-Way Equal Partition)",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "Subset Sum DP / Backtracking with Pruning",
        "lc_number": 698,
        "lc_title": "Partition to K Equal Sum Subsets",
        "lc_url": "https://leetcode.com/problems/partition-to-k-equal-sum-subsets/",
        "recall": "How do you determine if a set of integers can be partitioned into 3 subsets with equal sums?",
        "concept": "Total sum S must be divisible by 3 (target = S / 3). If S % 3 != 0, return 0. Use 2D/3D subset sum DP or backtracking with memoization. In DP: dp[i][s1][s2] = boolean whether prefix i can form subset 1 with sum s1 and subset 2 with sum s2 (subset 3 gets the remainder). If dp[N][target][target] is true, return 1.",
        "hints": [
            "First check: is the total sum divisible by 3?",
            "If total sum is S, each of the three subsets must sum to exactly S / 3."
        ],
        "trick": "Sort items descending before backtracking or DP to prune large impossible branches immediately.",
        "complexity": "Time: O(N * (S/3)^2) with DP, or O(3^N) pruned backtracking. Space: O((S/3)^2) DP table.",
        "edge_cases": [
            "Total sum not divisible by 3: immediately return 0.",
            "Any single item > target: immediately return 0.",
            "Fewer than 3 items: return 0."
        ]
    },
    {
        "folder": "2_primitive_calculator",
        "title": "Primitive Calculator",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "Shortest Path 1D DP with Predecessor Backtracking",
        "lc_number": 279,
        "lc_title": "Perfect Squares",
        "lc_url": "https://leetcode.com/problems/perfect-squares/",
        "recall": "Given an integer n, how do you find the minimum operations (+1, *2, *3) to reach n starting from 1, and reconstruct the sequence?",
        "concept": "Greedy fails (e.g. for n = 10: greedy does 10 -> 9 -> 3 -> 1 takes 3 ops, but 10 -> 5 -> 4 -> 2 -> 1 takes 4; for other numbers greedy gives suboptimal steps). Use DP: minOps[i] is min operations to reach i from 1. For i from 2 to n: minOps[i] = minOps[i - 1] + 1; if i % 2 == 0: minOps[i] = min(minOps[i], minOps[i // 2] + 1); if i % 3 == 0: minOps[i] = min(minOps[i], minOps[i // 3] + 1). Backtrack from n to 1 to reconstruct sequence.",
        "hints": [
            "Why does greedy fail? (e.g. dividing by 3 whenever possible doesn't always lead to the shortest path).",
            "Store min operations for all numbers from 1 to n in a DP table, then trace backwards."
        ],
        "trick": "Backtrack from n down to 1 by checking which transition (curr - 1, curr / 2, curr / 3) achieved minOps[curr] - 1.",
        "complexity": "Time: O(N) linear DP. Space: O(N) array to store minimum operations.",
        "edge_cases": [
            "n = 1: 0 operations, sequence [1].",
            "Powers of 3: optimal is repeated *3.",
            "Numbers where +1 early enables a *3 division."
        ]
    },
    {
        "folder": "3_car_fueling",
        "title": "Car Fueling",
        "difficulty": "Medium",
        "topic": "Greedy",
        "pattern": "Farthest Reachable Station (Greedy Leapfrog)",
        "lc_number": 134,
        "lc_title": "Gas Station",
        "lc_url": "https://leetcode.com/problems/gas-station/",
        "recall": "To travel distance d with tank capacity m, what is the minimum number of refueling stops needed?",
        "concept": "Add start (0) and destination (d) to stops array. Maintain currentStop = 0 and refills = 0. While currentStop < numStops: lastStop = currentStop. While currentStop < numStops and stops[currentStop + 1] - stops[lastStop] <= m: advance currentStop. If currentStop == lastStop: the next stop is unreachable (gap > m), return -1. If currentStop < destination: refills++.",
        "hints": [
            "Always drive as far as possible on the current tank before refueling.",
            "Refuel at the farthest reachable gas station."
        ],
        "trick": "If you cannot advance at least one station forward from your last refueling stop, the destination is unreachable -> return -1.",
        "complexity": "Time: O(N) where N is number of gas stations. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Destination reachable without stops: returns 0.",
            "Gap between any two adjacent stations > m: returns -1.",
            "Refueling at the final stop is unnecessary."
        ]
    },
    {
        "folder": "3_edit_distance",
        "title": "Edit Distance",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "2D Grid Levenshtein Distance DP",
        "lc_number": 72,
        "lc_title": "Edit Distance",
        "lc_url": "https://leetcode.com/problems/edit-distance/",
        "recall": "How do you compute the minimum number of insertions, deletions, and substitutions to transform string A into string B?",
        "concept": "Define dp[i][j] = edit distance between prefix A[0..i-1] and B[0..j-1]. Base cases: dp[i][0] = i (i deletions), dp[0][j] = j (j insertions). If A[i-1] == B[j-1], dp[i][j] = dp[i-1][j-1] (match, cost 0). Otherwise, dp[i][j] = 1 + min(dp[i-1][j] (deletion), dp[i][j-1] (insertion), dp[i-1][j-1] (substitution)). Return dp[n][m].",
        "hints": [
            "If characters match, edit distance is unchanged from the prefixes.",
            "If characters mismatch, take 1 + min of insert, delete, or substitute."
        ],
        "trick": "Space can be optimized to O(min(n, m)) by keeping only the previous row in memory.",
        "complexity": "Time: O(N * M) filling N x M table. Space: O(N * M) or O(min(N, M)) with row compression.",
        "edge_cases": [
            "One or both strings empty: return length of the other string.",
            "Identical strings: return 0.",
            "Completely disjoint characters: requires max(n, m) operations."
        ]
    },
    {
        "folder": "3_greatest_common_divisor",
        "title": "Greatest Common Divisor",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Euclidean Algorithm (gcd(a, b) = gcd(b, a % b))",
        "lc_number": 1979,
        "lc_title": "Find Greatest Common Divisor of Array",
        "lc_url": "https://leetcode.com/problems/find-greatest-common-divisor-of-array/",
        "recall": "How does Euclid's algorithm find the GCD of two integers in logarithmic time?",
        "concept": "Euclid's lemma: gcd(a, b) = gcd(b, a % b). Base case: when b == 0, gcd is a. In each step, the remainder a % b is strictly less than a / 2 when a >= b, guaranteeing logarithmic convergence.",
        "hints": [
            "Division remainder theorem: any common divisor of a and b also divides a % b.",
            "Repeat a, b = b, a % b until b == 0."
        ],
        "trick": "In each two iterations, the larger number is at least halved: (a % b) < a / 2, guaranteeing at most 2 * log2(b) steps.",
        "complexity": "Time: O(log(min(a, b))) Euclidean divisions. Space: O(1) iterative.",
        "edge_cases": [
            "b = 0: gcd is a.",
            "a = b: gcd is a.",
            "Prime numbers: gcd is 1."
        ]
    },
    {
        "folder": "3_improving_quicksort",
        "title": "Improving QuickSort (3-Way Partitioning)",
        "difficulty": "Medium",
        "topic": "Sorting",
        "pattern": "Dutch National Flag 3-Way Partitioning",
        "lc_number": 75,
        "lc_title": "Sort Colors",
        "lc_url": "https://leetcode.com/problems/sort-colors/",
        "recall": "Why does standard QuickSort degrade to O(N^2) on arrays with many duplicate elements, and how does 3-way partitioning fix it?",
        "concept": "Standard 2-way QuickSort puts equal elements on one side, leading to unbalanced N-1 vs 0 splits on arrays of identical elements. 3-way partitioning partitions the array into three segments: elements < pivot, elements == pivot, and elements > pivot. Recurse ONLY on the < pivot and > pivot sub-arrays, completely ignoring the == pivot middle segment.",
        "hints": [
            "When many duplicate elements exist, grouping all equal elements together into a middle segment eliminates them from further recursion.",
            "Use Dutch National Flag algorithm with three pointers: m1 (boundary for <), i (current), m2 (boundary for >)."
        ],
        "trick": "Sub-arrays containing only elements equal to pivot are completely skipped in subsequent recursive calls, running in O(N) on all-equal arrays.",
        "complexity": "Time: O(N log N) average, O(N) when only few distinct keys exist. Space: O(log N) stack space.",
        "edge_cases": [
            "All elements identical: runs in O(N) time with 0 further recursive calls.",
            "Already sorted array."
        ]
    },
    {
        "folder": "3_maximum_value_of_an_arithmetic_expression",
        "title": "Maximum Value of an Arithmetic Expression",
        "difficulty": "Hard",
        "topic": "Dynamic Programming",
        "pattern": "Interval DP / Matrix Chain Placing Parentheses",
        "lc_number": 241,
        "lc_title": "Different Ways to Add Parentheses",
        "lc_url": "https://leetcode.com/problems/different-ways-to-add-parentheses/",
        "recall": "Given an arithmetic expression with numbers and +, -, * operators, how do you parenthesize it to maximize its final value?",
        "concept": "Maintain two 2D tables: minVal[i][j] and maxVal[i][j] for the sub-expression from number i to number j. For expression length s = 1 to n: for each start i and end j = i + s: iterate split point k between i and j - 1. Compute all 4 combinations of minVal and maxVal around operator at k (min*min, min*max, max*min, max*max). Update maxVal[i][j] and minVal[i][j] with overall max and min. Return maxVal[0][n-1].",
        "hints": [
            "Why do we need BOTH minimum and maximum values? Because multiplying two negative numbers can yield a large positive number!",
            "Solve sub-expressions in increasing order of length (interval DP)."
        ],
        "trick": "Always track both minimum and maximum values for each sub-expression because subtraction of a minimum or multiplication of two negative minimums can produce a maximum.",
        "complexity": "Time: O(N^3) where N is number of digits. Space: O(N^2) for min and max DP tables.",
        "edge_cases": [
            "Expression with single number: maxVal[0][0] = digit.",
            "All subtraction operators: double negatives flip signs.",
            "Multiplication of negative values."
        ]
    },
    {
        "folder": "4_least_common_multiple",
        "title": "Least Common Multiple",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "GCD-to-LCM Relation (a * b) // gcd(a, b)",
        "lc_number": None,
        "lc_title": "Least Common Multiple",
        "lc_url": "https://leetcode.com/problems/find-greatest-common-divisor-of-array/",
        "recall": "How do you compute the LCM of two large integers up to 10^7 without factoring?",
        "concept": "Fundamental identity: a * b = gcd(a, b) * lcm(a, b). Therefore, lcm(a, b) = (a * b) // gcd(a, b). Compute gcd(a, b) first via Euclid's algorithm in O(log(min(a, b))). To avoid intermediate overflow, divide first: (a // gcd(a, b)) * b.",
        "hints": [
            "Identity: lcm(a, b) * gcd(a, b) = a * b.",
            "Compute (a // gcd(a, b)) * b to avoid overflow from a * b."
        ],
        "trick": "Divide before multiplying: (a // gcd(a, b)) * b prevents integer overflow when a * b exceeds 64-bit integer limits.",
        "complexity": "Time: O(log(min(a, b))) for Euclidean gcd. Space: O(1).",
        "edge_cases": [
            "a or b is 1: lcm is the other number.",
            "a == b: lcm is a.",
            "Coprime numbers: lcm is a * b."
        ]
    },
    {
        "folder": "4_longest_common_subsequence_of_two_sequences",
        "title": "Longest Common Subsequence of Two Sequences",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "2D Grid LCS DP",
        "lc_number": 1143,
        "lc_title": "Longest Common Subsequence",
        "lc_url": "https://leetcode.com/problems/longest-common-subsequence/",
        "recall": "How do you find the length of the longest subsequence common to two sequences of integers?",
        "concept": "Define dp[i][j] = LCS length of prefix a[0..i-1] and b[0..j-1]. If a[i-1] == b[j-1]: dp[i][j] = 1 + dp[i-1][j-1]. Otherwise: dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Initialize (n+1) x (m+1) table with 0s. Return dp[n][m].",
        "hints": [
            "If current characters match, can we extend the LCS of both prefixes?",
            "If they mismatch, the LCS is the maximum of dropping the char from sequence A or from sequence B."
        ],
        "trick": "dp[i][j] only depends on current row and previous row, allowing space optimization to O(min(N, M)).",
        "complexity": "Time: O(N * M). Space: O(N * M) or O(min(N, M)).",
        "edge_cases": [
            "No common elements: returns 0.",
            "One sequence is a subsequence of the other: returns min(n, m).",
            "Identical sequences."
        ]
    },
    {
        "folder": "4_maximum_advertisement_revenue",
        "title": "Maximum Advertisement Revenue",
        "difficulty": "Easy",
        "topic": "Greedy",
        "pattern": "Rearrangement Inequality / Dot Product Sort",
        "lc_number": 646,
        "lc_title": "Maximum Length of Pair Chain",
        "lc_url": "https://leetcode.com/problems/maximum-length-of-pair-chain/",
        "recall": "Given click values a and slot prices b, how do you pair them to maximize the dot product sum(a_i * b_i)?",
        "concept": "By the Rearrangement Inequality, the sum of products sum(a_i * b_i) is strictly maximized when both sequences are sorted in the same monotonic order. Sort sequence a in ascending order and sequence b in ascending order. Then sum a[i] * b[i] for all i. Use 64-bit integer to prevent overflow.",
        "hints": [
            "Pair the largest click value with the largest price, second largest with second largest, etc.",
            "Sort both sequences ascending and compute their dot product."
        ],
        "trick": "The Rearrangement Inequality proves that pairing sorted elements greedily produces the global maximum.",
        "complexity": "Time: O(N log N) for sorting both arrays. Space: O(1) or O(log N) sorting space.",
        "edge_cases": [
            "Negative values: product of two negative values is positive, which sorting naturally pairs correctly.",
            "Use 64-bit long for accumulated sum."
        ]
    },
    {
        "folder": "4_number_of_inversions",
        "title": "Number of Inversions",
        "difficulty": "Medium",
        "topic": "Divide & Conquer",
        "pattern": "Merge Sort Inversion Counting",
        "lc_number": 315,
        "lc_title": "Count of Smaller Numbers After Self",
        "lc_url": "https://leetcode.com/problems/count-of-smaller-numbers-after-self/",
        "recall": "How do you count the number of inversions (pairs i < j with a[i] > a[j]) in O(N log N) time?",
        "concept": "Count inversions during Merge Sort. Split array into left and right halves. Recursively count inversions in left half and right half. During the merge step, when an element from right half b[j] is smaller than element from left half a[i], it is smaller than ALL remaining elements in the left half from index i to mid! Add (mid - i) to inversion count. Return leftInversions + rightInversions + splitInversions.",
        "hints": [
            "When merging two sorted arrays, if right[j] < left[i], how many elements in left are strictly greater than right[j]?",
            "Every element from left[i] to left[mid] forms an inversion with right[j]."
        ],
        "trick": "When right[j] < left[i], add (mid - i) directly to the inversion counter in O(1). This counts all split inversions without extra comparisons.",
        "complexity": "Time: O(N log N) same as Merge Sort. Space: O(N) auxiliary merge array.",
        "edge_cases": [
            "Already sorted array: 0 inversions.",
            "Reverse sorted array: maximum N * (N - 1) / 2 inversions.",
            "Inversion count can exceed 32-bit int: use 64-bit long."
        ]
    },
    {
        "folder": "5_collecting_signatures",
        "title": "Collecting Signatures (Segment Covering)",
        "difficulty": "Medium",
        "topic": "Greedy",
        "pattern": "Greedy Interval Scheduling by Right Endpoints",
        "lc_number": 452,
        "lc_title": "Minimum Number of Arrows to Burst Balloons",
        "lc_url": "https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/",
        "recall": "Given a set of segments [l_i, r_i], how do you find the minimum number of points such that each segment contains at least one point?",
        "concept": "Sort segments by right endpoint r_i ascending. Pick the right endpoint of the first segment as your first point: point = segments[0].r. For each subsequent segment: if segment.l > point, the current segment is not covered; pick a new point = segment.r and add to points list. Otherwise, the segment is already covered by the existing point.",
        "hints": [
            "Sorting by right endpoints allows you to place a point as far right as possible, maximizing its chance of covering future segments.",
            "Only place a new point when a segment's left endpoint exceeds the current point."
        ],
        "trick": "Always place the point at the segment's right endpoint segment.r. Placing it anywhere earlier would strictly reduce the opportunities to cover subsequent segments.",
        "complexity": "Time: O(N log N) to sort segments. Space: O(N) to store chosen points.",
        "edge_cases": [
            "Segments overlapping at a single point: [[1, 3], [3, 5]] covered by point 3.",
            "One segment inside another: [[1, 5], [2, 3]] sorted by right endpoint puts [2, 3] first, covering both."
        ]
    },
    {
        "folder": "5_fibonacci_number_again",
        "title": "Huge Fibonacci Number Modulo M",
        "difficulty": "Medium",
        "topic": "Math & Number Theory",
        "pattern": "Pisano Period Modulo M",
        "lc_number": 509,
        "lc_title": "Fibonacci Number",
        "lc_url": "https://leetcode.com/problems/fibonacci-number/",
        "recall": "How do you compute F(n) % m for astronomical n (up to 10^14) and m up to 10^3?",
        "concept": "The Fibonacci sequence modulo m is strictly periodic, known as the Pisano Period. The period always begins with 0, 1. Find the period length P by generating Fibonacci numbers modulo m until seeing 0 followed by 1 (at i >= 1). Then F(n) % m = F(n % P) % m. Since P <= 6 * m, finding the period and computing the answer takes O(m) time.",
        "hints": [
            "The sequence F(n) % m repeats periodically.",
            "Detect the period by looking for the repeat of 0, 1.",
            "Once period length P is found, compute n % P."
        ],
        "trick": "Pisano period always starts with 0, 1. The period length never exceeds 6 * m, turning an exponential calculation into at most 6000 additions.",
        "complexity": "Time: O(m) to find Pisano period. Space: O(1) auxiliary variables.",
        "edge_cases": [
            "n = 0: 0.",
            "n = 1: 1 % m.",
            "m = 2: period is 3."
        ]
    },
    {
        "folder": "5_longest_common_subsequence_of_three_sequences",
        "title": "LCS of Three Sequences",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "pattern": "3D Grid Dynamic Programming",
        "lc_number": 1143,
        "lc_title": "Longest Common Subsequence",
        "lc_url": "https://leetcode.com/problems/longest-common-subsequence/",
        "recall": "How do you find the longest common subsequence of three sequences of lengths up to 100?",
        "concept": "Extend 2D LCS to a 3D DP table dp[i][j][k] representing the LCS of prefixes a[0..i-1], b[0..j-1], and c[0..k-1]. If a[i-1] == b[j-1] == c[k-1]: dp[i][j][k] = 1 + dp[i-1][j-1][k-1]. Otherwise: dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]). Return dp[n1][n2][n3].",
        "hints": [
            "Can you generalize the 2D recurrence relation to three dimensions?",
            "If all three characters match, increment the 3D diagonal by 1; otherwise take max along the 3 axes."
        ],
        "trick": "Notice that computing LCS(A, B) and then LCS with C does NOT work! All three sequences must be matched simultaneously in the 3D DP.",
        "complexity": "Time: O(N1 * N2 * N3) states. Space: O(N1 * N2 * N3) or O(N2 * N3) with 2D layer compression.",
        "edge_cases": [
            "No elements common to all three: returns 0.",
            "Sequences of different lengths.",
            "Identical sequences."
        ]
    },
    {
        "folder": "5_organizing_a_lottery",
        "title": "Organizing a Lottery (Points and Segments)",
        "difficulty": "Hard",
        "topic": "Divide & Conquer & Sorting",
        "pattern": "Sweep-line Event Sorting",
        "lc_number": 1851,
        "lc_title": "Minimum Interval to Include Each Query",
        "lc_url": "https://leetcode.com/problems/minimum-interval-to-include-each-query/",
        "recall": "Given N segments and M query points, how do you find how many segments contain each point in O((N + M) log(N + M)) time?",
        "concept": "Sweep-line algorithm: create events for segment starts, query points, and segment ends. Represent each as (coordinate, event_type, index). Crucial ordering of event_type at identical coordinates: START < POINT < END (e.g. -1 for START, 0 for POINT, +1 for END). Sort events. Iterate through sorted events: if START, activeSegments++; if END, activeSegments--; if POINT, result[point.index] = activeSegments.",
        "hints": [
            "Instead of checking each point against all segments (O(N * M)), treat points and segment boundaries as events along the number line.",
            "If a segment starts at the same coordinate as a point, the segment must be counted before processing the point."
        ],
        "trick": "Tie-breaking at identical coordinates: START (-1) must precede POINT (0), which must precede END (+1) so segments covering the boundary are correctly counted.",
        "complexity": "Time: O((N + M) log(N + M)) sorting events. Space: O(N + M) event storage.",
        "edge_cases": [
            "Point exactly on segment start or end boundary.",
            "Segments with length 0 ([x, x]).",
            "Points outside all segments: return 0."
        ]
    },
    {
        "folder": "6_closest_points",
        "title": "Closest Pair of Points",
        "difficulty": "Hard",
        "topic": "Divide & Conquer",
        "pattern": "Divide and Conquer 2D Plane Split ($O(N \\log N)$)",
        "lc_number": 973,
        "lc_title": "K Closest Points to Origin",
        "lc_url": "https://leetcode.com/problems/k-closest-points-to-origin/",
        "recall": "How do you find the minimum Euclidean distance between any two points in a 2D plane in O(N log N) time?",
        "concept": "Sort points by x-coordinate. Divide: split by vertical line at median x. Recursively find min distance d = min(d_left, d_right). Conquer: build a 'strip' of points within distance d of the dividing line, sorted by y-coordinate. For each point in the strip, only inspect points within vertical distance d. Geometrically, at most 7 points can lie in this d x 2d bounding box! Update d with any closer pair.",
        "hints": [
            "Split the plane vertically in half and recurse on left and right.",
            "The magic is in the strip: points in the strip within distance d of the midline only need to be compared with at most 7 subsequent points sorted by y."
        ],
        "trick": "Geometric sparsity: inside a d x 2d box, no two points on the same side can be closer than d, mathematically capping comparisons in the strip to 7 per point.",
        "complexity": "Time: O(N log N) with presorted y-coordinates. Space: O(N) auxiliary space.",
        "edge_cases": [
            "2 points: base case.",
            "Points with identical x or y coordinates.",
            "Points situated directly on the dividing line."
        ]
    },
    {
        "folder": "6_last_digit_of_the_sum_of_fibonacci_numbers",
        "title": "Last Digit of the Sum of Fibonacci Numbers",
        "difficulty": "Medium",
        "topic": "Math & Number Theory",
        "pattern": "Fibonacci Sum Identity (Sum = F(n+2) - 1)",
        "lc_number": 509,
        "lc_title": "Fibonacci Number",
        "lc_url": "https://leetcode.com/problems/fibonacci-number/",
        "recall": "How do you find the last digit of the sum of the first n Fibonacci numbers (F(0) + F(1) + ... + F(n)) for n up to 10^14?",
        "concept": "Mathematical identity: sum_{i=0}^n F(i) = F(n + 2) - 1. Therefore, (sum_{i=0}^n F(i)) % 10 = (F(n + 2) - 1) % 10. The Pisano period of Fibonacci numbers modulo 10 is 60. Thus compute index = (n + 2) % 60, find F(index) % 10, and compute (F(index) - 1 + 10) % 10.",
        "hints": [
            "Use the telescopic identity: F(i) = F(i+2) - F(i+1), which telescopes to sum = F(n+2) - 1.",
            "Combine this with the Pisano period modulo 10 (which is 60)."
        ],
        "trick": "Adding 10 before modulo: (F((n + 2) % 60) - 1 + 10) % 10 handles negative results when F(n+2) ends in 0.",
        "complexity": "Time: O(1) (at most 60 Fibonacci iterations). Space: O(1).",
        "edge_cases": [
            "n = 0: sum is 0.",
            "n = 1: sum is 1.",
            "F(n+2) % 10 == 0: subtraction yields -1, correctly adjusted to 9 by + 10."
        ]
    },
    {
        "folder": "6_maximum_number_of_prizes",
        "title": "Maximum Number of Prizes (Distinct Summands)",
        "difficulty": "Easy",
        "topic": "Greedy",
        "pattern": "Triangular Progression Greedy Choice",
        "lc_number": None,
        "lc_title": "Distinct Summands",
        "lc_url": "https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/",
        "recall": "How do you represent integer n as the sum of the maximum possible number of distinct positive integers?",
        "concept": "To maximize count, pick the smallest available integers greedily: 1, 2, 3, ... In each step k: if remaining n - k > k, take k, add to prizes, and decrement n -= k. If n - k <= k, taking k would leave a remainder that cannot be strictly greater than k, so take the entire remaining n as the final prize.",
        "hints": [
            "To maximize the number of distinct prizes, give 1 to first place, 2 to second place, etc.",
            "When the remaining candies cannot support the next distinct number + a strictly larger remainder, give all remaining candies to the current prize."
        ],
        "trick": "Condition n - k > k guarantees that whatever remains will be strictly greater than k, keeping all summands distinct.",
        "complexity": "Time: O(sqrt(N)) since 1 + 2 + ... + k ~= k^2 / 2 = n. Space: O(sqrt(N)) to store prizes.",
        "edge_cases": [
            "n = 1: [1].",
            "n = 2: [2].",
            "n = 6: [1, 2, 3]."
        ]
    },
    {
        "folder": "7_last_digit_of_the_sum_of_fibonacci_numbers_again",
        "title": "Last Digit of a Partial Fibonacci Sum",
        "difficulty": "Medium",
        "topic": "Math & Number Theory",
        "pattern": "Prefix Sum Difference of Fibonacci Modulo 10",
        "lc_number": 509,
        "lc_title": "Fibonacci Number",
        "lc_url": "https://leetcode.com/problems/fibonacci-number/",
        "recall": "How do you find the last digit of the partial sum F(m) + F(m+1) + ... + F(n) for large m and n?",
        "concept": "Partial sum S(m, n) = sum_{i=0}^n F(i) - sum_{i=0}^{m-1} F(i). Using the Fibonacci sum identity: sum_{i=0}^k F(i) = F(k+2) - 1. Therefore S(m, n) = (F(n+2) - 1) - (F(m+1) - 1) = F(n+2) - F(m+1). Compute (F((n + 2) % 60) - F((m + 1) % 60) + 10) % 10.",
        "hints": [
            "Partial sum from m to n is TotalSum(n) - TotalSum(m - 1).",
            "S(m, n) simplifies cleanly to F(n + 2) - F(m + 1)."
        ],
        "trick": "S(m, n) = F(n + 2) - F(m + 1). Reduce indices modulo 60 and add 10 before modulo to avoid negative answers.",
        "complexity": "Time: O(1) (at most 60 Fibonacci iterations). Space: O(1).",
        "edge_cases": [
            "m == n: returns F(m) % 10.",
            "m = 0: standard sum from 0 to n."
        ]
    },
    {
        "folder": "7_maximum_salary",
        "title": "Maximum Salary (Largest Number)",
        "difficulty": "Medium",
        "topic": "Greedy & Custom Sort",
        "pattern": "Concatenation Comparator Sort (ab vs ba)",
        "lc_number": 179,
        "lc_title": "Largest Number",
        "lc_url": "https://leetcode.com/problems/largest-number/",
        "recall": "How do you arrange a list of integers to form the largest possible combined number?",
        "concept": "Greedy pairwise comparison: for two numbers a and b (as strings), compare concatenation a + b versus b + a. If a + b > b + a, a should come before b. Sort all numbers using this custom comparator in descending order, then concatenate. If the largest element is '0', the result is '0'.",
        "hints": [
            "Does comparing single digits work? (e.g. 2 vs 21: 221 > 212, so 2 comes first).",
            "Compare concatenated strings: sort by whether a + b > b + a."
        ],
        "trick": "Transitivity: the comparison (a + b) > (b + a) defines a strict weak ordering, guaranteeing a globally optimal arrangement.",
        "complexity": "Time: O(N log N * K) where K is max string length. Space: O(N) to store string representations.",
        "edge_cases": [
            "All zeros: ['0', '0'] -> return '0' (not '00').",
            "Numbers with common prefixes: '9' vs '91' -> '991' > '919'."
        ]
    },
    {
        "folder": "8_last_digit_of_the_sum_of_squares_of_fibonacci_numbers",
        "title": "Last Digit of Sum of Fibonacci Squares",
        "difficulty": "Medium",
        "topic": "Math & Number Theory",
        "pattern": "Fibonacci Area Geometry Identity (F(n) * F(n+1))",
        "lc_number": 509,
        "lc_title": "Fibonacci Number",
        "lc_url": "https://leetcode.com/problems/fibonacci-number/",
        "recall": "How do you find the last digit of F(0)^2 + F(1)^2 + ... + F(n)^2 for n up to 10^14?",
        "concept": "Geometric identity of tiling Fibonacci squares into a rectangle: sum_{i=0}^n F(i)^2 = F(n) * F(n + 1). Therefore, the sum modulo 10 is (F(n) * F(n + 1)) % 10 = ((F(n % 60) % 10) * (F((n + 1) % 60) % 10)) % 10.",
        "hints": [
            "Think of Fibonacci squares forming a rectangle of dimensions F(n) by F(n + 1).",
            "Sum of squares identity: sum(F_i^2) = F(n) * F(n + 1)."
        ],
        "trick": "The sum of squares equals the area of rectangle F(n) * F(n + 1). Reduce indices modulo 60 and multiply their last digits.",
        "complexity": "Time: O(1) (at most 60 Fibonacci iterations). Space: O(1).",
        "edge_cases": [
            "n = 0: 0.",
            "n = 1: 1.",
            "Product of last digits ending in 0."
        ]
    }
]
print("UCSD problems loaded:", len(UCSD_PROBLEMS))
