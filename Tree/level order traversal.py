class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def height(root):
    if root == None :
        return 0
    else:
        lh=height(root.left)
        rh=height(root.right)
        return (lh + 1) if (lh > rh) else (rh + 1)

def printGivenLevel(root,level):
    if root == None :
        return 0
    if level == 1:
        if root.data != None :
            print(root.data)
    else:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def printLevelOrder(root):
    for i in range(1,height(root)+1):
        l=printGivenLevel(root,i)
        if l is not None:
            print(l)
    
root = Node(1) 
root.left=Node(2) 
root.right=Node(3) 
root.left.left=Node(4) 
root.left.right=Node(5)
#print(height(root))
#printGivenLevel(root,3)
printLevelOrder(root)
