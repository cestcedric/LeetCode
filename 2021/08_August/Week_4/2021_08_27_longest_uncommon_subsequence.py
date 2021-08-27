class Solution:
    # O(k) time: k = len(string)
    def isSubstring(self, sub: str, string: str) -> bool:
        if sub == '': return True
        if len(sub) > len(string): return False
        i = 0
        for s in string:
            if s == sub[i]:
                i += 1
                if i == len(sub):
                    return True
        return False


    # O(n^2 * k) time: n = len(strs), k = average len(word)
    # O(1) space
    def findLUSlength(self, strs: list) -> int:
        # longest = -1
        # sorting longest to shortest:
        # assume subsequence only in one string
        # => subsequence + x still only in that one string
        # => longest subsequence is complete string
        # => can stop early by starting with longest string
        strs.sort(key = lambda s : len(s), reverse = True)

        # O(n)
        for i, a in enumerate(strs):
            substring = False
            # O(n)
            for j, b in enumerate(strs):
                if i == j: continue
                # O(k)
                if self.isSubstring(a, b): 
                    substring = True
                    break
            if not substring:
                return len(a)
                # if longest == -1: longest = len(strs[a])
                # else: longest = max(longest, len(strs[a]))

        return -1 # longest


testcases = [
    (['aba','cdc','eae'], 3),
    (['aaa', 'aaa', 'aa'], -1),
    (['aabbcc', 'aabbcc','cb','abc'], 2),
    (['aabbcc', 'aabbcc','c','e','aabbcd'], 6)
]

for i, (strs, target) in enumerate(testcases):
    output = Solution().findLUSlength(strs)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')