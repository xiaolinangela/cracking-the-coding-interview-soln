from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_level_BFS(root):
    if not root:
        return None
    levels = []
    queue = deque([root])
    level = 0
    while queue:
        level_length = len(queue)
        levels.append([])
        for i in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels

def create_level_recursion(root):
    levels = []
    level = 0
    def helper(node,level):
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        if node.left:
            helper(node.left,level+1)
        if node.right:
            helper(node.right,level+1)
    helper(root,level)
    return levels

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(create_level_recursion(root))