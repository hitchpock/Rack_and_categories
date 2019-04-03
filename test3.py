from TreeRack import Node
from Item import Item
import copy

item1 = Item("Овощи", 1, 1)
item2 = Item("qwert", 2, 2)
node1 = Node(item1)
node2 = Node(item2)
node1.child = node2
node2.child = Node(Item("123", 3, 3))
node3 = node1
print(node1)
print(node3)