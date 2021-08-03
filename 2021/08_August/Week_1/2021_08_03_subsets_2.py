class Solution:
    # O(2^n) time complexity: number of subsets at most 2^n
    # O(n) space complexity: tmp with at most n elements, subsets = output not counted
    def subsetsWithDup(self, nums: list) -> list:
        subsets = set()

        for i in range(2 ** len(nums)):
            tmp = []
            pattern = reversed(bin(i)[2:])
            for j, b in enumerate(pattern):
                if b == '1': tmp.append(nums[j])
            subsets.add(tuple(sorted(tmp)))

        return subsets


testcases = [
    ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
    ([0], [[],[0]])
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().subsetsWithDup(nums)
    print('Case #{} should be:\n{}, is\n{}'.format(i + 1, sorted(target), sorted(output)))
    assert sorted(target) == sorted(output)
print('All test cases passed!')
        