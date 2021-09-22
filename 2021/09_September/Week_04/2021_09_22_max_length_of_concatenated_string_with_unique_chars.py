class Solution:
    # O(1) time: always finished after looking at 26 letters
    # O(1) space: array with 26 entries
    def uniqueChars(self, stringList: list) -> list:
        fp = [0] * 26
        for s in stringList:
            for c in s:
                if fp[ord(c) - ord('a')] == 1:
                    return False
                fp[ord(c) - ord('a')] = 1

        return True

    # O(2^n) time: we always try every combination
    # O(n) space: temporary candidate list at most contains all input strings
    # obviously bruteforce solution, but works given the small input size
    def maxLengthBruteforce(self, arr: list) -> int:
        n = len(arr)
        if n == 1: return len(arr[0])

        combinations = 2**n
        maxLength = 0

        for i in range(1, combinations + 1):
            choices = bin(i)[2:].zfill(combinations)
            candidate = [s for idx, s in enumerate(arr) if choices[-idx - 1] == '1']

            if self.uniqueChars(candidate):
                maxLength = max(maxLength, sum(len(s) for s in candidate))
                if maxLength == 26: return maxLength

        return maxLength


    # O(2^n) time: on average a lot quicker than bruteforce bc. early pruning
    # O(n) space: call stack depth, at most combining all words
    def maxLength(self, arr: list) -> int:

        # O(1) time
        def containsDuplicates(s: str) -> bool:
            chars = [0] * 26
            for c in s:
                if chars[ord(c) - ord('a')] == 1: return True
                chars[ord(c) - ord('a')] = 1
            return False

        # O(n) time
        def fingerprint(s: str) -> list:
            fp = ['0'] * 26
            for c in s: fp[ord(c) - ord('a')] = '1'
            return int(''.join(fp), 2) 
        
        def backtrack(prefix: str, position: int) -> int:
            nonlocal arr

            prefixFP = fingerprint(prefix)
            maxLength = len(prefix)

            for i in range(position + 1, len(arr)):
                if prefixFP & fingerprint(arr[i]) == 0:
                    maxLength = max(maxLength, backtrack(prefix + arr[i], i))
                    if maxLength == 26: break

            return maxLength

        arr = [s for s in arr if not containsDuplicates(s)]
        if len(arr) == 0: return 0
        return max(backtrack(s, i) for i, s in enumerate(arr))



testcases = [
    (['un','iq','ue'], 4),
    (['cha','r','act','ers'], 6),
    (['abcdefghijklmnopqrstuvwxyz'], 26),
    (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'], 16),
    (["yy","bkhwmpbiisbldzknpm"], 0)
]


for i, (arr, target) in enumerate(testcases):
    output = Solution().maxLength(arr)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        