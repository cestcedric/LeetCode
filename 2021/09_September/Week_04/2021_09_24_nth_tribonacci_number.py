class Solution:
    # O(n) time
    # O(1) space
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1

        if n == 0: return t0
        if n == 1: return t1
        if n == 2: return t2

        while n > 2:
            n -= 1
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2


testcases = [
    (4, 4),
    (25, 1389537)
]

for i, (n, target) in enumerate(testcases):
    output = Solution().tribonacci(n)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')