def height(root): 
    if root is None: 
        return 0
    return max(height(root.left), height(root.right)) + 1
    
def isBalanced(root):
    if root is None:
        return True
    if abs(height(root.left)-height(root.right))<=1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False
