class Solution:
    # O(n) time complexity, every index looked at at most twice, dict lookup in O(1)
    # O(n) space complexity, dictionary of at most same length as nums
    def maximumUniqueSubarray(self, nums: list) -> int:
        included = {}
        maxScore = 0
        total = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] in included:
                # delete all entries up to and including the last occurrence
                while left <= included[nums[right]]:
                    total -= nums[left]
                    left += 1
            total += nums[right]
            included[nums[right]] = right
            maxScore = max(maxScore, total)
        return maxScore


testcases = [
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().maximumUniqueSubarray(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')
        