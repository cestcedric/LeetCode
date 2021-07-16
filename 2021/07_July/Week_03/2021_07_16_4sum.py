class Solution:
    # O(n^3) time complexity: two nested outer loops, one pass through rest of array
    # O(n^2) space complexity: sets to save already used combinations
    def fourSum(self, nums: list, target: int) -> list:
        output = []
        n = len(nums)
        nums.sort()

        ab_combinations = set()
        for i in range(n - 3):
            a = nums[i]
            for j in range(i + 1, n - 2):
                b = nums[j]
                if (a, b) in ab_combinations: continue
                ab_combinations.add((a, b))

                t = target - a - b
                left, right = j + 1, n - 1
                cd_combinations = set()
                while left < right:
                    c, d = nums[left], nums[right]
                    if c + d == t and (c, d) not in cd_combinations:
                        output.append([a, b, c, d])
                        cd_combinations.add((c, d))
                        left += 1
                        right -= 1
                    elif c + d < t: left += 1
                    else: right -= 1

        return output


        


testcases = [
    ([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
    ([2,2,2,2,2], 8, [[2,2,2,2]])
]

for i, (nums, target, expectedOutput) in enumerate(testcases):
    output = Solution().fourSum(nums, target)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, expectedOutput, output))
    assert sorted(expectedOutput) == sorted(output)
print('All test cases passed')