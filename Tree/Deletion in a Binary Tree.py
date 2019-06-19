class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
def deleteLast(root,deepnode):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp is deepnode:
            temp = None
            return
        if temp.right:
            if temp.right is deepnode:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left :
            if temp.left is deepnode:
                temp.left = None
                return
            else:
                q.append(temp.left)
def delete(root,key):
    q = []
    q.append(root)
    while len(q):
        temp=q.pop(0)
        if temp.data == key:
            keynode=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    x=temp.data
    deleteLast(root,temp)
    keynode.data = x
    
root = Node(1) 
root.left = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
print("The tree before the deletion:") 
inorder(root)
print()
key = 5
delete(root, key)  
print("The tree after the deletion;") 
inorder(root)     
