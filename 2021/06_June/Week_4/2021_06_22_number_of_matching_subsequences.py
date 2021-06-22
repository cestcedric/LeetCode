class Solution:
    # O(n*m*w) time complexity, with n = len(s), m = avg(len(word)), w = len(words)
    # O(1) space complexity
    def numMatchingSubseqFind(self, s: str, words: list) -> int:
        subseqs = 0

        for word in words:
            i = 0
            subseqs += 1
            for w in word:
                i = s.find(w, i) + 1
                if i == 0: 
                    subseqs -= 1
                    break

        return subseqs


testcases = [
    ('abcde', ['a','bb','acd','ace'], 3),
    ('dsahjpjauf', ['ahjpjau','ja','ahbwzgqnuk','tnmlanowax'], 2),
    ('hallohallo', ['abcd', 'eeeee', 'pimelpomel'], 0)
]


for i, (s, words, target) in enumerate(testcases):
    output = Solution().numMatchingSubseq(s, words)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')
        