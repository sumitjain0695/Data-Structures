class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def identical(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    q1 = []
    q2 = []
    q1.append(root1)
    q2.append(root2)
    while q1 and q2:
        n1=q1.pop(0)
        n2=q2.pop(0)
        if n1.data != n2.data :
            return False
        if n1.left and n2.left :
            q1.append(n1.left)
            q2.append(n2.left)
        elif n1.left or n2.left :
            return False

        if n1.right and n2.right :
            q1.append(n1.right)
            q2.append(n2.right)
        elif n1.right or n2.right :
            return False
    return True

root1 = Node(1)  
root1.left = Node(2)  
root1.right = Node(3)  
root1.left.left = Node(4)  
root1.left.right = Node(5)  

root2 = Node(1)  
root2.left = Node(2)  
root2.right = Node(3)  
root2.left.left = Node(3)  
root2.left.right = Node(5)  

if identical(root1, root2): 
    print("Yes") 
else: 
    print("No")
