from collections import deque

# O(n) time complexity: every index put into deque once, and removed once
# Later iterations already work on pre-filtered deque, so not quadratic or sth similar
# O(n + k) space complexity: 'jumps' of length n and deque of length k
# Can be reduced by using nums to store intermediate values, then O(k)
class Solution:
    def maxResult(self, nums: list, k: int) -> int:
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2: return nums[0] + nums[1]
        jumps = [ 0 for _ in nums ]
        jumps[0] = nums[0]
        jumps[1] = nums[0] + nums[1]
        queue = deque([1]) if jumps[1] > jumps[0] else deque([0,1])

        for i in range(2, length):
            # remove old entries to far back
            while queue and queue[0] < i-k: queue.popleft()
            # jump to current field with largest value
            jumps[i] = nums[i] + jumps[queue[0]]
            # remove entries smaller than current value
            while queue and jumps[i] >= jumps[queue[-1]]: queue.pop()
            queue.append(i)
        return jumps[-1]

testcases = [
    ([1,-1,-2,4,-7,3], 2, 7),
    ([10,-5,-2,4,0,3], 3, 17),
    ([1,-5,-20,4,-1,3,-6,-3], 2, 0)
]

for i, (input, k, target) in enumerate(testcases):
    output = Solution().maxResult(input, k)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed')