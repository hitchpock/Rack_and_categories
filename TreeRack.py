from Item import Item
import random

class TreeRack:
    def __init__(self, volume):
        self.category = None
        self.volume_start = volume
        self.volume = volume
        self.value = None

    
    def put(self, node):
        self.value = node
        self.category = node.value.category
        self.volume -= node.value.volume

    
    def calc_volume(self):
        node = self.value
        volume = 0
        while node is not None:
            volume += node.value.volume
            node = node.child
        return volume


    def __str__(self):
        if self.value is not None:
            #return "Rack: cat({0}), st_vol({1}), vol({2}), lst({3} --> {4})\n".format(self.category, self.volume_start,
                                                                                #self.volume, str(self.value), str(self.child))
            return "Rack vol = {0} - {2} :: {1}".format(self.volume_start, self.value, self.calc_volume())
            #return "{0} --> {1}".format(self.value.term, self.child)
        else:
            return "Rack vol = {0} :: None".format(self.volume_start)


class Node:
    def __init__(self,  value):
        self.value = value
        self.child = None


    def __str__(self):
        if self.value is not None and self.child is not None:
            return "{0} --> {1}".format(str(self.value), str(self.child))
        else:
            return "{0}".format(str(self.value))


def rnd():
    """
        Функция задающая случайные стеллаж и список товаров
        :return: Возвращает стеллаж и список товаров
    """
    rack_lst = []
    categories = ["Овощи", "Фрукты", "Бакалея"]
    for _ in range(random.randint(10, 12)):
        rack = TreeRack(random.randint(10, 20))
        rack_lst.append(rack)
    item_lst = []
    for _ in range(random.randint(20, 40)):
        item = Item(random.choice(categories), random.randint(1, 7), random.randint(1, 14))
        item_lst.append(item)
        # print(str(item))
    return rack_lst, item_lst
