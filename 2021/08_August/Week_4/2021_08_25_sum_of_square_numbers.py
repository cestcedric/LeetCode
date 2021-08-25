import math

class Solution:
    # O(sqrt(c)) time: single pass through interval of length sqrt(c)
    # O(1) space
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            t = left ** 2 + right ** 2
            if t == c: return True
            if t < c: left += 1
            else: right -= 1

        return False


testcases = [
    (5, True),
    (4, True),
    (3, False),
    (2, True),
    (1, True)
]

for i, (c, target) in enumerate(testcases):
    output = Solution().judgeSquareSum(c)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')