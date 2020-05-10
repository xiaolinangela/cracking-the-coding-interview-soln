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
        if val <= lower or val > upper:
            return False
        stack.append((root.right, val, upper))
        stack.append((root.left, lower, val))
    return True

def ValidateBST_recursion(root, lower, upper):
    if not root:
        return True
    if root.val <= lower or root.val > upper:
        return False
    return ValidateBST_recursion(root.left, lower, root.val) and ValidateBST_recursion(root.right, root.val, upper)


if __name__ == "__main__":
    t = TreeNode(3)
    t.right = TreeNode(10)
    t.right.left = TreeNode(1)
    t.left = TreeNode(2)
    print(ValidateBST(t))
    print(ValidateBST_recursion(t, -1000, 1000))
    

# TimeComplexity O(n)
# SpaceComplexity O(n)