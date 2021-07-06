from collections import defaultdict
import heapq

class Solution:
    # O(n * log(n)) time complexity: 
    # -> push and pop of one element on heap in O(log(n))
    # -> one pass through arr, one through dict
    # O(n) space complexity: dict and heap with at most n entries each
    def minSetSize(self, arr: list) -> int:
        n = len(arr)
        occurrenceDict = defaultdict(int)
        occurrenceHeap = []

        for a in arr:
            occurrenceDict[a] += 1

        for d in occurrenceDict:
            heapq.heappush(occurrenceHeap, (-occurrenceDict[d], d))

        count = n / 2
        setSize = 0
        while count > 0:
            addToSet = heapq.heappop(occurrenceHeap)
            count += addToSet[0]
            setSize += 1

        return setSize

        



testcases = [
    ([3,3,3,3,5,5,5,2,2,7], 2),
    ([7,7,7,7,7,7], 1),
    ([1,9], 1),
    ([1000,1000,3,7], 1),
    ([1,2,3,4,5,6,7,8,9,10], 5)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().minSetSize(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')