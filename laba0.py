from Item import Item
from Rack import Rack
import random
from itertools import combinations


def comb(lst_items, res, list_of_tuples):
    """
    Ищет комбинацию для заполнения стеллаже минимальным числом товаров
    :param lst_items: Список товаров
    :param res: Необходимый объем
    :return: Готовая комбинация товаров
    """
    lst_1 = []
    lst = []
    lst_res = []
    for item in lst_items:
        lst.append(item.volume)
    for index in range(0, len(lst) + 1):
        for i in list(combinations(lst, index)):
            if sum(i) == res:
                lst_1.append(i)
    if len(lst_1) > 0:
        tuple_res = min(lst_1, key=len)
        print(tuple_res)
        count = 0
        for index in tuple_res:
            for item in list_of_tuples:
                for i in item[1]:
                    if index == i.volume:
                        lst_res.append(i)
                        break
        return lst_res
    else:
        return None


# def rnd():
#     """
#     Функция задающая случайные стеллаж и список товаров
#     :return: Возвращает стеллаж и список товаров
#     """
#     rack = Rack(random.randint(7, 18))
#     print(rack.volume)
#     lst = []
#     for _ in range(random.randint(10, 20)):
#         item = Item('Овощи', random.randint(1, 5), random.randint(1, 14))
#         lst.append(item)
#     return rack, lst


def create_list_of_tuples(lst):
    """
    Сортирует список товаров и возвращает кортеж
    :param lst:
    :return:
    """
    dct = {}
    for item in lst:
        if item.term in dct:
            dct[item.term].append(item)
        else:
            dct[item.term] = [item]

    tuples_list = []
    for k in sorted(dct.keys()):
        for _ in dct[k]:
            dct[k] = sorted(dct[k], key=lambda item: item.volume)
        n = (k, dct[k])
        tuples_list.append(n)

    for i in tuples_list:
        print(i[0], " : ", ", ".join(str(item) for item in i[1]))

    return tuples_list


def search(lst, rack):
    """
    Ищет комбинацию, заполняющую стеллаж товарами
    :param lst: Список отсортированных товаров
    :param rack: Пустой стеллаж
    :return: Заполненный стеллаж
    """
    lst_times = []
    for plane in lst:
        for elem in plane[1]:
            lst_times.append(elem)
            res = comb(lst_times, rack.volume, lst)
            if res is not None:
                print("Стеллаж заполнен")
                for item in res:
                    rack.put(item)
                return res, rack


# lst_category = ['Овощи', 'Фрукты', 'Бакалея']
# # Список стеллажей
# lst_rack = []
# # Список товаров
# lst_item = []
# # Список укомлектованных стеллажей
# rack_ended = []
#
#
# def rnd():
#     for index in range(random.randint(4, 10)):
#         rack = Rack(random.randint(7, 18))
#         lst_rack.append(rack)
#     print(len(lst_rack))
#
#     for index in range(random.randint(20, 30)):
#         item = Item(random.choice(lst_category), random.randint(1, 5), random.randint(1, 14))
#         lst_item.append(item)
#     print(len(lst_item))
#
#
# def output():
#     for index in range(len(lst_rack)):
#         print(lst_rack[index])
#     print(len(lst_rack))
#
#     for index in range(len(lst_item)):
#         print(lst_item[index])
#     print(len(lst_item))
#     print('\n')
#
#     if len(rack_ended) > 0:
#         for index in range(len(rack_ended)):
#             print(rack_ended[index])
#         print(len(rack_ended))
#
#
# def occupancy(lst_items, lst_racks):
#     lst_item_sort = sorted(lst_items, key=lambda item: item.volume)
#     min_item = lst_item_sort[0].volume
#     lst_rack_sort = sorted(lst_racks, key=lambda rack: rack.volume, reverse=True)
#     max_rack = lst_rack_sort[0].volume
#     print('Минимальный товар - ' + str(min_item))
#     print('Максимальный стеллаж - ' + str(max_rack))
#     if min_item <= max_rack:
#         return True
#     else:
#         return False
#
#
# rnd()
# output()
# lst_item.sort(key=lambda items: items.term, reverse=False)
# output()
#
# while occupancy(lst_item, lst_rack) is True:
#     for item in lst_item:
#         for rack in lst_rack:
#             if (item.category == rack.category or rack.category is None) and rack.volume >= item.volume:
#                 rack.put(item)
#                 lst_item.remove(item)
#                 if rack.volume == 0:
#                     rack_ended.append(rack)
#                     lst_rack.remove(rack)
#                 break
#
# # bol = occupancy(lst_item, lst_rack)
# output()


rack, lst_item = rnd()
list_of_tuples = create_list_of_tuples(lst_item)
lst_res, rack = search(list_of_tuples, rack)
print(", ".join(str(item) for item in lst_res))
print(rack)

