class Solution:
    # O(n) time complexity: maximum two passes over each entry
    # O(1) space complexity: only use three additional variables
    def longestOnes(self, nums: list, k: int) -> int:
        n = len(nums)
        maxLength, currStart, currK = 0, 0, 0

        for currEnd in range(n):
            if nums[currEnd] == 1: maxLength = max(maxLength, currEnd - currStart + 1)
            elif currK < k:
                currK += 1
                maxLength = max(maxLength, currEnd - currStart + 1)
            else:
                currK += 1
                while currK > k:
                    if nums[currStart] == 0: currK -= 1
                    currStart += 1

        return maxLength



testcases = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10)
]

for i, (input, k, target) in enumerate(testcases):
    output = Solution().longestOnes(input, k)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')