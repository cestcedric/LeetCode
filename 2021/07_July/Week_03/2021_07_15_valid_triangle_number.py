class Solution:
    # O(n^2) time complexity: k is only reset for each i
    # j and k pass over the rest of nums twice, so linear time complexity
    # O(1) space complexity: depending on implementation of sort()
    def triangleNumber(self, nums: list) -> int:
        n = len(nums)
        nums.sort()
        combinationCount = 0

        for i in range(n - 2):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[k] < nums[i] + nums[j]: k += 1
                combinationCount += k - j - 1

        return combinationCount


testcases = [
    ([2,2,3,4], 3),
    ([4,2,3,4], 4),
    ([0,1,0,1], 0)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().triangleNumber(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
