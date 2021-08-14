class Solution:
    def removeBoxes(self, boxes: list) -> int:
        # TODO:
        pass


testcases = [
    ([1,3,2,2,2,3,4,3,1], 23),
    ([1,1,1], 9),
    ([1], 1)
]

for i, (boxes, target) in enumerate(testcases):
    output = Solution().removeBoxes(boxes)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')