class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return max(left, right) + 1

        height(root)
        return self.max_diameter