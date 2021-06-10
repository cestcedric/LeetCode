class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0

        numbers = [1 for _ in range(n+1)]
        numbers[0] = 0
        numbers[1] = 0
        f = 2
        while f < n**0.5:
            for i in range(f, n // f + 1):
                numbers[i*f] = 0
            f += 1
            while numbers[f] == 0 and f < n:
                f += 1
        return sum(numbers[:-1])
            



        


testcases = [
    (10,4),
    (2,0),
    (1,0),
    (0,0),
    (20,8),
    (3,1)
]

for i, (n, p) in enumerate(testcases):
    guess = Solution().countPrimes(n)
    print('Case #{} should be {}, is {}.'.format(i+1, p, guess))
    assert guess == p
print('Tests passed!')