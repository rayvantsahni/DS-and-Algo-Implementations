class Node:
    def __init__(self, value = None):
        self.value = value #stores the value of the node
        self.left = None #stores the left child node
        self.right = None #stores the right child node
        self.parent = None #stores the parent node
        
    def get_value(self): #gives the value of the node
        return self.value
    
    def get_left(self): #gives the left child of the node
        return self.left
    
    def get_right(self): #gives the right child of the node
        return self.right
        
    def get_parent(self): #gives the parent of the node
        return self.parent
        
    
    
class BST:
    def __init__(self):
        self.root = None #stores the root node of the tree
        
#--------------------------------------------------------
    def insert(self, value):
        if not self.root: #checks if the root node is Null or not; if it is Null, then it sets the root node
            self.root = Node(value)
        else:
            self._insert(value, self.root)
        
        
    def _insert(self, value, current_node):
        
        if value < current_node.get_value(): #handles the insertion of values smaller than the root
            if not current_node.get_left():
                current_node.left = Node(value)
                current_node.get_left().parent = current_node
            else:
                self._insert(value, current_node.get_left())
                
        elif value > current_node.get_value(): #handles the insertion of values greater than the root
            if not current_node.get_right():
                current_node.right = Node(value)
                current_node.get_right().parent = current_node
            else:
                self._insert(value, current_node.get_right())
                
        else: #handles the insertion of values that already exist
            print(value, "already exists!!")
#---------------------------------------------------------            

#---------------------------------------------------------
    def get_height(self): #gives the height of the tree
        if self.root: #checks if the root exists
            return self._get_height(self.root)
        else:
            return 0
        
    
    def _get_height(self, current_node):
        if current_node.get_left() and current_node.get_right(): #handles the case where the node has both the children
            return 1 + max(self._get_height(current_node.get_left()), self._get_height(current_node.get_right()))
        elif current_node.get_left(): #handles the case where the node only has a left child
            return 1 + self._get_height(current_node.get_left())
        elif current_node.get_right(): #handles the case where the node only has a right child
            return 1 + self._get_height(current_node.get_right())
        else: #handles the case where the node doesn't have any children
            return 1
#--------------------------------------------------------    
    
#--------------------------------------------------------    
    def search(self, value_to_find):   
        if self.root: #checks if the tree has a root node
            if self.root.get_value() == value_to_find: #checks if the value is present in the root
                return True
            elif value_to_find < self.root.get_value():
                return self._search(self.root.get_left(), value_to_find)            
            elif value_to_find > self.root.get_value():
                return self._search(self.root.get_right(), value_to_find)
        
        else:
            return False    
        
    
    def _search(self, node, value_to_find):
        if not node: #handles the scenario when the element is not present in the tree
            return False
        elif value_to_find == node.get_value():
            return True 
        elif value_to_find < node.get_value():
            return self._search(node.get_left(), value_to_find)
        elif value_to_find > node.get_value():
            return self._search(node.get_right(), value_to_find)
#-------------------------------------------------------

#-------------------------------------------------------
    def get_size(self): #gives the size of the tree, i.e the number of nodes in the tree
        if self.root: #checks if the tree has a root node
            return self._get_size(self.root)
        else:
            return 0
        
    
    def _get_size(self, current_node):
        if current_node.get_left() and current_node.get_right(): #hanldes the case where the node has both the children
            return 1 + self._get_size(current_node.get_right()) + self._get_size(current_node.get_left())
        elif current_node.get_left(): #handles the case where the node only has a left child
            return 1 + self._get_size(current_node.get_left())
        elif current_node.get_right(): #handles the case where the node only has a right child
            return 1 + self._get_size(current_node.get_right())
        else:
            return 1
#------------------------------------------------------
            
