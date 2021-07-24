class Solution:

    # O(w) time complexity: word1 and word2 both of length w
    def dist(self, word1, word2):
        d = 0
        for x, y in zip(word1, word2):
            d += (x != y)
        return d


    # O(n * w * w * len(alphabet)) time complexity: check if modification fo node closer to target
    # O(n*n) space complexity: if all nodes equidistant to endWord, all nodes point at all nodes
    def buildGraph(self, beginWord, endWord, wordList):
        graph = {word: [] for word in wordList}
        graph[beginWord] = []
        alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
            
        for node in graph:
            for i in range(len(node)):
                for letter in alphabet:
                    word = node[:i] + letter + node[i + 1:]
                    if word not in graph: continue
                    if self.dist(node, word) == 1 and self.dist(node, endWord) >= self.dist(word, endWord):
                        graph[node].append(word)
        
        return graph


    # O(n) time complexity: every node visited at most once
    # O(n * n) space complexity: at most n entries, each entry stores a path of length at most n
    # Very loose upper bound on space complexity: the more entries are in queue, the shorter the paths are
    def findPaths(self, graph, start, end):
        paths = []
        queue = [(start, [])]
        visited = set()
        found = False

        while queue != []:
            nextLevel = []
            for node, path in queue:
                if node == end: 
                    paths.append(path + [end])
                    found = True
                    continue

                visited.add(node)
                for dst in graph[node]:
                    if dst not in visited: nextLevel.append((dst, path + [node]))

            if found: break
            queue = nextLevel

        return paths


    # Time complexity depending on buildGraph
    # Space complexity depending on findPaths
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        if endWord not in wordList: return []
        graph = self.buildGraph(beginWord, endWord, wordList)
        return self.findPaths(graph, beginWord, endWord)


testcases = [
    ('hit', 'cog', ['hot','dot','dog','lot','log','cog'], [['hit','hot','dot','dog','cog'],['hit','hot','lot','log','cog']]),
    ('hit', 'cog', ['hot','dot','dog','lot','log'], []),
    ('a', 'c', ['a', 'b', 'c'], [['a', 'c']]),
    ('red', 'tax', ['ted','tex','red','tax','tad','den','rex','pee'], [['red','ted','tad','tax'],['red','ted','tex','tax'],['red','rex','tex','tax']])
]

for i, (beginWord, endWord, wordList, target) in enumerate(testcases):
    output = Solution().findLadders(beginWord, endWord, wordList)
    print('Case #{} should be:'.format(i + 1))
    for path in sorted(target):
        print(path)
    print('Output:')
    for path in sorted(output):
        print(path)
    assert sorted(output) == sorted(target)
print('All test cases passed!')
        