#Binary Tree creation
class Node:
    def __init__(self,data):
        self.data=data
        self.left= None
        self.right=None

root= Node(5)
root.left=Node(4)
root.right=Node(3)
root.left.left=Node(2)
root.left.right=Node(1)
root.right.left=Node(10)
root.right.right=Node(9)
root.right.left.left=Node(8)
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.right.left.data)
print(root.right.right.data)
print(root.right.left.left.data)