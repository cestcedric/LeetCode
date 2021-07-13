class Solution:
    # O(log(n)) time complexity: basically binary search
    # O(1) space complexity
    def findPeakElement(self, nums: list) -> int:
        left, right = 0, len(nums) - 1

        if right == 0: return 0
        if nums[0] > nums[1]: return 0
        if nums[right] > nums[right - 1]: return right

        while left < right - 2:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]: left = mid
            else: right = mid + 1

        return right - 1

testcases = [
    ([1,2,3,1], 2),
    ([1,2,1,3,5,6,4], 5),
    ([1,2,3,4,5], 4),
    ([3,2,1], 0),
    ([1], 0)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().findPeakElement(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')