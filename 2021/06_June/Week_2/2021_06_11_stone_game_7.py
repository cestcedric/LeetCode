class Solution:
    # O(n^2) time complexity: compute half of the entries in an n x n grid
    # O(n^2) space complexity: as mentioned above, n x n grid
    def stoneGameVII(self, stones: list) -> int:
        n = len(stones)
        scores = [ [ 0 for _ in range(n) ] for _ in range(n) ]

        # reverse problem: start with no stones and add the greater value one
        for i in range(n-2, -1, -1):
            total = stones[i]
            for j in range(i+1, n):
                total += stones[j]
                scores[i][j] = max(
                    total - stones[i] - scores[i+1][j], 
                    total - stones[j] - scores[i][j-1])
        return scores[0][n-1]


    # O(n^2) time complexity: still using same technique to solve
    # O(n) space complexity: only need current and previous line, not whole grid
    def effStoneGameVII(self, stones: list) -> int:
        n = len(stones)
        scores_curr = [ 0 ] * n
        scores_prev = [ 0 ] * n

        for i in range(n-2, -1, -1):
            total = stones[i]
            scores_curr, scores_prev = scores_prev, scores_curr
            for j in range(i+1, n):
                total += stones[j]
                scores_curr[j] = max(
                    total - stones[i] - scores_prev[j], 
                    total - stones[j] - scores_curr[j-1])
        return scores_curr[n-1]



testcases = [
    ([5,3,1,4,2], 6),
    ([7,90,5,1,100,10,10,2], 122)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().effStoneGameVII(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')