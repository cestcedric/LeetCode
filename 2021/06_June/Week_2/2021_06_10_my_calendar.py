from bisect import bisect

class MyCalendar:

    def __init__(self):
        self.events = []
        self.earliest = None
        self.latest = None
        self.size = 0
        
        
    def book(self, start: int, end: int) -> bool:
        if self.earliest is None: 
            self.events.append((start, end))
            self.earliest = start
            self.latest = end
            self.size = 1
            return True
        if self.earliest >= end:
            self.events = [(start, end)] + self.events
            self.earliest = start
            self.size += 1
            return True
        if self.latest <= start:
            self.events.append((start, end))
            self.latest = end
            self.size += 1
            return True

        # manual binary search to find position
        # works, but obviously faster with library functions
        # left, right = 0, self.size - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     event = self.events[mid]
        #     if event[0] == start: return False
        #     if event[0] < start: 
        #         if event[1] > start: return False
        #         left = mid + 1
        #     if event[0] > start: 
        #         if event[0] < end: return False
        #         right = mid

        # if self.events[left][0] < end: return False
        # if self.events[left-1][1] > start: return False
        # self.events = self.events[:left] + [(start, end)] + self.events[left:]
        index = bisect(self.events, (start, end))
        if index == self.size or index == 0: return False # beginning and end checked above
        if self.events[index-1][1] > start: return False
        if self.events[index][0] < end: return False
        self.events.insert(index, (start, end))
        self.size += 1
        return True

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
bookings = [[20,29],[13,22],[44,50],[1,7],[2,10],[14,20]]
for b in bookings:
    print(b, ':', obj.book(b[0], b[1]))
    print(obj.events)
