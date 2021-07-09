from bisect import bisect_left

class Solution:
    # O(n^2) time complexity: look up all previous entries for every entry
    # O(n) space complexity: additional dp array of size n
    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            dp[i] += max([0] + [dp[j] for j in range(i, -1, -1) if nums[j] < nums[i]])

        return max(dp)


    # O(n * log(n)) time complexity: one pass through nums, binary search in sorted seq
    # O(n) space complexity: seq with at most n elements
    def lengthOfLIS2(self, nums: list) -> int:
        seq, s = [], 0

        for n in nums:
            index = bisect_left(seq, n)
            if index == s: 
                seq.append(n)
                s += 1
            elif seq[index] > n:
                seq[index] = n
            elif seq[index] < n:
                seq[index + 1] = n

        return s

testcasses = [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),
    ([1,3,6,7,9,4,10,5,6], 6),
    ([1,2,3,4,0,3], 4)
]

for i, (input, target) in enumerate(testcasses):
    output = Solution().lengthOfLIS2(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')