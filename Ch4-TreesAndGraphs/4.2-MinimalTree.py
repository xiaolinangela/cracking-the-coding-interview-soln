import queue

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    

def minBST(array, left, right):
    if left > right:
        return None
    p = (left + right) // 2

    root = TreeNode(array[p])
    root.left = minBST(array, left, p-1)
    root.right = minBST(array, p+1, right)
    return root

def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
  
# Print nodes at a given level 
def printGivenLevel(root , level): 
    if root is None: 
        return print("None")
    if level == 1: 
        print(root.val)
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 

def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  
if __name__ == "__main__":
    array = [-10, -3, 0, 5, 9]
    left = 0
    right = len(array) - 1
    result = minBST(array, left, right)
    printLevelOrder(result)
  


   


