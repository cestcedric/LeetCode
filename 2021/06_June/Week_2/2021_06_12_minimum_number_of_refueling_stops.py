import heapq

class Solution:
    # O(n log(n)) time complexity: one pass through all stations, but heappush with O(n log(n))
    # O(n) space complexity: heap and tmpStations
    def minRefuelStops(self, target: int, startFuel: int, stations: list) -> int:
        if startFuel >= target: return 0
        if stations == []: return -1
        tmpStations = stations + [[target, 0]]
        length = len(tmpStations)

        passed = []
        stops = 0
        distCovered = 0
        for i in range(length):
            # drive up to next station
            startFuel -= (tmpStations[i][0] - distCovered)

            # not enough fuel, go back and fuel up
            while passed and startFuel < 0:
                startFuel -= heapq.heappop(passed)
                stops += 1
            if startFuel < 0: return - 1

            heapq.heappush(passed, -tmpStations[i][1])
            distCovered = tmpStations[i][0]
        
        return stops

testcases = [
    (1, 1, [], 0),
    (100, 10, [[10,60],[20,30],[30,30],[60,40]], 2),
    (100, 1, [[10,100]], -1),
    (100, 10, [[10,20],[20,80],[30,30],[60,40]], 2),
    (100, 50, [[60, 50]], -1)
]

for i, (target, startFuel, stations, expected) in enumerate(testcases):
    output = Solution().minRefuelStops(target, startFuel, stations)
    print('Case #{}: should be {}, is {}'.format(i+1, expected, output))
    assert expected == output
print('All test cases passed!')