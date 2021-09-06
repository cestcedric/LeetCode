class Solution:
    # O(n) time: one pass through arrays
    # O(1) space
    def slowestKey(self, releaseTimes: list, keysPressed: str) -> str:
        longestKey, longestPress = keysPressed[0], releaseTimes[0]
        
        for t in range(1, len(keysPressed)):
            d = releaseTimes[t] - releaseTimes[t - 1]
            k = keysPressed[t]
            if d > longestPress:
                longestKey = k
                longestPress = d
            elif d == longestPress:
                longestKey = max(longestKey, k)

        return longestKey



testcases = [
    ([9,29,49,50], 'cbcd', 'c'),
    ([12,23,36,46,62], 'spuda', 'a'),
    ([23,34,43,59,62,80,83,92,97], 'qgkzzihfc', 'q')
]

for i, (releaseTimes, keysPressed, target) in enumerate(testcases):
    output = Solution().slowestKey(releaseTimes, keysPressed)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))