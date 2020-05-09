class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if not root:
        return True
    return abs(height(root.left) - height(root.right)) < 2 and isBalanced(root.left) and isBalanced(root.right)

if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(2)
    t.right = TreeNode(1)
    t.right.right = TreeNode(8)
    t.right.right.right = TreeNode(18)
    print(isBalanced(t))