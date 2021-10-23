class Solution:
    # O(n) time: one pass through list
    # O(1) space
    # but really simple and fast because included function
    def findMinLin(self, nums: list) -> int:
        return min(nums)


    # O(log(n)) time: binary search
    # O(n) time worst case: lots of duplicates
    # O(1) space
    def findMin(self, nums: list) -> int:
        lo, hi = 0, len(nums) - 1
        if nums[lo] < nums[hi]: return nums[lo]

        while lo < hi:
            mid = (lo + hi) // 2
            l, h, m = nums[lo], nums[hi], nums[mid]

            # minimum in right half
            if m > h: lo = mid + 1
            # minimum in left half
            elif m < h: hi = mid
            # linear pass through duplicates
            else: hi -= 1

        return nums[lo]


testcases = [
    ([4,5,6,7,0,1,4], 0),
    ([0,1,4,4,5,6,7], 0),
    ([1,3,5], 1),
    ([2,2,2,0,1], 0)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().findMin(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')