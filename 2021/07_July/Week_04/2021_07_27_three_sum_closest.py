class Solution:
    # O(n^2) time complexity: sorting in O(n*log(n)), traversing in O(n^2)
    # O(1) space complexity: depending on sorting algorithm, might be up to O(n*log(n))
    def threeSumClosest(self, nums: list, target: int) -> int:
        n = len(nums)
        nums.sort()
        nearest = 10**5

        for i in range(n - 2):
            a = nums[i]
            j, k = i + 1, n - 1
            while j < k:
                b, c = nums[j], nums[k]
                candidate = a + b + c
                if candidate == target: return candidate
                if candidate < target: j += 1
                elif candidate > target: k -= 1

                if abs(target - candidate) < abs(target - nearest):
                    nearest = candidate
                
        return nearest


testcases = [
    ([-1,2,1,-4], 1, 2)
]
        


for i, (nums, target, expectedOuput) in enumerate(testcases):
    output = Solution().threeSumClosest(nums, target)
    print('Case #{}: should be {}, is {}'.format(i + 1, expectedOuput, output))
    assert expectedOuput == output
print('All test cases passed!')