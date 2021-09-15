class Solution:
    # O(n) time
    # O(n) space
    def maxTurbulenceSizeDP(self, arr: list) -> int:
        n = len(arr)
        if n < 2: return n

        def diffSign(x, y):
            if x == y: return 0
            if x < y: return -1
            return 1

        dp = [1] * n

        sign = None
        for i in range(1, n):
            s = diffSign(arr[i - 1], arr[i])
            if s == 0: continue
            if s == sign: dp[i] = 2
            else: dp[i] = dp[i - 1] + 1
            sign = s

        return max(dp)


    # O(n) time
    # O(1) space
    def maxTurbulenceSize(self, arr: list) -> int:
        n = len(arr)
        if n < 2: return n

        def diffSign(x, y):
            if x == y: return 0
            if x < y: return -1
            return 1

        maxSubarray = 0
        start = 0

        sign = None
        for i in range(1, n):
            s = diffSign(arr[i - 1], arr[i])
            if s == 0: start = i
            elif s == sign: start = i - 1
            maxSubarray = max(maxSubarray, i - start + 1)
            sign = s

        return maxSubarray





testcases = [
    ([2,0,2,4,2,5,0,1,2,3], 6),
    ([9,4,2,10,7,8,8,1,9], 5),
    ([4,8,12,16], 2),
    ([100], 1)
]

for i, (arr, target) in enumerate(testcases):
    output = Solution().maxTurbulenceSize(arr)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')