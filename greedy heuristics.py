"""
Жадные эвристики.
"""
from random_func import rnd


def output(dct):
    """
    Вывод словаря.
    :param dct:Словарь.
    :return:
    """
    print()
    for k in sorted(dct.keys()):
        print("{0}: {1}".format(k, ", ".join(str(item) for item in dct[k])))
    print()


def check(item_dict, rack_list):
    """
    Проверка заполненности склада и стеллажей.
    :param item_dict:
    :param rack_list:
    :return:
    """
    item_bool = True
    rack_bool = True
    for k in item_dict.keys():
        if len(item_dict[k]) > 0:
            item_bool = False
    for rack in rack_list:
        if rack.category is None:
            rack_bool = False
    return item_bool, rack_bool


def create_dict(item_list):
    """
    Создание словаря товаров по сроку хранения.
    :param item_list: Список товаров.
    :return: Словарь.
    """
    item_dict = {}
    for item in item_list:
        if item.term in item_dict:
            item_dict[item.term].append(item)
        else:
            item_dict[item.term] = [item]
    return item_dict


def sort(rack_list, item_dict):
    item_bool, rack_bool = check(item_dict, rack_list)
    while item_bool is False and rack_bool is False:
        item_bool, rack_bool = check(item_dict, rack_list)
        output(item_dict)
        for k in sorted(item_dict.keys()):
            if item_dict[k] is not None:
                item_dict[k] = sorted(item_dict[k], key=lambda x: x.volume, reverse=True)
                for item in item_dict[k]:
                    for rack in rack_list:
                        if rack.volume > item.volume and (item.category == rack.category or rack.category is None):
                            rack.put(item)
                            item_dict[k].remove(item)
                            break
    return rack_list, item_dict


rack_list, item_list = rnd()
item_dict = create_dict(item_list)
output(item_dict)

rack_list, item_dict = sort(rack_list, item_dict)
# output(item_dict)

for rack in rack_list:
    #if rack.category is not None:
        print(rack)
