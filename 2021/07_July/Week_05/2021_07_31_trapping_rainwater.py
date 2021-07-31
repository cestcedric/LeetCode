class Solution:
    # O(n) time complexity: three passes through array
    # O(n) space complexity: fillHeight for every field
    def trap(self, height: list) -> int:
        n = len(height)
        fillHeight = height.copy()

        # leftmost and rightmost field cannot be filled
        # out of scope fields are 0, not infinite height

        # pass from left to right
        maxHeight = 0
        for i in range(n - 1):
            maxHeight = max(maxHeight, height[i])
            fillHeight[i] = maxHeight

        maxHeight = 0
        for i in range(n - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            fillHeight[i] = min(fillHeight[i], maxHeight)

        trappedWater = 0
        for i in range(n):
            trappedWater += fillHeight[i] - height[i]

        return trappedWater


testcases = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9)
]

for i, (height, target) in enumerate(testcases):
    output = Solution().trap(height)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')