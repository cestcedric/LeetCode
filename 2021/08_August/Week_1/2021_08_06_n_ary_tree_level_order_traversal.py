# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # O(n) time: look at each node once
    # O(1) space: only new memory allocated is for output structure
    def levelOrder(self, root: 'Node') -> list:
        if root is None: return []
        
        nodes = [[root]]

        while nodes[-1] != []:
            nodes.append([])
            for node in nodes[-2]:
                for child in node.children:
                    nodes[-1].append(child)

        nodes.pop()

        for level in range(len(nodes)):
            for node in range(len(nodes[level])):
                nodes[level][node] = nodes[level][node].val

        return nodes