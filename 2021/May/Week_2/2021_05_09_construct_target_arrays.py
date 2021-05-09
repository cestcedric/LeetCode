class Solution:
    def isPossible(self, target: list) -> bool:
        length = len(target)
        while True:
            print(target)
            _max = max(target)
            _max_index = target.index(_max)
            prev = target[_max_index]
            target[_max_index] -= (sum(target[:_max_index]) + sum(target[_max_index+1:]))
            if prev == target[_max_index]:
                return False
            checksum = sum(target)
            if checksum == length:
                return True
            if checksum < length:
                return False


testcases = [
    ([9,3,5], True),
    ([1,1,1,2], False),
    ([8,5], True),
    ([9,9,9], False),
    ([1,1000000000], True)
]

for i, (target, result) in enumerate(testcases):
    x = Solution().isPossible(target)
    print('Case #{} solved correctly: {}'.format(i+1, x == result))