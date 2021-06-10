class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # O(n*m) time complexity
        # O(n*m) space complexity, obviously entries for all combinations
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2: return False

        grid = [ [ None for _ in range(l2+1) ] for _ in range(l1+1) ]

        for x in range(l1+1):
            for y in range(l2+1):
                if x == y == 0: grid[x][y] = True
                elif x == 0: grid[x][y] = s3[y-1] == s2[y-1] and grid[x][y-1]
                elif y == 0: grid[x][y] = s3[x-1] == s1[x-1] and grid[x-1][y]
                else: grid[x][y] = (grid[x-1][y] and s3[x+y-1] == s1[x-1]) or (grid[x][y-1] and s3[x+y-1] == s2[y-1])

        return grid[l1][l2]


    def isInterleaveEff(self, s1: str, s2: str, s3: str) -> bool:
        # O(n*m) time complexity, still need to look at all combinations
        # O(m) space complexity, just need one line of the grid actually
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2: return False

        grid = [ None for _ in range(l2+1)]

        for x in range(l1+1):
            for y in range(l2+1):
                if x == y == 0: grid[y] = True
                elif x == 0: grid[y] = s3[y-1] == s2[y-1] and grid[y-1]
                elif y == 0: grid[y] = s3[x-1] == s1[x-1] and grid[y]
                else: grid[y] = (grid[y] and s3[x+y-1] == s1[x-1]) or (grid[y-1] and s3[x+y-1] == s2[y-1])
        
        return grid[-1]


        


testcases = [
    (("aabcc", "dbbca", "aadbbcbcac"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (('', '', ''), True),
    (('', '', 'a'), False)
]

for i, ((s1, s2, s3), target) in enumerate(testcases):
    output1 = Solution().isInterleave(s1, s2, s3)
    output2 = Solution().isInterleaveEff(s1, s2, s3)
    print('Case #{} solved: {}'.format(i+1, output1 == output2 == target))
    assert target == output1 == output2, '\nSimple DP working: {}\nEfficient DP working: {}'.format(output1 == target, output2 == target)
print('All test cases solved!')