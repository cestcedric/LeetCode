class Solution:
    def ambiguousCoordinates(self, s: str) -> list:

        s = s[1:-1]

        def setPoint(s: str) -> list:
            output = []
            if s == '0' or not s[0] == '0': output.append(s)
            for i in range(1, len(s)):
                left = s[:i]
                right = s[i:]
                if (left == '0' or not left[0] == '0') and not right[-1] == '0':
                    output.append('{}.{}'.format(left, right))
            return output

        output = []
        # O(n) to try all places for comma
        for i in range(1, len(s)):
            # O(n) to get all decimal point positions
            left = setPoint(s[:i])
            right = setPoint(s[i:])
            # O(n^2) to combine all different possibilities
            for l in left:
                for r in right:
                    output.append('({}, {})'.format(l, r))
        return output





testcases = [
    ('(123)', ['(1, 23)', '(12, 3)', '(1.2, 3)', '(1, 2.3)']),
    ('(00011)', ['(0.001, 1)', '(0, 0.011)']),
    ('(0123)', ['(0, 123)', '(0, 12.3)', '(0, 1.23)', '(0.1, 23)', '(0.1, 2.3)', '(0.12, 3)']),
    ('(100)', ['(10, 0)'])
]
        
for i, (s, t) in enumerate(testcases):
    result = Solution().ambiguousCoordinates(s)
    print('Case #{} should be:\n{}\n is\n{}'.format(i+1, t, result))
    assert sorted(result) == sorted(t)
print('All test cases solved!')