class Solution:
    # O(n*l) time complexity: n words of average length l (dict lookup in O(1))
    # O(n) space complexity: additional dict containing all words
    def palindromePairs(self, words: list) -> list:
        positions = { x: i for i, x in enumerate(words) }
        output = []

        for i, w in enumerate(words):
            length = len(w)
            for l in range(length+1):
                pre, suf = w[:l], w[l:]

                # prefix is palindrome
                if pre == pre[::-1]:
                    k = w[l:][::-1]
                    if k in positions and positions[k] != i: output.append([positions[k], i])
                
                # suffix is palindrome
                if l == length: continue
                if suf == suf[::-1]:
                    k = w[:l][::-1]
                    if k in positions and positions[k] != i: output.append([i, positions[k]])
        
        return output



testcases = [
    (["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]]),
    (["bat","tab","cat"], [[0,1],[1,0]]),
    (["a",""], [[0,1],[1,0]]),
    (["abcb", "a"], [[0,1]]),
    (["hello", "b"], [])
]

for i, (input, target) in enumerate(testcases):
    output = Solution().palindromePairs(input)
    print('Case #{} should be:\n{}, is\n{}'.format(i+1, sorted(target), sorted(output)))
    assert sorted(target) == sorted(output)
print('All test cases passed!')