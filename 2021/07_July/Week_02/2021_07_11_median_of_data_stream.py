from sortedcontainers import SortedList
import heapq

class MedianFinderSorted:

    # O(n) space complexity to hold all data
    def __init__(self):
        self.data = SortedList()
        self.size = 0
        
    # O(log(n)) time complexity per insertion 
    # => O(n * log(n)) time complexity for all elements
    # Only because we use SortedList, binary search + insertion is actually O(log(n) + n)
    def addNum(self, num: int) -> None:
        self.data.add(num)
        self.size += 1
        
    # O(1) time complexity
    def findMedian(self) -> float:
        if self.size % 2 == 1: return self.data[self.size // 2]
        else: 
            mid = self.size // 2
            return (self.data[mid - 1] + self.data[mid]) / 2


class MedianFinderHeap:

    # O(n) space complexity
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.minSize = 0
        self.maxSize = 0

    # O(log(n / 2)) time complexity per insertion, O(n log(n / 2)) total
    def addNum(self, num: int) -> None:
        if self.minSize == self.maxSize:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, num))
            self.minSize += 1
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, -num))
            self.maxSize += 1

    # O(1) time complexity
    def findMedian(self) -> float:
        if self.maxSize != self.minSize: return -self.minHeap[0]
        else: return (self.maxHeap[0] - self.minHeap[0]) / 2
        


m = MedianFinderHeap()
m.addNum(1)
m.addNum(2)
assert m.findMedian() == 1.5
m.addNum(3)
assert m.findMedian() == 2