class Solution:
    # O(log(n)) time: n = max(left, right)
    # O(1) space
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        k = 0
        while left != right and left > 0 and right > 0:
            left = left >> 1
            right = right >> 1
            k += 1
        return left << k


    # O(log(n)) time
    # O(log(n)) space
    def rangeBitwiseAndRec(self, left: int, right: int) -> int:
        if left == right: return left
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1


testcases = [
    (5, 7, 4),
    (0, 0, 0),
    (1, 2147483647, 0)
]

for i, (left, right, target) in enumerate(testcases):
    output = Solution().rangeBitwiseAnd(left, right)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')