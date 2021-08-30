class Solution:
    # O(k) time: k = len(ops)
    # O(1) space
    def maxCount(self, m: int, n: int, ops: list) -> int:
        if ops == []: return m * n
        x = min(a for a, _ in ops)
        y = min(b for _, b in ops)

        # for a, b in ops:
        #     # all subareas start from 0,0 
        #     # => are always partially overlapping
        #     # => can only shrink candidate number
        #     x = min(x, a)
        #     y = min(y, b)

        return x * y
            


testcases = [
    (3, 3, [[2,2],[3,3]], 4),
    (3, 3, [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]], 4),
    (3, 3, [], 9)
]

for i, (m, n, ops, target) in enumerate(testcases):
    output = Solution().maxCount(m, n, ops)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')