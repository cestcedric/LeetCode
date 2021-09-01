class Solution:
    # O(n) time: visited set to detect cycle and skip visited nodes
    # O(n) space: could be reduce to O(1) by e.g. negating visited entries in nums
    def arrayNesting(self, nums: list) -> int:
        n = len(nums)
        visited = set()
        maxCycle, currCycle = 0, 0

        for i in range(n):
            if i in visited: continue
            while i not in visited:
                visited.add(i)
                i = nums[i]
                currCycle += 1
            maxCycle = max(maxCycle, currCycle)
            currCycle = 0
            if maxCycle >= n / 2: return maxCycle

        return maxCycle


testcases = [
    ([5,4,0,3,1,6,2], 4),
    ([0,1,2], 1),
    ([0,2,1], 2)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().arrayNesting(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')