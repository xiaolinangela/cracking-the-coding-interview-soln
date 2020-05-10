class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ValidateBST(root):
    if not root:
        return True
    stack = [(root,float('-inf'),float('inf'))]
    while stack:
        root, lower, upper = stack.pop()
        if not root:
            continue
        val = root.val 
        if val < lower or val >= upper:
            return False
        
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
    
    return True

if __name__ == "__main__":
    t = TreeNode(3)
    t.right = TreeNode(10)
    t.right.left = TreeNode(5)
    t.left = TreeNode(2)
    print(ValidateBST(t))
    
