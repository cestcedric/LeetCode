from collections import Counter, defaultdict

class Solution:
    # O(n) time: n = max(len(s), len(t))
    # worst case scenario: both pointers traverse s, or len(t) > len(s)
    # O(1) space: dictionary with at most 26 entries
    def minWindow(self, s: str, t: str) -> str:
        minWindow, minWindowSize = '', len(s) + 1
        counter_t = Counter(t)
        counter_s = defaultdict(int)
        left, right, charsFound = 0, 0, 0

        # O(n)
        while right < len(s):
            c = s[right]

            counter_s[c] += 1

            if c in counter_t and counter_s[c] == counter_t[c]:
                charsFound += 1

            # O(right - left)
            while charsFound == len(counter_t) and left <= right:
                if right - left + 1 < minWindowSize:
                    minWindow = s[left : right + 1]
                    minWindowSize = right - left + 1

                c = s[left]
                counter_s[c] -= 1
                if c in counter_t and counter_s[c] < counter_t[c]:
                    charsFound -= 1
                left += 1

            right += 1

        return minWindow


testcases = [
    ('ADOBECODEBANC', 'ABC', 'BANC'),
    ('a', 'a', 'a'),
    ('a', 'aa', '')
]

for i, (s, t, target) in enumerate(testcases):
    output = Solution().minWindow(s, t)
    print('Case #{}: should be \'{}\', is \'{}\''.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')