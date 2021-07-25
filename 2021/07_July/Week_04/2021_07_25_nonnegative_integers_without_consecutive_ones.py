from functools import lru_cache

class Solution:

    # O(log(n)) time complexity
    # O(log(n)) space complexity: call stack depth
    # TLE
    def findIntegersRec(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n, limit):
            print(n)
            if n > limit: return 0
            if n & 1: return 1 + helper(n << 1, limit)
            return 1 + helper(n << 1, limit)  + helper((n << 1) + 1, limit)

        return 1 + helper(1, n)

    
    # O(1) time: compute 30 entries, then 30 iterations to sum up possibilities
    # O(1) space: array with 30 entries
    def findIntegers(self, n: int) -> int:
        # only need 30 entries as 2^30 > 10^9
        fib = [0] * 30
        fib[0], fib[1] = 1, 2
        for i in range(2, 30):
            fib[i] = fib[i - 1] + fib[i - 2]
        
        count, oneInLastIndex = 0, False
        for i in range(30, -1, -1):
            if (1 << i) & n:
                count += fib[i]
                if oneInLastIndex: return count
                oneInLastIndex = True
            else:
                oneInLastIndex = False
        return count + 1


testcases = [
    (21, 13),
    (10, 8),
    (5, 5),
    (1, 2),
    (2, 3)
]

for i, (n, target) in enumerate(testcases):
    output = Solution().findIntegers(n)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')