from functools import lru_cache

class Solution:
    # O(n) time complexity: compute cost for each stair
    # O(n) space complexity: additional array containing all stairs
    def minCostClimbingStairsFullDP(self, cost: list) -> int:
        length = len(cost)
        stairs = [ None for _ in range(length+1) ]
        stairs[0], stairs[1] = 0, 0
        for i in range(2, length+1):
            stairs[i] = min(stairs[i-1] + cost[i-1], stairs[i-2] + cost[i-2])
        return stairs[-1]


    # O(n) time complexity: compute cost for each stair
    # O(1) space complexity: only save the cost for the two previous stairs
    def minCostClimbingStairsEfficientDP(self, cost: list) -> int:
        length = len(cost)
        stairs1, stairs2 = 0, 0
        for i in range(2, length+1):
            stairs = min(stairs1 + cost[i-1], stairs2 + cost[i-2])
            stairs2, stairs1 = stairs1, stairs
        return stairs


    # O(n) time complexity: caching intermediate results to avoid quadratic complexity
    # O(n) space complexity: cache and recursive call stack, each in O(n)
    def minCostClimbingStairs(self, cost: list) -> int:
        @lru_cache()
        def climb(stair):
            if stair < 2: return 0
            return min(climb(stair-1) + cost[stair-1], climb(stair-2) + cost[stair-2])
        return climb(len(cost))



testcases = [
    ([10,15,20], 15),
    ([1,100,1,1,1,100,1,1,100,1], 6),
    ([0,2,2,1], 2),
    ([0,2,3,2], 3)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().minCostClimbingStairs(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')

        