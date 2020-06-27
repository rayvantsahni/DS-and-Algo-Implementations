# Node class:
class Node:
  def __init__(self, value, next_node = None):
    self.next_node = next_node
    self.value = value

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

  def __repr__(self):
    return "This node contains the value " + str(self.value)

node1 = Node(44)
print(node1)

node2 = Node(6)
print(node2)

node3 = Node("hello")
print(node3)
