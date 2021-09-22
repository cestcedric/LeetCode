class Solution:
    # O(2^n) time: we always try every combination
    # O(n) space: temporary candidate list at most contains all input strings
    # obviously bruteforce solution, but works given the small input size
    def uniqueChars(self, stringList: list) -> list:
        fp = [0] * 26
        for s in stringList:
            for c in s:
                if fp[ord(c) - ord('a')] == 1:
                    return False
                fp[ord(c) - ord('a')] = 1

        return True


    def maxLength(self, arr: list) -> int:
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


testcases = [
    (['un','iq','ue'], 4),
    (['cha','r','act','ers'], 6),
    (['abcdefghijklmnopqrstuvwxyz'], 26),
    (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'], 16)
]


for i, (arr, target) in enumerate(testcases):
    output = Solution().maxLength(arr)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        