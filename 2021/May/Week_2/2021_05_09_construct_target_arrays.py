import heapq

class Solution:
    def isPossible(self, target: list) -> bool:
        # idea biggest element generated in last sum => go backwards until we have 1 everywhere
        # or not, then it doesn't work
        total = sum(target)
        # heap returns smallest element, so turn everything around
        heap = [-t for t in target]
        heapq.heapify(heap)
        while heap[0] != -1:
            _max = -heapq.heappop(heap)
            total -= _max
            if total < 1 or _max <= total:
                return False
            _max %= total
            total += _max
            heapq.heappush(heap, -_max)
        return True


testcases = [
    ([9,3,5], True),
    ([1,1,1,2], False),
    ([8,5], True),
    ([9,9,9], False),
    ([1,1000000000], True)
]

for i, (target, result) in enumerate(testcases):
    x = Solution().isPossible(target)
    print('Case #{} solved correctly: {}'.format(i+1, x == result))