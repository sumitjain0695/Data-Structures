class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.key)
        preorder(root.left)
        preorder(root.right)
    
def postorder(root):
    if root:
        postorder(root.right)
        postorder(root.left)
        print(root.key)
    
root = Node(1) 
root.left=Node(2) 
root.right=Node(3) 
root.left.left=Node(4) 
root.left.right=Node(5)
print('inorder')
inorder(root)
print('preorder')
preorder(root)
print('postorder')
postorder(root)
