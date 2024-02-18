# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return self.recursive1(root, p, q)
        return self.recursive2(root, p, q)
        # return self.iterative(root, p, q)

    def recursive1(self, root, p, q):
        self.res = None
        def helper(node):
            if not node: return False
            if (node.val >= p.val and node.val <= q.val) or (node.val >= q.val and node.val <= p.val):
                self.res = node
                return True
            helper(node.left)
            helper(node.right)
            return False

        helper(root)
        return self.res
    
    def recursive2(self, root, p, q):
        self.res = None
        def helper(node):
            if not node: return
            if node.val > p.val and node.val > q.val: helper(node.left)
            elif node.val < p.val and node.val < q.val: helper(node.right)
            else:
                self.res = node
                return

        helper(root)
        return self.res
    
    def iterative(self, root, p, q):
        node = root

        while node:
            if node.val < p.val and node.val < q.val: node = node.right
            elif node.val > p.val and node.val > q.val: node = node.left
            else: return node
        
        return None
