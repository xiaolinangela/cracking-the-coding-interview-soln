class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorder(t):
    if not t:
        return "null"
    return "#" + "{0}".format(t.val) + preorder(t.left) + preorder(t.right)

def is_subtree(s,t):
    tree1 = preorder(s)
    tree2 = preorder(t)
    try:
        tree1.index(tree2)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    s = TreeNode(3)
    s.left = TreeNode(1)
    s.right = TreeNode(2)
    s.left.left = TreeNode(4)
    s.left.right = TreeNode(5)
    t = TreeNode(1)
    t.left = TreeNode(4)
    # t.right = TreeNode(5)
    print(is_subtree(s,t))