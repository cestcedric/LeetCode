class Solution:
    def maxScore(self, cardPoints: list, k: int) -> int:
        total = sum(cardPoints)
        length = len(cardPoints)
        
        if length == k: return total

        cut = length - k
        excluded = sum(cardPoints[:cut])
        maxSum = total - excluded
        for i in range(0, length - cut):
            excluded = excluded - cardPoints[i] + cardPoints[i+cut]
            maxSum = max(maxSum, total - excluded)
        return maxSum




testcases = [
    ([1,2,3,4,5,6,1], 3, 12),
    ([2,2,2], 2, 4),
    ([9,7,7,9,7,7,9], 7, 55),
    ([1,1000,1], 1, 1),
    ([1,79,80,1,1,1,200,1], 3, 202),
    ([96,90,41,82,39,74,64,50,30], 8, 536)
]

for i, (cardPoints, k, s) in enumerate(testcases):
    result = Solution().maxScore(cardPoints, k)
    print('Case #{}: should be {}, is {}'.format(i+1, s, result))
    assert result == s
print('All testcases passed!')

        