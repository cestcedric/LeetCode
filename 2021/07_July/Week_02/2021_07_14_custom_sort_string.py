from collections import Counter
from functools import cmp_to_key

class Solution:
    # O(n * log(n)) time complexity: it's sorting after all
    # O(n) space complexity: temporarilly allocate memory for list
    def customSortStringComparator(self, order: str, str: str) -> str:
        orderDict = {c: i for i, c in enumerate(order)}
        
        def comparator(a, b):
            nonlocal orderDict
            orderA = orderDict[a] if a in orderDict else 25
            orderB = orderDict[b] if b in orderDict else 26
            return orderA - orderB

        return ''.join(sorted(list(str), key = cmp_to_key(comparator)))


testcases = [
    ('cba', 'abcd', 'cbad')
]

for i, (order, string, target) in enumerate(testcases):
    output = Solution().customSortString(order, string)
    print('Case #{}: should be\n\'{}\', is\n\'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')