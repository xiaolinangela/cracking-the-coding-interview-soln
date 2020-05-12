class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def first_common_ancestor(root,p,q):
    left = None
    right = None
    if root.val == p.val or root.val == q.val:
        return root
    if root.left:
        left = first_common_ancestor(root.left, p, q)
    if root.right:
        right = first_common_ancestor(root.right, p, q)
    if left and right:
        return root
    if left == None and right == None:
        return None
    return left if left else right

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left = TreeNode(2)
    p = root.right
    q = root.right.right
    result = first_common_ancestor(root,p,q)
    print(result.val)