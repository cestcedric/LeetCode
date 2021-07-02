from bisect import bisect_left

class Solution:
    # O(log(n) + k) time complexity: O(log(n)) to find middle, O(k) to create window of k
    # O(1) space complexity: constant number of variables used
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        n = len(arr)
        if n <= k: return arr
        
        left = bisect_left(arr, x) - 1
        right = left + 1

        while right - left - 1 < k:
            if left == -1: right += 1
            elif right == n or abs(x - arr[left]) <= abs(x - arr[right]): left -= 1
            else: right += 1

        return arr[left + 1 : right]




testcases = [
    ([1,2,3,4,5], 4, 3, [1,2,3,4]),
    ([1,2,3,4,5], 4, -1, [1,2,3,4]),
    ([1,2,4,5,6], 2, 3, [2,4]),
    ([0,2,2,3,4,6,7,8,9,9], 4, 5, [3,4,6,7]),
    ([1,3], 1, 2, [1]),
    ([1], 1, 1, [1])
]

for i, (input, k, x, target) in enumerate(testcases):
    output = Solution().findClosestElements(input, k, x)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, output))
    print('-----')
    assert target == output
print('All test cases passed!')
        