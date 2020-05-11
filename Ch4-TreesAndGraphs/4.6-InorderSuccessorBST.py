class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def successor(root,p):
    successor = None
    while root:
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
        
    return successor

if __name__ == "__main__":
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.left.right = TreeNode(4)
    t.right = TreeNode(6)
    p = t.left.right
    result = successor(t,p)
    if result:
        print(result.val)
    else:
        print("None")