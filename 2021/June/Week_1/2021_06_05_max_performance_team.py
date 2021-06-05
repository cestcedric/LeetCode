import heapq

class Solution:
    # O(n (log(n) + log(k))) time complexity: O(n log(n)) for sorting O(n log(k)) for heap stuff
    # O(n + k) space complexity for 'combined' (n entries) and heap (k-1 entries)
    def maxPerformance(self, n: int, speed: list, efficiency: list, k: int) -> int:
        combined = []
        # sort by efficiency
        for s, e in zip(speed, efficiency):
            combined.append((s,e))
        combined.sort(key = lambda entry: entry[1], reverse = True)

        heap = []
        totalSpeed, perf = 0, 0
        # assume current member to be the least efficient, how fast can k-1 more efficient members be at best
        for s, e in combined:
            # more than k-1 candidates, remove the slowest from the heap
            # efficiency not important here, since lowest efficiency fixed by 's'
            if len(heap) > k-1: totalSpeed -= heapq.heappop(heap)
            # 's' is a candidate for a team of efficiency <= 'e'
            heapq.heappush(heap, s)
            totalSpeed += s
            perf = max(perf, totalSpeed * e)

        return perf % (10**9+7)


testcases = [
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2, 60),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3, 68),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4, 72)
]

for i, (n, speed, efficiency, k, target) in enumerate(testcases):
    output = Solution().maxPerformance(n, speed, efficiency, k)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')