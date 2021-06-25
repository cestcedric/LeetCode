from collections import deque

class Solution:
    
    # O(n^2) time complexity: n edges, O(n) DFS for each edge
    # O(n) space complexity: build graph with at most n entries, DFS with O(n) space complexity 
    def findRedundantConnection(self, edges: list) -> list:
        # build tree
        # when adding edge, check if connection possible, return if yes
        graph = {}
        

        # O(n) time complexity: looking at each node at most once
        # O(n) space complexity: deque and visited set with at most n entries
        # Classic DFS
        def dfs(a, b):
            nonlocal graph
            queue = deque([a])
            visited = set()

            while queue:
                node = queue.popleft()
                visited.add(node)

                if node == b: return True
                if node in graph:
                    if b in graph[node]: return True
                    for c in graph[node]: 
                        if c not in visited: queue.appendleft(c)
            return False

        for x, y in edges:
            if dfs(x, y): return [x, y]
            if x in graph: graph[x].append(y)
            else: graph[x] = [y]
            if y in graph: graph[y].append(x)
            else: graph[y] = [x]




testcases = [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
    ([[3,4],[1,2],[2,4],[3,5],[2,5]], [2,5])
]

for i, (input, target) in enumerate(testcases):
    output = Solution().findRedundantConnection(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')
        