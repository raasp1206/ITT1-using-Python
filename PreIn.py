class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left_bound, right_bound):
            if left_bound > right_bound:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            pivot_idx = inorder_map[root_val]
            root.left = helper(left_bound, pivot_idx - 1)
            root.right = helper(pivot_idx + 1, right_bound)
            
            return root
            
        return helper(0, len(inorder) - 1)
