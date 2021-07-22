class Solution:
    # O(n) time complexity
    # O(n) space complexity: minFromRight and maxFromLeft
    def partitionDisjoint(self, nums: list) -> int:
        n = len(nums)
        minFromRight, maxFromLeft = [0] * n, [0] * n
        minFromRight[-1] = nums[-1]
        maxFromLeft[0] = nums[0]

        for i in range(n - 2, -1, -1):
            minFromRight[i] = min(nums[i], minFromRight[i + 1])

        for i in range(1, n):
            maxFromLeft[i] = max(nums[i], maxFromLeft[i - 1])

        for i in range(n - 1):
            if minFromRight[i + 1] >= maxFromLeft[i]: return i + 1


    # O(n) time complexity
    # O(1) space complexity
    def partitionDisjointConstantSpace(self, nums: list) -> int:
        maxValue, maxCandidate = nums[0], nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] >= maxCandidate:
                maxValue = max(maxValue, nums[i])
            else:
                length = i + 1
                maxCandidate = maxValue
        
        return length



testcases = [
    ([5,0,3,8,6], 3),
    ([1,1,1,0,6,12], 4),
    ([1,1], 1)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().partitionDisjointConstantSpace(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')