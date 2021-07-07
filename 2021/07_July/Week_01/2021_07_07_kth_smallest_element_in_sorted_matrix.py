import heapq

class Solution:
    # O(n * log(n) + k * log(n)) time complexity: 
    # O(n * log(n)) to init heap, O(k * log(n)) to got to k
    # O(n) space complexity: heap will always hold n values
    def kthSmallest(self, matrix: list, k: int) -> int:
        n = len(matrix)
        index = [0] * n
        heap = []

        # init heap
        for i in range(n):
            heapq.heappush(heap, (matrix[i][index[i]], i))

        # got to k
        for _ in range(k):
            value, i = heapq.heappop(heap)
            if index[i] == n - 1: continue

            index[i] += 1
            heapq.heappush(heap, (matrix[i][index[i]], i))

        return value




testcases = [
    ([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
    ([[-5]], 1, -5),
    ([[1,2],[1,3]], 2, 1)
]

for i, (matrix, k, target) in enumerate(testcases):
    output = Solution().kthSmallest(matrix, k)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')