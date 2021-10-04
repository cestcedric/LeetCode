class Solution:
    # O(n) time: one pass through nums
    # O(1) space: only one additional variable allocated
    def canJump(self, nums: list) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if i > reachable: return False

            reachable = max(reachable, i + nums[i])
            if reachable >= len(nums) - 1: return True

        return False




testcases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([0], True)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().canJump(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')