class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def has_path_sum(root,sum):
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return has_path_sum(root.left,sum) or has_path_sum(root.right,sum)

if __name__ == "__main__":
    pass
    