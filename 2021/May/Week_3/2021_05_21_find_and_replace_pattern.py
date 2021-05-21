class Solution:
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        # Similar to isomorphic strings task, just for every word in list
        # O(n*k) time complexity, n words of length k
        out = []
        dic_p = {}
        for i, c in enumerate(pattern):
            dic_p[c] = dic_p[c] + [i] if c in dic_p else [i]

        for word in words:
            # length check not needed when pattern and word length guaranteed
            # if len(word) != len(pattern): continue
            dic_w = {}
            pattern_matched = True
            for i, c in enumerate(word):
                dic_w[c] = dic_w[c] + [i] if c in dic_w else [i]

            for w, p in zip(dic_w.keys(), dic_p.keys()):
                if dic_w[w] != dic_p[p]: 
                    pattern_matched = False
                    break
            
            if pattern_matched: out.append(word)
        
        return out



testcases = [
    (["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]),
    (["a","b","c"], "a", ["a","b","c"]),
    (["a","b","c"], "abc", [])
]


for i, (words, pattern, result) in enumerate(testcases):
    out = Solution().findAndReplacePattern(words, pattern)
    print('Case #{}: should be {}, is {}'.format(i+1, result, out))
    assert result == out

print('All test cases solved')
        