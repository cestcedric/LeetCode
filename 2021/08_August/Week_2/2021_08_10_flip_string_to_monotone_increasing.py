from itertools import accumulate

class Solution:
    # O(n) time: create cumSum and iterate through possible solutions
    # O(n) space: cumSum list
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        cumSum = [0] + list(accumulate(map(int, s)))

        # possible solutions:
        # 00000, 00001, 00011, 00111, 01111, 11111
        minFlips = n
        for i in range(n + 1):
            changesFront = cumSum[n - i]
            changesBack = i - (cumSum[n] - cumSum[n - i - 1])
            minFlips = min(minFlips, changesFront + changesBack)

        return minFlips


testcases = [
    ('00110', 1),
    ('010110', 2),
    ('00011000', 2),
    ('11011', 1)
]


for i, (s, target) in enumerate(testcases):
    output = Solution().minFlipsMonoIncr(s)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('Aöö test cases passed!')