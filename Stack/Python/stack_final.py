class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
class Stack:
    def __init__(self, limit = 1000, top_item = None):
        self.top_item = Node(top_item)
        self.size = 1
        self.limit = limit
        
        if self.top_item == None:
            self.size = 0
        
    def has_space(self):
        return self.limit > self.size
    
    def is_empty(self):
        return self.size == 0
        
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        return "Nothing"

    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            new_item.next_node = self.top_item
            self.top_item = new_item
            self.size += 1
            print("Adding ", value, " to the Stack", sep = "")
        else:
            print("No space left :(")
        
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Popping ", item_to_remove.get_value(), " from the Stack", sep = "")
            return item_to_remove.get_value()
        print("Nothing to pop here")
        
stack1 = Stack(10, 0)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.push(7)
stack1.push(8)

print("Peeked and saw:", stack1.peek())

stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()

print("Peeked and saw:", stack1.peek())

stack1.pop()
stack1.pop()

print("Peeked and saw:", stack1.peek())

stack1.pop()

print("Peeked and saw:", stack1.peek())

stack1.pop()
stack1.pop()

print("Peeked and saw:", stack1.peek())
