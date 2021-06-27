class Solution:
    # O(n) time complexity: two passes through ratings
    # O(n) space complexity: two additional arrays of size n
    def candy(self, ratings: list) -> int:
        candy_left = [1 for _ in ratings]
        candy_right = [1 for _ in ratings]
        n = len(ratings)

        c = 1
        for r in range(1, n):
            if ratings[r - 1] < ratings[r]: c += 1
            else: c = 1
            candy_left[r] = c

        c = 1
        for r in range(n - 2, -1, -1):
            if ratings[r + 1] < ratings[r]: c += 1
            else: c= 1
            candy_right[r] = c

        total = 0
        for left, right in zip(candy_left, candy_right):
            total += max(left, right)

        return total


testcases = [
    ([1,0,2], 5),
    ([1,2,2], 4),
]

for i, (input, target) in enumerate(testcases):
    output = Solution().candy(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        