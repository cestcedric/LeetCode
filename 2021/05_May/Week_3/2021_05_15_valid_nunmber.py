class Solution:
    # pre-check if only valid chars included
    # float(s) would correctly parse 'inf' which is not valid here
    validChars = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
        '.', 'e', 'E', '-', '+'
    ]

    def isNumber(self, s: str) -> bool:
        for c in s:
            if c not in self.validChars:
                return False
        try:
            float(s)
            return True
        except:
            return False


testcases = [
    ('0', True),
    ('e', False),
    ('.', False),
    ('.1', True),
    ('10034.45', True),
    ('10e4', True),
    ('10E5', True),
    ('-354', True),
    ('+345.45', True),
    ('+35.3.4', False),
    ('-56456.', True),
    ('inf', False)
]

for i, (s, r) in enumerate(testcases):
    result = Solution().isNumber(s)
    print('Case #{} solved: {}'.format(i+1, r == result))
    # assert r == result
print('All test cases passed!')