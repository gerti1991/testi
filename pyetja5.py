
class Node:
   
    def __init__(self, data):
       
        self.data = data
        self.left = None
        self.right = None
 

def findParent(node : Node,
               val : int,
               parent : int) -> None:
    if (node is None):
        return

    if (node.data == val):

        print(parent)
    else:
        findParent(node.left,
                   val, node.data)
        findParent(node.right,
                   val, node.data)
 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

node = 5

findParent(root, node, -1)
 
