class Solution:
    # O(n) time complexity: n = len(s)
    # O(1) space complexity: mapping obviously contains at most 26 letters no matter s
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappingST = {}
        mappingTS = {}
        
        for i, j in zip(s, t):
            if i not in mappingST:
                if j in mappingTS: return False
                mappingST[i] = j
                mappingTS[j] = i
            elif mappingST[i] != j: return False
            
        return True
                
            
testcases = [
    ('baba', 'badc', False),
    ('egg', 'odd', True)
]

for i, (s, t, target) in enumerate(testcases):
    output = Solution().isIsomorphic(s, t)
    print('Case #{} should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')