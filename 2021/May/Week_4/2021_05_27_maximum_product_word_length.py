class Solution:
    def maxProduct(self, words: list) -> int:
        # O(n^2) time complexity, all word combinations are tested
        # O(k) space complexity, where k is the average word length
        result = 0
        length = len(words)
        for x in range(length-1):
            w_s = set(words[x])
            w_l = len(words[x])
            for y in range(x+1, length):
                if w_s.isdisjoint(set(words[y])):
                    result = max(result, w_l * len(words[y]))
        return result



testcases = [
    (["abcw","baz","foo","bar","xtfn","abcdef"], 16),
    (["a","ab","abc","d","cd","bcd","abcd"], 4),
    (["a","aa","aaa","aaaa"], 0)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().maxProduct(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')