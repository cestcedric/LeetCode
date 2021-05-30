class Buckets:
        min_element = None
        max_element = None

        def insert(self, x):
            if self.min_element is None or x < self.min_element: self.min_element = x
            if self.max_element is None or x > self.max_element: self.max_element = x


class Solution:
    def maximumGap(self, nums: list) -> int:
        # Easy solution: sort, then find biggest gap => O(n log(n)) time complexity
        # O(n) time complexity wanted => bucket sort, find biggest gap between different buckets
        # O(2*n) for _min and _max, O(n) for bucket sort, O(n_buckets) for gap
        # Overall O(n) time complexity, and O(n) space complexity
        length = len(nums)
        if length < 2: return 0
        if length == 2: return abs(nums[0] - nums[1])
        _min, _max = min(nums), max(nums)
        diff = _max - _min
        n_buckets = length - 2
        d_buckets = (diff + n_buckets - 1) // n_buckets
        buckets = [ Buckets() for _ in range(n_buckets) ]
        for n in nums:
            if n != _min and n != _max:
                b = (n - _min) // d_buckets
                buckets[b].insert(n)
        
        max_gap = 0
        c = _min
        for b in buckets:
            if b.min_element is None: continue
            max_gap = max(max_gap, b.min_element - c)
            c = b.max_element
        max_gap = max(max_gap, _max - c)
        return max_gap




testcases = [
    ([3,6,9,1], 3),
    ([10], 0),
    ([1,10000], 9999),
    ([1,2,3], 1),
    ([1,2,3,7,8,9], 4),
    ([1,7,3,2,9,8], 4)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().maximumGap(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')