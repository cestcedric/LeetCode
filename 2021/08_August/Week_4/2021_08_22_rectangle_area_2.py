class Solution:
    def rectangleArea(self, rectangles: list) -> int:
        MOD = 10**9 + 7


testcases = [
    ([[0,0,2,2],[1,0,2,3],[1,0,3,1]], 6),
    ([[0,0,1000000000,1000000000]], 49)
]

for i, (rectangles, target) in enumerate(testcases):
    output = Solution().rectangleArea(rectangles)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')