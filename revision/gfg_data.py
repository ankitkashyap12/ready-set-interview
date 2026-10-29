# 21 GeeksforGeeks problems
GFG_PROBLEMS = [
    {
        "folder": "1. Absolute Value - GFG",
        "title": "Absolute Value",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Branchless / Conditional Sign Inversion",
        "lc_number": None,
        "lc_title": "Math.abs Implementation",
        "lc_url": "https://leetcode.com/problems/calculate-money-in-leetcode-bank/",
        "recall": "How do you compute the absolute value of an integer without using library functions?",
        "concept": "If the number is negative (I < 0), return -I; otherwise return I. In bitwise manipulation, (n ^ (n >> 31)) - (n >> 31) computes absolute value branchlessly.",
        "hints": [
            "Check if the number is less than zero.",
            "Remember that negating a negative number yields its positive magnitude."
        ],
        "trick": "In 32-bit signed two's complement, watch out for Integer.MIN_VALUE (-2^31), as -MIN_VALUE overflows 32-bit signed int.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "Zero: 0 -> 0.",
            "Negative numbers: -32 -> 32.",
            "Integer MIN_VALUE."
        ]
    },
    {
        "folder": "1. Array insert at end - GFG",
        "title": "Array Insert at End",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Direct Index Assignment",
        "lc_number": 27,
        "lc_title": "Remove Element (Array Operations)",
        "lc_url": "https://leetcode.com/problems/remove-element/",
        "recall": "How do you insert an element at the end of a fixed-capacity array at index sizeOfArray - 1?",
        "concept": "Directly assign arr[sizeOfArray - 1] = element. Since array indexing is random access, assigning to the final slot takes O(1) time.",
        "hints": [
            "What is the index of the last element in an array of size N?",
            "Remember that array indexing is 0-based."
        ],
        "trick": "In fixed-size arrays, inserting at the end is an O(1) assignment arr[size - 1] = element without shifting.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "Array of size 1.",
            "Negative or zero element values."
        ]
    },
    {
        "folder": "1. Find first set bit - GFG",
        "title": "Find First Set Bit",
        "difficulty": "Easy",
        "topic": "Bit Manipulation",
        "pattern": "Two's Complement LSB Isolation (n & -n)",
        "lc_number": 191,
        "lc_title": "Number of 1 Bits",
        "lc_url": "https://leetcode.com/problems/number-of-1-bits/",
        "recall": "How do you find the 1-based position of the first set bit (from right to left) in an integer?",
        "concept": "Isolate the lowest set bit using n & -n. The 1-based position corresponds to log2(n & -n) + 1. Alternatively, iteratively check (n & 1); if 1 return count, else right-shift n >>= 1 and increment count.",
        "hints": [
            "What does n & -n do in two's complement arithmetic?",
            "n & -n leaves ONLY the rightmost set bit active. Its position is log2(isolatedBit) + 1."
        ],
        "trick": "Two's complement -n is (~n + 1). Therefore n & -n isolates the lowest set bit in O(1) time.",
        "complexity": "Time: O(1) or O(log N) bit shifts. Space: O(1).",
        "edge_cases": [
            "n == 0: no set bits, return 0.",
            "n is a power of 2: first set bit is the only set bit.",
            "n is odd: first set bit is at position 1."
        ]
    },
    {
        "folder": "2. Array insert at index - GFG",
        "title": "Array Insert at Index",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Right Shift Array Elements",
        "lc_number": 27,
        "lc_title": "Remove Element",
        "lc_url": "https://leetcode.com/problems/remove-element/",
        "recall": "How do you insert an element at a specified index in an array by shifting subsequent elements?",
        "concept": "Shift all elements from index to sizeOfArray - 2 one position to the right, starting from the back (i = sizeOfArray - 1 down to index + 1: arr[i] = arr[i - 1]). Then assign arr[index] = element.",
        "hints": [
            "If you shift from left to right, you overwrite values before moving them! Shift from right to left.",
            "Insert the element at arr[index] after the shift completes."
        ],
        "trick": "Always iterate backwards (from size - 1 down to index + 1) when shifting elements to the right to avoid overwriting unshifted data.",
        "complexity": "Time: O(N) where N is the number of elements shifted. Space: O(1) in-place.",
        "edge_cases": [
            "Inserting at index 0 (maximum shift).",
            "Inserting at the very end index (0 shifts)."
        ]
    },
    {
        "folder": "2. Rightmost different bit - GFG",
        "title": "Rightmost Different Bit",
        "difficulty": "Easy",
        "topic": "Bit Manipulation",
        "pattern": "XOR + Two's Complement LSB Isolation",
        "lc_number": 461,
        "lc_title": "Hamming Distance",
        "lc_url": "https://leetcode.com/problems/hamming-distance/",
        "recall": "Given two numbers m and n, how do you find the 1-based position of the rightmost bit where they differ?",
        "concept": "XOR m and n: x = m ^ n. In x, set bits represent positions where m and n differ. Finding the rightmost different bit is equivalent to finding the first set bit of x. Compute isolated = x & -x and return log2(isolated) + 1. If m == n, return -1.",
        "hints": [
            "Which bitwise operation highlights differing bits between two numbers? XOR!",
            "Once you have m ^ n, find its lowest set bit using x & -x."
        ],
        "trick": "m ^ n produces 1s exactly where m and n have different bits. Then x & -x isolates the rightmost difference in O(1).",
        "complexity": "Time: O(1) bitwise operations. Space: O(1).",
        "edge_cases": [
            "m == n: numbers are identical, return -1.",
            "Difference is at bit 0 (one even, one odd): returns 1."
        ]
    },
    {
        "folder": "3. Check whether K-th bit is set or not - GFG",
        "title": "Check K-th Bit Set",
        "difficulty": "Easy",
        "topic": "Bit Manipulation",
        "pattern": "Bitwise Shift and Mask ((n >> k) & 1)",
        "lc_number": 191,
        "lc_title": "Number of 1 Bits",
        "lc_url": "https://leetcode.com/problems/number-of-1-bits/",
        "recall": "How do you check if the k-th bit (0-indexed or 1-indexed) of an integer n is set?",
        "concept": "Right shift n by k positions and test the lowest bit: (n >> k) & 1 == 1. Alternatively, create a mask 1 << k and check (n & (1 << k)) != 0.",
        "hints": [
            "Shift the k-th bit to the 0th position using n >> k, then AND with 1.",
            "Verify whether k is 0-indexed or 1-indexed in the problem statement."
        ],
        "trick": "Using (n >> k) & 1 avoids potential overflow that can occur when shifting 1 << 31 in signed integers.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "k == 0 (LSB).",
            "k == 31 (sign bit or MSB).",
            "n == 0 (all bits 0 -> false)."
        ]
    },
    {
        "folder": "3. Mean And Median of Array - GFG",
        "title": "Mean and Median of Array",
        "difficulty": "Easy",
        "topic": "Math & Sorting",
        "pattern": "Sum Division & Midpoint of Sorted Array",
        "lc_number": None,
        "lc_title": "Find Median of Array",
        "lc_url": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
        "recall": "How do you compute the mean (floor) and median of an unsorted integer array?",
        "concept": "Mean: sum all elements and compute sum // N. Median: sort the array. If N is odd, median is a[N // 2]. If N is even, median is floor((a[(N - 1) // 2] + a[N // 2]) / 2).",
        "hints": [
            "Mean is total sum divided by N.",
            "Median requires sorting the array first, then picking the middle element (or average of two middles)."
        ],
        "trick": "Watch for integer division vs floor: in Java/C++, integer division truncates towards zero. Use 64-bit sum to prevent overflow.",
        "complexity": "Time: O(N log N) to sort for median; O(N) for mean. Space: O(1) or O(log N) sorting space.",
        "edge_cases": [
            "Even vs odd N for median calculation.",
            "Large array elements where total sum exceeds 32-bit integer limit."
        ]
    },
    {
        "folder": "4. Count total set bits - GFG",
        "title": "Count Total Set Bits from 1 to N",
        "difficulty": "Medium",
        "topic": "Bit Manipulation",
        "pattern": "Bit Position Periodicity (2^i cycles)",
        "lc_number": 338,
        "lc_title": "Counting Bits",
        "lc_url": "https://leetcode.com/problems/counting-bits/",
        "recall": "How do you count the total number of set bits across all numbers from 1 to N in O(log N) time?",
        "concept": "For each bit position i (from 0 up to 2^i <= N): the bit toggles every 2^i numbers with a cycle length of 2^(i+1). In each complete cycle, there are 2^i set bits. Total complete cycles = (N + 1) // 2^(i+1). Remaining numbers = (N + 1) % 2^(i+1). Add fullCycles * 2^i + max(0, remainder - 2^i) to the total.",
        "hints": [
            "Look at each bit position independently. Does bit i follow a regular periodic cycle of 0s and 1s?",
            "Bit i has a period of 2^(i+1), with 2^i consecutive 1s in every period."
        ],
        "trick": "Formula for bit i: ((N + 1) // 2^(i+1)) * 2^i + max(0, (N + 1) % 2^(i+1) - 2^i). Sum this over all i where 2^i <= N in O(log N).",
        "complexity": "Time: O(log N) operations (at most 32 iterations). Space: O(1).",
        "edge_cases": [
            "N = 0 or N = 1.",
            "Powers of 2 (e.g. N = 2^k - 1: total set bits is k * 2^(k-1))."
        ]
    },
    {
        "folder": "4. Factorial Of Number - GFG",
        "title": "Factorial of Number",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Iterative Product Accumulator",
        "lc_number": 172,
        "lc_title": "Factorial Trailing Zeroes",
        "lc_url": "https://leetcode.com/problems/factorial-trailing-zeroes/",
        "recall": "How do you calculate n! for non-negative integers?",
        "concept": "Base cases: 0! = 1, 1! = 1. Iteratively multiply fact *= i for i from 2 up to n. Use 64-bit integer (long) or BigInteger for larger values.",
        "hints": [
            "0! is defined as 1.",
            "Factorials grow super-exponentially; use 64-bit integer types."
        ],
        "trick": "Factorial of 0 is 1. An iterative loop from 1 to N avoids call stack overhead.",
        "complexity": "Time: O(N). Space: O(1).",
        "edge_cases": [
            "n = 0: returns 1.",
            "n = 1: returns 1."
        ]
    },
    {
        "folder": "5. Bit Difference - GFG",
        "title": "Bit Difference",
        "difficulty": "Easy",
        "topic": "Bit Manipulation",
        "pattern": "Brian Kernighan's Algorithm on (a ^ b)",
        "lc_number": 461,
        "lc_title": "Hamming Distance",
        "lc_url": "https://leetcode.com/problems/hamming-distance/",
        "recall": "How do you count the number of bits that need to be flipped to convert integer a to integer b?",
        "concept": "XOR a and b to get diff = a ^ b. Every set bit in diff corresponds to a bit position that must be flipped. Count set bits in diff using Brian Kernighan's algorithm: while diff > 0: diff &= (diff - 1), count++.",
        "hints": [
            "XOR returns 1 wherever bits differ.",
            "Counting the number of flips equals counting set bits in a ^ b (the Hamming distance)."
        ],
        "trick": "Brian Kernighan's trick diff &= (diff - 1) clears the lowest set bit in each iteration, running in O(number of set bits) rather than 32 steps.",
        "complexity": "Time: O(K) where K is the number of flipped bits (at most 32). Space: O(1).",
        "edge_cases": [
            "a == b: 0 bits to flip.",
            "a and b have no bits in common: all bits flip."
        ]
    },
    {
        "folder": "5. Digits In Factorial - GFG",
        "title": "Digits in Factorial",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Logarithmic Summation (Kamenetsky's Formula)",
        "lc_number": None,
        "lc_title": "Number of Digits in Factorial",
        "lc_url": "https://leetcode.com/problems/calculate-money-in-leetcode-bank/",
        "recall": "How do you find the number of digits in n! for large n without actually computing the massive factorial?",
        "concept": "The number of digits in an integer X in base 10 is floor(log10(X)) + 1. Since n! = 1 * 2 * ... * n, log10(n!) = sum(log10(i)) for i = 1 to n. Compute sum of log10(i) and return floor(sum) + 1.",
        "hints": [
            "Number of digits in X is floor(log10(X)) + 1.",
            "Use the log product identity: log(a * b) = log(a) + log(b)."
        ],
        "trick": "Summing log10(i) for i from 1 to n avoids computing gigantic factorials while giving exact digit counts.",
        "complexity": "Time: O(N) simple floating-point loop. Space: O(1).",
        "edge_cases": [
            "n <= 1: 0! and 1! both equal 1, which has 1 digit.",
            "Floating point precision: use double."
        ]
    },
    {
        "folder": "5. Max and Second Max - GFG",
        "title": "Max and Second Max",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Single Pass Two-Variable Tracking",
        "lc_number": None,
        "lc_title": "Second Largest Element",
        "lc_url": "https://leetcode.com/problems/third-maximum-number/",
        "recall": "How do you find the largest and second distinct largest elements in an array in a single pass?",
        "concept": "Initialize max = -1, secondMax = -1. For each x in array: if x > max: secondMax = max, max = x. Else if x < max and x > secondMax: secondMax = x. Return [max, secondMax].",
        "hints": [
            "Track both maximum and strictly smaller second maximum in one loop.",
            "When a new maximum is found, what happens to the old maximum? It becomes secondMax."
        ],
        "trick": "Only update secondMax when x < max to ensure the second maximum is STRICTLY distinct from the maximum.",
        "complexity": "Time: O(N) single pass. Space: O(1) auxiliary space.",
        "edge_cases": [
            "All elements identical: [5, 5, 5] -> max = 5, secondMax = -1.",
            "Array with two elements.",
            "Negative numbers."
        ]
    },
    {
        "folder": "6. GP Term - GFG",
        "title": "GP Term",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Geometric Progression Formula (a * r^(n-1))",
        "lc_number": None,
        "lc_title": "Geometric Progression Term",
        "lc_url": "https://leetcode.com/problems/powx-n/",
        "recall": "Given first term A and second term B of a geometric progression, how do you find the N-th term?",
        "concept": "The common ratio is r = B / A. The N-th term of a GP is given by term_N = A * r^(N - 1) = A * (B / A)^(N - 1).",
        "hints": [
            "Common ratio r = B / A.",
            "N-th term formula: T_n = A * r^(n-1)."
        ],
        "trick": "Use pow(B / A, N - 1) with double precision floating-point arithmetic.",
        "complexity": "Time: O(log N) for power computation. Space: O(1).",
        "edge_cases": [
            "N = 1: returns A.",
            "N = 2: returns B.",
            "Ratio < 1: decaying GP."
        ]
    },
    {
        "folder": "6. Number is sparse or not - GFG",
        "title": "Number Is Sparse or Not",
        "difficulty": "Easy",
        "topic": "Bit Manipulation",
        "pattern": "Adjacent Bit Check (n & (n >> 1))",
        "lc_number": None,
        "lc_title": "Sparse Number Check",
        "lc_url": "https://leetcode.com/problems/number-of-1-bits/",
        "recall": "A number is sparse if there are no two consecutive set bits in its binary representation. How do you check this in O(1) time?",
        "concept": "If a number has two consecutive set bits, shifting it right by 1 position will align one of those set bits with the other. Therefore, (n & (n >> 1)) == 0 if and only if no two consecutive bits are both 1.",
        "hints": [
            "What happens when you bitwise AND a number with its right-shifted self?",
            "If any two adjacent bits were 1, (n & (n >> 1)) will have a non-zero bit at that position."
        ],
        "trick": "Single expression (n & (n >> 1)) == 0 checks all adjacent bits in parallel across the entire word in 1 CPU cycle.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "n = 0: sparse (no set bits).",
            "Powers of 4 or alternating bits (e.g. 101010b = 42) -> sparse.",
            "Numbers like 3 (11b), 6 (110b) -> not sparse."
        ]
    },
    {
        "folder": "6. Strongest Neighbour - GFG",
        "title": "Strongest Neighbour",
        "difficulty": "Easy",
        "topic": "Arrays & Hashing",
        "pattern": "Adjacent Pair Sliding Maximum",
        "lc_number": None,
        "lc_title": "Adjacent Pair Maxima",
        "lc_url": "https://leetcode.com/problems/sliding-window-maximum/",
        "recall": "For each adjacent pair of elements in an array, how do you find and print the maximum of the pair?",
        "concept": "Loop i from 0 to n - 2: print max(arr[i], arr[i + 1]). This creates an array of size n - 1 where each element is the maximum of the window of size 2.",
        "hints": [
            "Slide a window of size 2 across the array.",
            "At each step i, output max(arr[i], arr[i + 1])."
        ],
        "trick": "Loop bounds stop at n - 2 to prevent an index out of bounds on arr[i + 1].",
        "complexity": "Time: O(N) single pass. Space: O(1) auxiliary space.",
        "edge_cases": [
            "Array with exactly 2 elements.",
            "Array with negative numbers: max() preserves sign correctly."
        ]
    },
    {
        "folder": "7. Primality Test - GFG",
        "title": "Primality Test",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "6k ± 1 Trial Division up to sqrt(N)",
        "lc_number": None,
        "lc_title": "Prime Number Test",
        "lc_url": "https://leetcode.com/problems/count-primes/",
        "recall": "How do you test if an integer N is prime in O(sqrt(N)) time using the 6k ± 1 optimization?",
        "concept": "If N <= 1, return false. If N <= 3, return true. If N % 2 == 0 or N % 3 == 0, return false. All primes greater than 3 are of the form 6k ± 1. Loop i from 5 to sqrt(N) stepping by 6: if N % i == 0 or N % (i + 2) == 0, return false. If loop finishes, return true.",
        "hints": [
            "Divisors always appear in pairs (d, N / d); checking up to sqrt(N) is sufficient.",
            "After ruling out multiples of 2 and 3, all remaining prime candidates are of the form 6k ± 1."
        ],
        "trick": "Stepping by 6 checks both i (6k - 1) and i + 2 (6k + 1) in each iteration, skipping 2/3 of all numbers.",
        "complexity": "Time: O(sqrt(N)). Space: O(1).",
        "edge_cases": [
            "N <= 1: not prime.",
            "N = 2, 3: prime.",
            "Perfect squares of primes (e.g. 25, 49): caught at i = sqrt(N)."
        ]
    },
    {
        "folder": "7. Reverse array in groups - GFG",
        "title": "Reverse Array in Groups",
        "difficulty": "Easy",
        "topic": "Two Pointers",
        "pattern": "Block-wise Two Pointers Reversal",
        "lc_number": 189,
        "lc_title": "Rotate Array",
        "lc_url": "https://leetcode.com/problems/rotate-array/",
        "recall": "Given an array and integer k, how do you reverse every contiguous sub-array of size k in-place?",
        "concept": "Iterate i from 0 to n in steps of k. For each block, define left = i and right = min(i + k - 1, n - 1). Reverse the sub-array arr[left..right] in-place using two pointers: while left < right: swap(arr[left], arr[right]), left++, right--.",
        "hints": [
            "Process the array in chunks of size k.",
            "Use min(i + k - 1, n - 1) as the right boundary to handle the final partial chunk."
        ],
        "trick": "The right boundary of the last group must be clamped to min(i + k - 1, n - 1) so trailing elements are reversed safely without index errors.",
        "complexity": "Time: O(N) every element swapped at most once. Space: O(1) in-place.",
        "edge_cases": [
            "k >= n: reverses the entire array.",
            "k == 1: array remains unchanged.",
            "n is not a multiple of k: last chunk of size n % k is reversed correctly."
        ]
    },
    {
        "folder": "8. Exactly 3 Divisors - GFG",
        "title": "Exactly 3 Divisors",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Primes Squared via Sieve / Trial Division",
        "lc_number": None,
        "lc_title": "Three Divisors",
        "lc_url": "https://leetcode.com/problems/three-divisors/",
        "recall": "Which numbers have EXACTLY 3 positive divisors, and how do you count how many exist up to N?",
        "concept": "A number has exactly 3 divisors if and only if it is the square of a prime number p (its divisors are 1, p, and p^2). To count such numbers <= N, count all prime numbers p such that p^2 <= N (i.e. p <= sqrt(N)). Use a Sieve of Eratosthenes up to sqrt(N) and count primes.",
        "hints": [
            "If a number has divisors 1, d, and n, what must d be? d must be prime and d * d = n!",
            "Count prime numbers up to floor(sqrt(N))."
        ],
        "trick": "Only squares of prime numbers have exactly 3 divisors. Counting them up to N reduces to counting primes up to sqrt(N).",
        "complexity": "Time: O(sqrt(N) log log(sqrt(N))) using Sieve. Space: O(sqrt(N)) for sieve array.",
        "edge_cases": [
            "N < 4: return 0 (smallest is 2^2 = 4).",
            "N = 4: return 1 (4 has divisors 1, 2, 4)."
        ]
    },
    {
        "folder": "9. Addition Under Modulo - GFG",
        "title": "Addition Under Modulo",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Modular Arithmetic Addition Identity",
        "lc_number": None,
        "lc_title": "Modular Arithmetic Operations",
        "lc_url": "https://leetcode.com/problems/super-pow/",
        "recall": "How do you calculate (a + b) % M preventing 64-bit integer overflow?",
        "concept": "Modular addition rule: (a + b) % M = ((a % M) + (b % M)) % M. Taking modulo before adding prevents large operands from overflowing the integer limit.",
        "hints": [
            "Take modulo of individual terms first.",
            "((a % M) + (b % M)) % M prevents overflow."
        ],
        "trick": "In languages with fixed integer sizes, reduce both operands modulo M first to keep their sum within the representation limits.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "a + b exceeding 32-bit integer range.",
            "M = 10^9 + 7 (standard competitive programming modulo)."
        ]
    },
    {
        "folder": "10. Multiplication Under Modulo - GFG",
        "title": "Multiplication Under Modulo",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Modular Arithmetic Multiplication Identity",
        "lc_number": None,
        "lc_title": "Modular Multiplication",
        "lc_url": "https://leetcode.com/problems/powx-n/",
        "recall": "How do you calculate (a * b) % M safely without integer overflow?",
        "concept": "Modular multiplication rule: (a * b) % M = ((a % M) * (b % M)) % M. Cast operands to 64-bit integers (long / unsigned long long) before multiplying to avoid 32-bit overflow before modulo.",
        "hints": [
            "Take modulo of each operand first.",
            "Cast operands to 64-bit long before the multiplication."
        ],
        "trick": "Even after modulo M, (a % M) * (b % M) can be up to (M-1)^2. If M = 10^9 + 7, (M-1)^2 ~= 10^18, requiring a 64-bit long in C++/Java.",
        "complexity": "Time: O(1). Space: O(1).",
        "edge_cases": [
            "Large a and b near 10^9.",
            "Operand divisible by M -> result 0."
        ]
    },
    {
        "folder": "11. Modular Multiplicative Inverse - GFG",
        "title": "Modular Multiplicative Inverse",
        "difficulty": "Easy",
        "topic": "Math & Number Theory",
        "pattern": "Extended Euclidean Algorithm (Bézout Identity)",
        "lc_number": None,
        "lc_title": "Modular Multiplicative Inverse",
        "lc_url": "https://leetcode.com/problems/super-pow/",
        "recall": "Given integers a and m, how do you find an integer x in [1, m - 1] such that (a * x) % m == 1?",
        "concept": "A modular inverse exists if and only if gcd(a, m) == 1. Use the Extended Euclidean Algorithm to find coefficients x and y such that a*x + m*y = gcd(a, m) = 1. Taking modulo m: (a * x) % m = 1. The result is (x % m + m) % m. If gcd != 1, return -1.",
        "hints": [
            "Does a modular inverse exist if gcd(a, m) != 1? No, return -1.",
            "Extended Euclidean algorithm finds integers x and y satisfying a*x + m*y = 1."
        ],
        "trick": "The coefficient x returned by Extended GCD may be negative. Normalize it into [1, m - 1] via (x % m + m) % m.",
        "complexity": "Time: O(log(min(a, m))) Euclidean steps. Space: O(1).",
        "edge_cases": [
            "gcd(a, m) > 1: inverse does not exist -> return -1.",
            "m = 1: no valid inverse in [1, m - 1].",
            "a = 1: inverse is 1."
        ]
    }
]
print("GFG problems loaded:", len(GFG_PROBLEMS))
