class Solution:
    # O(4^n) time complexity: for each matchstick there are 4 possible buckets
    # O(n) space complexity: call stack of max depth n
    def makesquare(self, matchsticks: list) -> bool:
        if matchsticks == []: return False
        numMatchsticks = len(matchsticks)
        totalLength = sum(matchsticks)
        maxLength = max(matchsticks)
        
        if totalLength % 4 != 0 or maxLength > totalLength // 4:
            return False

        matchsticks.sort(reverse = True)
        sideLength = totalLength // 4
        sides = [0, 0, 0, 0]

        def dfs(index):
            nonlocal matchsticks
            nonlocal numMatchsticks
            nonlocal sides
            nonlocal sideLength

            if index == numMatchsticks:
                return sides[0] == sides[1] == sides[2] == sideLength

            # try to put match in all four sides + backtracking
            for s in range(4):
                if sides[s] + matchsticks[index] <= sideLength:
                    sides[s] += matchsticks[index]
                    if dfs(index + 1): return True
                    sides[s] -= matchsticks[index]
            return False
        
        return dfs(0)


testcases = [
    ([1,1,2,2,2], True),
    ([3,3,3,3,4], False)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().makesquare(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')