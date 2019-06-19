class Node: 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        
def buildTree(inOrder, preOrder, st, end):
    if st > end :
        return None
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    if st == end :
        return tNode
    else:
        inIndex = inOrder.index(tNode.data)
        tNode.left =  buildTree(inOrder, preOrder, st, inIndex - 1)
        tNode.right =  buildTree(inOrder, preOrder, inIndex + 1, end)
        return tNode

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
inOrder = [x for x in input().split()]
preOrder = [x for x in input().split()]
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
print('done:')
inorder(root)
