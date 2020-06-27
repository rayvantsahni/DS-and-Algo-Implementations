# LINKED LIST IMPLEMENTATION IN PYTHON

# this is the node class
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
    # return the value of the node
    def get_value(self):
        return self.value
    
    # returns the node that the current node points to
    def get_next_node(self):
        return self.next_node


# this is the linked list class
class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
        
    # returns the head node of the linked list
    def get_head_node(self):
        return self.head_node
    
    # inserts a new node from the head
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next_node = self.head_node
        self.head_node = new_node
        
    # inserts a new node from the tail
    def insert_end(self, new_value):
        new_node = Node(new_value)
        current_node = self.head_node
        while current_node.get_next_node() != None:
            current_node = current_node.get_next_node()
        current_node.next_node = new_node
        
    # displays the contents of the linked list
    def display(self):
        elements = []
        current_node = self.head_node
        while current_node:
            elements.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return elements

    # removes a node
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node.get_next_node().get_value() != value_to_remove:
                current_node = current_node.get_next_node()
            current_node.next_node = current_node.get_next_node().get_next_node()
            
    # gives the length of the linked list
    def get_length(self):
        count = 0
        current_node = self.head_node
        while current_node != None:
            count += 1
            current_node = current_node.get_next_node()
        return count
     
    # gives the value at a particular index
    def value_at_index(self, index):
        current_index = 0
        current_node = self.head_node
        while current_node.get_next_node != None:
            if current_index == index:
                return current_node.get_value()
            current_node = current_node.get_next_node()
            current_index += 1
        
        
            
ll = LinkedList(10)
ll.insert_beginning(20)
ll.insert_beginning(30)
ll.insert_beginning(40)
ll.insert_beginning(50)
ll.insert_beginning(60)
ll.insert_beginning(70)

print("new linked list:\n", ll.display(), sep = "")
print("length is ", ll.get_length(), sep = "")

ll.remove_node(30)
print("after deletion:\n", ll.display(), sep = "")
print("length is ", ll.get_length(), sep = "")

ll.insert_end(0)
ll.insert_end(-10)
print("after adding element(s) in the end:\n", ll.display(), sep = "")
print("length is ", ll.get_length(), sep = "")
        

print("value is:", ll.value_at_index(0))
print("value is:", ll.value_at_index(2))
print("value is:", ll.value_at_index(7))
print("value is:", ll.value_at_index(1))
        
