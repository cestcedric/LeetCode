class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        sorted_h = [0] + horizontalCuts + [h]
        sorted_v = [0] + verticalCuts + [w]

        max_h = 0
        for x, y in zip(sorted_h[:-1], sorted_h[1:]):
            max_h = max(max_h, y-x)

        max_v = 0
        for x, y in zip(sorted_v[:-1], sorted_v[1:]):
            max_v = max(max_v, y-x)

        return (max_v * max_h) % (10**9 + 7)

testcases = [
    (5, 4, [1,2,4], [1,3], 4),
    (5, 4, [3,1], [1], 6),
    (5, 4, [3], [3], 9)
]

for i, (h, w, hcuts, vcuts, target) in enumerate(testcases):
    output = Solution().maxArea(h, w, hcuts, vcuts)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')