"""Модуль времени и объема. Подумай!"""

import copy
import math
from TreeRack import rnd, TreeRack, Node
from Item import Item


def check(lst, volume):
    for item in lst:
        if item.volume <= volume:
            return True
    return False


def list_remove(lst, node):
    lst1 = []
    print()
    while node is not None:
        print(type(node))
        lst1.append(node.value)
        node = node.child
    for i in lst1:
        lst.remove(i)
    return lst


def calc(node):
    if node.child is not None:
        res = node.value.term - node.child.value.term
        return math.fabs(res)
    else:
        print("Child = None")
        return 0


def search_child(item_list, par_node, rack):
    if check(item_list, rack.volume) is True:
        test_node = copy.copy(par_node)
        par_node.child = Node(Item(None, 100, 100))
        for item in item_list:
            test_node.child = Node(item)
            if calc(test_node) < calc(par_node) and item.volume <= rack.volume and (item.category == rack.category or rack.category is None):
                par_node.child = test_node.child
        if par_node.child.value.category is None:
            return None
        print(type(par_node), type(par_node.child))
        rack.put(par_node)
        item_list.remove(par_node.child.value)
        if rack.volume > 0:
            n = copy.copy(rack)
            par_node.child.child = search_child(item_list, par_node.child, n)
        return rack
    else:
        return None


def sort(item_list, rack_lst):
    for rack in rack_lst:
        item = best_item(item_list)
        if item is not None:
            print("Best item = ", item)
            rack.category = item.category
            rack.value = Node(item)
            rack.volume -= item.volume
            n = copy.copy(rack)
            rack.value.child = search_child(item_list, Node(item), n)
            list_remove(item_list, rack.value)
    return item_list, rack_lst


def best_item(item_list):
    if len(item_list) > 0:
        res = item_list[0]
        for item in item_list:
            if item.term < res.term:
                res = item
        return res
    else:
        return None


rack_list, item_list = rnd()
print(len(item_list))

for item in item_list:
    print(item)
for r in rack_list:
    print("Rack volume = ", r.volume)
print()

item_list, rack_list = sort(item_list, rack_list)

for rack in rack_list:
    print("Rack: cat({0}), st_vol({1}), lst(".format(rack.category, rack.volume_start), end='')
    print(rack)
    print()
# for item in item_list:
#     print(item)
