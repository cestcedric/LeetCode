class Solution:
    # O(n) time: worst case: nums = [1] * n
    # O(1) space
    def minPatches(self, nums: list, n: int) -> int:
        reach, patches, idx = 0, 0, 0

        while reach < n:
            if idx >= len(nums) or nums[idx] > reach + 1:
                patches += 1
                reach = 2 * reach + 1
            else:
                reach += nums[idx]
                idx += 1

        return patches


testcases = [
    ([1,3], 6, 1),
    ([1,5,10], 20, 2),
    ([1,2,2], 5, 0)
]

for i, (nums, n, target) in enumerate(testcases):
    output = Solution().minPatches(nums, n)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')