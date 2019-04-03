"""Вроде как правильный метод ветвей и границ"""
import copy
from TreeRack import Node, TreeRack, rnd
from Item import Item


def best_item(lst):
    if len(lst) > 0:
        res = lst[0]
        for item in lst:
            if item.term < res.term:
                res = item
        return res
    else:
        return None


def check(volume, lst):
    for item in lst:
        if item.volume <= volume:
            return True
    return False


def calc(node):
    return (node.value.term + node.child.value.term)


def search_child(node, volume, lst):
    if check(volume, lst) is True:
        res_node = copy.copy(node)
        node.child = Node(Item(None, 100, 100))
        for item in lst:
            res_node.child = Node(item)
            if calc(res_node) < calc(node) and (res_node.child.value.category == res_node.value.category) and (res_node.child.value.volume <= volume):
                node.child = res_node.child
        if node.child.value.category is None:
            return None
        volume -= node.child.value.volume
        lst.remove(node.child.value)
        if volume > 0:
            node.child.child = search_child(node.child, volume, lst)
        return node.child
    else:
        return None
        

rack_list, item_list = rnd()
print(len(item_list))
for item in item_list:
    print(item)
for rack in rack_list:
    print(rack)

for rack in rack_list:
    item = best_item(item_list)
    if item is not None:
        node = Node(item)
        rack.put(node)
        item_list.remove(node.value)
        node.child = search_child(node, rack.volume, item_list)

for rack in rack_list:
    print(rack)
    print()

