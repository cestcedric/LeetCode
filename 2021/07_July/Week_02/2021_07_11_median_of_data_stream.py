from sortedcontainers import SortedList

class MedianFinderSorted:

    # O(n) space complexity to hold all data
    def __init__(self):
        self.data = SortedList()
        self.size = 0
        
    # O(log(n)) time complexity per insertion 
    # => O(n * log(n)) time complexity for all elements
    def addNum(self, num: int) -> None:
        self.data.add(num)
        self.size += 1
        
    # O(1) time complexity
    def findMedian(self) -> float:
        if self.size % 2 == 1: return self.data[self.size // 2]
        else: 
            mid = self.size // 2
            return (self.data[mid - 1] + self.data[mid]) / 2


m = MedianFinderSorted()
m.addNum(1)
m.addNum(2)
assert m.findMedian() == 1.5
m.addNum(3)
assert m.findMedian() == 2