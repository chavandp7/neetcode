from typing import Optional

from TreeNode import TreeNode


class Solution:
    def find_sub_root(self, root, val, root_list):
        if not root:
            return

        if root.val == val:
            root_list.append(root)

        self.find_sub_root(root.left, val, root_list)

        self.find_sub_root(root.right, val, root_list)

    def equal_trees(self, root1, root2):
        if not root1 and not root2:
            return True

        if (root1 and not root2) or (root2 and not root1):
            return False

        if root1.val != root2.val:
            return False

        left = self.equal_trees(root1.left, root2.left)
        right = self.equal_trees(root1.right, root2.right)

        if not left or not right:
            return False

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_list = []
        self.find_sub_root(root, subRoot.val, root_list)

        for sub_root in root_list:
            if self.equal_trees(sub_root, subRoot):
                return True

        return False
