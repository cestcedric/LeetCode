class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        # editDistances = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        # we actually only need the current and the previous line => less memory
        editDistances = [[0 for _ in range(len2 + 1)] for _ in range(2)]

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if not i:
                    d = j
                elif not j:
                    d = i
                elif word1[i-1] == word2[j-1]:
                    d = editDistances[(i-1) % 2][j-1]
                else:
                    d = 1 + min(editDistances[(i-1) % 2][j], editDistances[i % 2][j-1])
                editDistances[i % 2][j] = d
        return d
        


testcases = [
    ('leetcode', 'etco', 4),
    ('sea', 'eat', 2),
    ('dogs', 'frogs', 3)
]

for w1, w2, s in testcases:
    d = Solution().minDistance(w1, w2)
    print('Distance between \'{}\' and \'{}\' is {}, should be {}.'.format(w1, w2, d, s))
    assert d == s