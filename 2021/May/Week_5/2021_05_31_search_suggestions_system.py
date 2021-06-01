class Solution:
    def suggestedProducts(self, products: list, searchWord: str) -> list:
        # Probably O(n log(n)) time complexity
        # Not using binary search for start position, but caching result from previous round
        # O(3*s*p) space complexity, with s average length of searchWord and p average length of product name
        products.sort()
        length = len(products)
        output = []
        _n = 0
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            suggestions, n, j = [], _n, 0
            while n < length and products[n][:i] != prefix: n += 1
            _n = n # save first match to skip known wrong part
            while n < length and j < 3 and products[n][:i] == prefix:
                suggestions.append(products[n])
                n += 1
                j += 1 
            output.append(suggestions)
        return output


testcases = [
    (["mobile","mouse","moneypot","monitor","mousepad"], 'mouse', [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]),
    (["havana"], 'havana', [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
    (["bags","baggage","banner","box","cloths"], 'bags', [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]),
    (["havana"], 'tatiana', [[],[],[],[],[],[],[]])
]
        
for i, (input, searchword, target) in enumerate(testcases):
    output = Solution().suggestedProducts(input, searchword)
    print('Case #{} target:'.format(i+1))
    for t in target:
        print(t)
    print('Output:')
    for o in output:
        print(o)
    assert target == output
print('All test cases passed')
