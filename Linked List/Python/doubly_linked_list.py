class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def get_value(self):
        return self.value
    
    
    
    
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
        
    def prepend(self, new_value): #inserts a value at the beginning of the list
        new_node = Node(new_value)
        
        if not self.head: #checks if the list has any elements before inserting
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
            
    def append(self, new_value): #inserts a value at the end of the list
        new_node = Node(new_value)
        
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.next = new_node
            new_node.prev = current_node
            
            
    def exists(self, value_to_find): #checks whether a value exists in the list or not
        if not self.head: #case where the list is empty
            return False
        current_node = self.head
        while current_node:
            if current_node.get_value() == value_to_find:
                return True
            current_node = current_node.get_next()
        return False
            
            
    def insert_after(self, node_value, new_value): #inserts after a particular specified element in the list
        if not self.exists(node_value):
            print(node_value, "not in the list.")
            return
        else:
            current_node = self.head
            while current_node.get_value() != node_value:
                current_node = current_node.get_next()
            if not current_node.get_next():
                self.append(new_value)
            else:
                new_node = Node(new_value)                
                new_node.next = current_node.get_next()
                current_node.get_next().prev = new_node
                new_node.prev = current_node
                current_node.next = new_node
                return
            
            
    def insert_before(self, node_value, new_value): #inserts before a particular specified element in the list
        if not self.exists(node_value):
            print(node_value, "not in the list.")
            return
        else:
            current_node = self.head
            if current_node.get_value() == node_value:
                self.prepend(new_value)
                return
            while current_node.get_next().get_value() != node_value:
                current_node = current_node.get_next()
            new_node = Node(new_value)                
            new_node.next = current_node.get_next()
            current_node.get_next().prev = new_node
            new_node.prev = current_node
            current_node.next = new_node
            return
        
        
    def delete_head(self): #deletes the first element of the list
        if not self.head:
            print("List is already empty.")
            return
        elif self.head and not self.head.get_next():
            self.head = None
            return
        else:
            current_node = self.head
            current_node.get_next().prev = None
            self.head = current_node.get_next()
            current_node.next = current_node.prev = None
            current_node = None
            return
        
        
    def delete_tail(self): #deletes the last element of the list
        if not self.head:
            print("List is already empty.")
            return
        elif self.head and not self.head.get_next():
            self.head = None
            return
        else:
            current_node = self.head
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.get_prev().next = None
            current_node.prev = None
            current_node = None
            return
            
        
    def delete(self, value_to_delete): #deletes any specific element from any position of the list
        if not self.exists(value_to_delete):
            print(value_to_delete, "already absent from the list.")
            return
            
        current_node = self.head
        while current_node.get_value() != value_to_delete:
            current_node = current_node.get_next()
        
        if not current_node.get_prev():
            self.delete_head()
            return
        elif not current_node.get_next():
           self.delete_tail()
           return
        else:
            current_node.get_prev().next = current_node.get_next()
            current_node.get_next().prev = current_node.get_prev()
            current_node.next = current_node.prev = None
            current_node = None
            return
        
        
    def reverse(self): #reverses the list
        if not self.head:
            print("List has nothing to reverse.")
            return
        temp_node = None
        current_node = self.head
        while current_node:
            temp_node = current_node.get_prev()
            current_node.prev = current_node.get_next()
            current_node.next = temp_node
            current_node = current_node.get_prev()
        if temp_node:
            self.head = temp_node.get_prev()
            
            
    def get_length(self): #gives the number of elements in the list
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count
    
    
    def remove_duplicates(self): #removes any duplicates if any, in the list
        if not self.head or not self.head.get_next():
            print("List has no duplicates to remove")
            return
        current_node = self.head.get_next()
        previous_node = self.head
        
        keys = set([previous_node.get_value()])
        while current_node:
            if current_node.get_value() in keys:
                previous_node.next = current_node.get_next()
                if current_node.get_next():
                    current_node.get_next().prev = previous_node 
                current_node = current_node.get_next()
            else:
                keys.add(current_node.get_value())
                previous_node = current_node
                current_node = previous_node.get_next()

    
    def print_list(self): #prints out the elements of the list
        current_node = self.head
        print('-' * 12)
        print("LINKED LIST")
        print('-' * 12)
        while current_node:
            print(current_node.get_value())
            current_node = current_node.get_next()
        
            
            
            
            
d = DoublyLinkedList()

d.prepend(-1)
d.prepend(-2)
d.prepend(0)
d.append(4)
d.prepend(-1)
d.prepend(-2)
d.prepend(-1)
d.prepend(-2)
d.prepend(-3)
d.append(5)
d.prepend(-1)
d.prepend(-2)

print("Length is:", d.get_length())

d.insert_after(-1, 77)
d.insert_before(1, 99)

d.delete_head()
d.delete_head()
d.delete_tail()
d.delete_tail()

d.delete(5)
d.delete(2)

d.print_list()
    
d.reverse()
d.print_list()

d.remove_duplicates()
d.print_list()
