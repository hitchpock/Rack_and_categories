import copy
import math

class Node:
    def __init__(self,  value):
        self.value = value
        self.child = None


    def __str__(self):
        if self.child is not None:
            return "{0} --> {1}".format(self.value, str(self.child))
        else:
            return "{0}".format(self.value)


class Rack:
    def __init__(self, volume):
        self.volume = volume
        self.value = None
    
    def __str__(self):
        return "Объем: {0}; {1}".format(self.volume, str(self.value))
        

def check(lst, volume):
    for i in lst:
        if i[0] <= volume:
            return True
    return False


def calc(tree):
    if tree.child is not None:
        res = tree.value[1] - tree.child.value[1]
        return math.fabs(res)
    else:
        print("Child = None")
        return 0


def search_child(lst, par_node, rack):
    if check(lst, rack.volume) is True:
        test_node = copy.copy(par_node)
        child = Node(lst[0])
        par_node.child = child
        for item in lst:
            test_node.child = Node(item)
            if calc(test_node) < calc(par_node) and test_node.child.value[0] < rack.volume:
                par_node.child = test_node.child
        print("{0} --> {1}".format(par_node.value, par_node.child.value))
        rack.volume -= par_node.child.value[0]
        lst.remove(par_node.child.value)
        if rack.volume > 0:
            node = copy.copy(par_node.child)
            par_node.child.child = search_child(lst, node, rack)
        if rack.volume < 0:
            return None
        else:
            return par_node.child
    else:
        return None
            

        
        

# tpl = (volume, time)
tpl_list = [(4, 5), (1, 3), (3, 2), (2, 5), (3, 4)]
rack = Rack(8)
result = Node((100, 100))
for i in tpl_list:
    test_node = Node(i)
    if test_node.value[1] <= result.value[1]:
        result = test_node
#print(calc(result))
rack.value = result
rack.volume -= result.value[0]
tpl_list.remove(result.value)
result.child = search_child(tpl_list, result, rack)
print(rack)
