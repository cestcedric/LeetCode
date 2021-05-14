# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def toString(self):
        queue = []
        node = self
        output = [node.val]
        if node.left or node.right: queue += [node.left, node.right]

        while len(queue) > 0:
            node = queue.pop(0)
            output += [node.val if node else node]
            if node and (node.left or node.right): queue += [node.left, node.right]
        return output


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root or not root.left and not root.right: return root
        right = root.right
        root.right = self.flatten(root.left)
        root.left = None
        node = root
        while node.right:
            node = node.right
        node.right = self.flatten(right)
        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node1.left, node1.right = node2, node5
node2.left, node2.right = node3, node4
node5.right = node6

tree = node1.toString()
print('Tree: {}'.format(tree))
Solution().flatten(node1)
flat = node1.toString()
print('Flat: {}'.format(flat))
assert flat == [1, None, 2, None, 3, None, 4, None, 5, None, 6]
print('Test passed!')







    