#------------------------------------------------------

    def minimum_value_node(self, current_node): #finds the node with the minimum value when a node with 2 children is being removed
        while current_node.get_left():
            current_node = current_node.get_left()
        return current_node


    def remove(self, value_to_remove):
        if not self.root: #handles the case when the tree doesn't have a root, i.e the tree is empty
            print("The tree is already empty!")
            return False
        elif self.search(value_to_remove):
            self._remove(value_to_remove)
        else: #handles the case when the node doesn't exist in the tree
            print("This value does not exist!")
            return False
            
            
    def _remove(self, value_to_remove):
        # CASE 1: REMOVING ROOT
        if value_to_remove == self.root.get_value(): #handles the case when the node to be removed is the root node
            if not self.root.get_left() and not self.root.get_right(): #when the root node doesn't have any children
                self.root = None
            elif self.root.get_left() and not self.root.get_right(): #when the root node doesn't have a right child
                self.root = self.root.get_left()
            elif self.root.get_right() and not self.root.get_left(): #when the root node doesnt't have a left child
                self.root = self.root.get_right()
            elif self.root.get_left() and self.root.get_right(): #when the root has both the children
                replacement_node = self.minimum_value_node(self.root.get_right())
                self.root.value = replacement_node.get_value()
                
                if replacement_node.get_right(): #deleting the successor node
                    replacement_node.get_parent().left = replacement_node.get_right()
                elif not replacement_node.get_right():
                    replacement_node.get_parent().left = None
            return True
                    
        
        current_node = self.root
        while current_node and current_node.get_value() != value_to_remove: #looking for the node which has to be removed
            if current_node.get_value() > value_to_remove:
                current_node = current_node.get_left()
            elif current_node.get_value() < value_to_remove:
                current_node = current_node.get_right()
                
        parent_node = current_node.get_parent() #setting the parent node of the node that has to be removed
                
        # CASE 2: REMOVING A NODE WITH NO CHILDREN
        if not current_node.get_left() and not current_node.get_right(): #handles the case where the node doesn't have any children
            if parent_node.get_left().get_value() == value_to_remove:
                parent_node.left = None
            elif parent_node.get_right().get_value() == value_to_remove:
                parent_node.right = None
            current_node.parent = None
            return True
                
        # CASE 3A: REMOVING A NODE WITH ONLY LEFT CHILD
        elif current_node.get_left() and not current_node.get_right(): #handles the case where the node only has a left child
            if parent_node.get_left() == current_node:
                parent_node.left = current_node.get_left()
            elif parent_node.get_right() == current_node:
                parent_node.right = current_node.get_left()
            current_node.parent = None
            return True
                
        # CASE 3B: REMOVING A NODE WITH ONLY RIGHT CHILD
        elif current_node.get_right() and not current_node.get_left(): #handles the case where the node only has a right child
            if parent_node.get_left() == current_node:
                parent_node.left = current_node.get_right()
            elif parent_node.get_right() == current_node:
                parent_node.right = current_node.get_right()
            current_node.parent = None
            return True
                
        # CASE 4: REMOVING A NODE WITH 2 CHILDREN
        else: #handles the case where the node has 2 children
            replacement_node = self.minimum_value_node(current_node.get_right())
            current_node.value = replacement_node.get_value() #replacing the value of the node to be deleted by its successor's value
            
            #deleting the successor node
            if replacement_node.get_right(): #handles the case where the successor node has a right child
                if replacement_node.get_parent().get_left() == replacement_node:
                    replacement_node.get_parent().left = replacement_node.get_right()
                elif replacement_node.get_parent().get_right() == replacement_node:
                    replacement_node.get_parent().right = replacement_node.get_right()
                    
                replacement_node.parent = None
               
            elif not replacement_node.get_right(): #handles the case where the successor node doesn't have a right child
                if replacement_node.get_parent().get_left() == replacement_node:
                    replacement_node.get_parent().left = None
                elif replacement_node.get_parent().get_right() == replacement_node:
                    replacement_node.get_parent().right = None
                    
                replacement_node.parent = None
                
            return True
#-------------------------------------------------------
            

#-------------------------------------------------------
    def inorder(self): #prints the inorder traversal
        if self.root:
            print("\nInorder Traversal ==>")
            self._inorder(self.root)
            print()
        else:
            print("Nothing in the Tree")
            
    def _inorder(self, current_node):
        if current_node:
            self._inorder(current_node.get_left())
            print(current_node.get_value(), end = " ")
            self._inorder(current_node.get_right())
        
    
    def preorder(self): #prints the preorder traversal
        if self.root:
            print("\nPreorder Traversal ==>")
            self._preorder(self.root)
            print()
        else:
            print("Nothing in the Tree")
        
    def _preorder(self, current_node):
        if current_node:
            print(current_node.get_value(), end = " ")
            self._preorder(current_node.get_left())
            self._preorder(current_node.get_right())


    def postorder(self): #prints the postorder traversal
        if self.root:
            print("\nPostorder Traversal ==>")
            self._postorder(self.root)
            print()
        else:
            print("Nothing in the Tree")
        
    def _postorder(self, current_node):
        if current_node:
            self._postorder(current_node.get_left())
            self._postorder(current_node.get_right())
            print(current_node.get_value(), end = " ")
#-----------------------------------------------------
 
            
tree = BST()

tree.insert(50)
tree.insert(10)
tree.insert(75)
tree.insert(90)
tree.insert(23)
tree.insert(6)
tree.insert(44)
tree.insert(29)
tree.insert(65)
tree.insert(69)
tree.insert(55)
tree.insert(85)
tree.insert(88)
tree.insert(20)
tree.insert(12)
tree.insert(8)
tree.insert(88)
tree.insert(6)

print()

print(tree.search(6))
print(tree.search(50))
print(tree.search(88))
print(tree.search(85))
print(tree.search(22))
print(tree.search(0))
print(tree.search(8))
print(tree.search(44))
print(tree.search(99))

print()

print("Height of the tree is", tree.get_height(), end = "\n")
print("Size of the tree is", tree.get_size(), end = "\n")

tree.inorder()
tree.preorder()
tree.postorder()

print()

tree.remove(20)
tree.remove(69)
tree.remove(15) #does not exist in the tree
tree.remove(50)
tree.remove(29)
tree.remove(23)
tree.remove(99) #does not exist in the tree
tree.remove(50) #has already been removed

print("\n\nAFTER DELETION....\n")
print("Size of the tree is", tree.get_size(), end = "\n")

tree.inorder()
