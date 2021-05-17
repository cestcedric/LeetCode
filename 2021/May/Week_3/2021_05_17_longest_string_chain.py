from functools import lru_cache

class Solution:
    # Time complexity O(n*L^2), where L is the maximum length of a word
    # Space complexity O(n*L^2)
    def longestStrChain(self, words: list) -> int:
        dict = {w: len(w) for w in words}

        @lru_cache(None)
        def chainLength(word: str) -> int:
            if word not in dict: return 0
            return max(chainLength(word[:i] + word[i+1:]) for i in range(dict[word])) + 1


        return max(chainLength(word) for word in words)


testcases = [
    (["a","b","ba","bca","bda","bdca"], 4),
    (["xbc","pcxbcf","xb","cxbc","pcxbc"], 5),
    (['hallo', 'test'], 1)
]
for i, (words, res) in enumerate(testcases):
    result = Solution().longestStrChain(words)
    print('Case #{}: should be {}, is {}'.format(i+1, res, result))
    assert res == result
print('All test cases passed!')