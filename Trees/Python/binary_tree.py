class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def get_value(self):
        return self.value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
   
    def set_left(self, value):
        self.left = Node(value)
        
    def set_right(self, value):
        self.right = Node(value)
    
    
class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
        
        
    def display_preorder(self, start_node):
        # Parent --> Left --> Right
        if start_node:
            print(start_node.get_value(), end = "  ")
            self.display_preorder(start_node.get_left())
            self.display_preorder(start_node.get_right())
            
    def display_inorder(self, start_node):
        # Left --> Parent --> Right
        if start_node:
            self.display_inorder(start_node.get_left())
            print(start_node.get_value(), end = "  ")
            self.display_inorder(start_node.get_right())
            
    def display_postorder(self, start_node):
        # Left --> Right --> Parent
        if start_node:
            self.display_postorder(start_node.get_left())
            self.display_postorder(start_node.get_right())
            print(start_node.get_value(), end = "  ")

            

tree = BinaryTree("root")

tree.root.set_left("A")
tree.root.set_right("C")

tree.root.get_left().set_left("B")
tree.root.get_left().get_left().set_left("D")
tree.root.get_left().set_right("E")

tree.root.get_right().set_left("G")
tree.root.get_right().get_left().set_left("H")
tree.root.get_right().get_left().set_right("I")
tree.root.get_right().set_right("F")
tree.root.get_right().get_right().set_right("J")

print("\nINORDER Traversal:")
tree.display_inorder(tree.root)

print("\nPREORDER Traversal:")
tree.display_preorder(tree.root)

print("\nPOSTORDER Traversal:")
tree.display_postorder(tree.root)

'''
         ROOT
       /     \
      a       c
     / \     / \
    b   e   g   f
   /       / \   \
  d       h   i   j
'''
