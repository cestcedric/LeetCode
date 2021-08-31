class Solution:
    # O(log(n)) time: binary search
    # O(1) space
    def findMin(self, nums: list) -> int:
        left, right = 0, len(nums) - 1

        while nums[left] > nums[right]:
            mid = (left + right) // 2
            
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


testcases = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().findMin(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')