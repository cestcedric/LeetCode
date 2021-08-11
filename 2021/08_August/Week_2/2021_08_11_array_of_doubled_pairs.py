from collections import Counter

class Solution:
    # O(n * log(n)) time: sorting of at most n keys in counter
    # O(n) space: at most n entries in counter
    def canReorderDoubled(self, arr: list) -> bool:
        counter= Counter(arr)

        for x in sorted(list(counter.keys()), key = lambda x : abs(x)):
            if counter[x] == 0: continue
            if x * 2 not in counter: return False
            if counter[x * 2] < counter[x]: return False
            counter[x * 2] -= counter[x]

        return True



testcases = [
    ([3,1,3,6], False),
    ([2,1,2,6], False),
    ([4,-2,2,-4], True), # [-2, -4, 2, 4]
    ([1,2,4,16,8,4], False),
    ([6,2,1,3], True), # [1, 2, 3, 6]
    ([1,2,1,-8,8,-4,4,-4,2,-2], True) # [1, 2, 1, 2, -4, -8, 4, 8, -2, -4]
]

for i, (arr, target) in enumerate(testcases):
    output = Solution().canReorderDoubled(arr)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')