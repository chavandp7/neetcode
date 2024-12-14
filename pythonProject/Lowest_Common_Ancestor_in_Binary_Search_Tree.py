# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import TreeNode

# root = [5, 3, 8, 1, 4, 7, 9, null, 2], p = 3, q = 4

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        low = min(p.val, q.val)
        high = max(p.val, q.val)

        if low <= root.val <= high:
            return root

        if root.left and high < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root.right, p, q)

if __name__ == "__main__":
    root = TreeNode(5)

    three = TreeNode(3)
    eight = TreeNode(8)

    root.left = three
    root.right = eight

    one = TreeNode(1)
    four = TreeNode(4)
    three.left = one
    three.right = four


    seven = TreeNode(7)
    nine = TreeNode(9)
    eight.left = seven
    eight.right = nine

    two = TreeNode(2)
    one.right = two

    solution = Solution()
    ancestor = solution.lowestCommonAncestor(root, TreeNode(3), TreeNode(4))
    print(ancestor.val)

