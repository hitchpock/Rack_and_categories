from Item import Item
from Rack import Rack
import random


def rnd():
    """
        Функция задающая случайные стеллаж и список товаров
        :return: Возвращает стеллаж и список товаров
    """
    rack_lst = []
    categories = ["Овощи", "Фрукты", "Бакалея"]
    for _ in range(random.randint(20, 300)):
        rack = Rack(random.randint(10, 20))
        rack_lst.append(rack)
    item_lst = []
    for _ in range(random.randint(500, 1000)):
        item = Item(random.choice(categories), random.randint(1, 7),
                    random.randint(1, 14))
        item_lst.append(item)
        # print(str(item))
    return rack_lst, item_lst
