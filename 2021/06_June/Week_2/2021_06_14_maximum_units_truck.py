class Solution:
    # O(n log(n)) time complexity due to sorting
    # O(n) space complexity, can be reduced to O(1) with in-place sorting
    def maximumUnits(self, boxTypes: list, truckSize: int) -> int:
        sortedBoxes = sorted(boxTypes, key = lambda box: box[1], reverse = True)
        total = 0
        for boxes in sortedBoxes:
            if boxes[0] < truckSize:
                total += boxes[0] * boxes[1]
                truckSize -= boxes[0]
            else:
                total += truckSize * boxes[1]
                break
            if truckSize == 0: break
        
        return total


    # O(n) time complexity: bucket sort working because maximum box content limited to 1000
    # O(k) space complexity: k = maximum box content
    # With these constraints slower than using native sort functions, 
    # since everything is done in Python
    def maximumUnitsBuckets(self, boxTypes: list, truckSize: int) -> int:
        sortedBoxes = [0] * 1000
        for boxes in boxTypes:
            # we want boxes with many units first, use this to "reverse sort"
            sortedBoxes[1000 - boxes[1]] += boxes[0]

        total = 0
        for i in range(1000):
            q = min(truckSize, sortedBoxes[i])
            total += (1000-i) * q
            truckSize -= q
            if truckSize == 0: break
        
        return total




testcases = [
    ([[1,3],[2,2],[3,1],[1,1000]], 4, 1007),
    ([[5,10],[2,5],[4,7],[3,9]], 10, 91)
]

for i, (input1, input2, target) in enumerate(testcases):
    output = Solution().maximumUnitsBuckets(input1, input2)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')