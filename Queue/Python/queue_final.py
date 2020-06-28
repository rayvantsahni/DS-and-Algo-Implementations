# node class
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
# queue class
class Queue:
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
        
    # peeks and returns the top most item of the queue
    def peek(self):
        if self.is_empty():
            return "Nobody in line right now!"
        return self.head.get_value()
    
    # gives the current size of the queue
    def get_size(self):
        return self.size
    
    # checks if the queue has any space left
    def has_space(self):
        if self.max_size == None:
            return True
        return self.max_size > self.get_size()
    
    # checks if the queue is empty
    def is_empty(self):
        return self.size == 0
    
    # adds an item to the end of the queue
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding ", item_to_add.get_value(), " to the queue.", sep = "")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.next_node = item_to_add
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry! No more room :(")
        
    # removes an item from the starting of the queue
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Serving ", item_to_remove.get_value(), sep = "")
            
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("No more orders left to serve...")
        
print("Taking upto 10 orders.\n------------")
deli_line = Queue(10)
print("Accepting orders now.. \n------------")
deli_line.enqueue("boiled eggs")
deli_line.enqueue("bacon")
deli_line.enqueue("rice")
deli_line.enqueue("bread")
deli_line.enqueue("fries")
deli_line.enqueue("pizza")
deli_line.enqueue("burger")
deli_line.enqueue("milkshake")
deli_line.enqueue("noodles")
deli_line.enqueue("omelet")
deli_line.enqueue("sushi")

print("------------\n\nFirst order in the queue is:", deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
