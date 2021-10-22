from collections import Counter

class Solution:
    # O(n) time: one pass through s
    # O(n) space: counter with at most n entries
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counts = [(char, count) for char, count in counter.items()]
        # lambda x : x[1] sufficient, 
        # but this way we get alphabetical order if same count
        counts.sort(reverse = True, key = lambda x : (x[1], -ord(x[0])))
        counts = [char * count for char, count in counts]
        return ''.join(counts)


testcases = [
    ('tree', 'eert'),
    ('cccaaa', 'aaaccc'),
    ('Aabb', 'bbAa')
]


for i, (s, target) in enumerate(testcases):
    output = Solution().frequencySort(s)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')