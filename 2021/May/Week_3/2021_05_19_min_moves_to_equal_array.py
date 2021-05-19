from statistics import median

class Solution:
    def minMoves2(self, nums: list) -> int:
        m = int(median(nums))
        moves = 0
        for n in nums:
            moves += abs(n - m)
        return moves

testcases = [
    ([1,2,3], 2),
    ([1,10,2,9], 16),
    ([1,1,1,1], 0),
    ([1,2,3,4], 4)
]

for i, (nums, moves) in enumerate(testcases):
    result = Solution().minMoves2(nums)
    print('Case #{} should be {}, is {}'.format(i+1, moves, result))
    assert result == moves
print('All test cases passed!')
        