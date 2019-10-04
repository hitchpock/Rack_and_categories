"""
Правильные жадные эвристики.
"""

import time
from random_func import rnd


def output(item_lst, rack_lst):
    print("Товары")
    if item_lst is not None:
        for i in item_lst:
            print(i)
    print("Стеллажи")
    if rack_lst is not None:
        for r in rack_lst:
            print(r)
    print()


def preparation(lst):
    lst = sorted(lst, key=lambda x: x.term/x.volume, reverse=False)
    return lst


def check(item_lst, rack_lst):
    """
    Проверка заполненности склада и стеллажей.
    :param item_dict:
    :param rack_list:
    :return:
    """
    item_bool = True
    rack_bool = True
    if len(item_lst) > 0:
        item_bool = False
    for rack in rack_lst:
        if rack.category is None:
            rack_bool = False
    return item_bool, rack_bool
    

def sort(item_lst, rack_lst):
    item_bool, rack_bool = check(item_lst, rack_lst)
    while item_bool is False and rack_bool is False:
        item_bool, rack_bool = check(item_lst, rack_lst)
        output(item_lst, rack_lst)
        for item in item_lst:
            for rack in rack_lst:
                if rack.volume > item.volume and (rack.category == item.category or rack.category is None):
                    rack.put(item)
                    item_lst.remove(item)
                    break

start_time = time.time()
rack_list, item_list = rnd()
print(len(item_list))
item_list = preparation(item_list)
for i in item_list:
    print("{0}: {1}".format(i, i.term/i.volume))

sort(item_list, rack_list)
output(item_list, rack_list)
chislo = 0
for rack in rack_list:
    chislo += len(rack.lst)
print(chislo)
end_time = time.time()
print(end_time-start_time)
