"""
Динамическое программирование задачи для нескольких стеллажей и категорий.
"""
from Item import Item
from Rack import Rack
from Cell import Cell
import time
from random_func import rnd


def preparation(lst_item1, pack_volume1):
    """
    Подготовка двумерного массива и списка товаров.
    :param lst_item1: Список товаров.
    :param pack_volume1: Размер занимаемого объема.
    :return: Обработанный список товаров и двумерный массив.
    """
    for index in lst_item1:
        index.term = 15 - index.term

    table1 = []
    for index in range(len(lst_item1)):
        table1.append([])
        for jindex in range(pack_volume1):
            table1[index].append(None)
    return lst_item1, table1


def fill_cell(i, j, lst1, lst_item1):
    """
    Заполнение клетки
    :param i: Строка
    :param j: Столбец
    :param lst1: Двумерный массив, заполненный None
    :param lst_item1: Список всех товаров
    :return: Информация о ячейке
    """

    if lst_item1[i].volume-1 <= j:
        res1 = Cell()
        res2 = Cell()
        lst_test = []
        if lst1[i-1][j] is not None:
            res1.lst += lst1[i - 1][j].lst
        else:
            res1.lst = []
        if lst1[i-1][j-lst_item1[i].volume] is None or i-1 < 0 or j-lst_item1[i].volume < 0:
            addition = 0
            lst_test.append(lst_item1[i])
        else:
            addition = lst1[i-1][j-lst_item1[i].volume].crc
            lst_test += lst1[i-1][j-lst_item1[i].volume].lst
        res2.crc = lst_item1[i].term + addition
        res2.lst += lst_test
        res2.lst.append(lst_item1[i])
        res2.lst = list(set(res2.lst))
        if res1.crc > res2.crc:
            return res1
        else:
            return res2
        if res1.crc == res2.crc:
            if len(res1.lst) > len(res2.lst):
                return res1
            else:
                return res2
    else:
        res3 = Cell()
        if lst1[i-1][j] is not None:
            res3.lst += lst1[i - 1][j].lst
            return res3
        else:
            return None


def fill(table1, lst_item):
    """
    Заполнение ячеек таблицы.
    :param table1: Таблица заполненная None.
    :return: Готовая таблица.
    """
    for index in range(len(table1)):
        for jindex in range(len(table1[index])):
            table1[index][jindex] = fill_cell(index, jindex, table1, lst_item)
    return table1


def output_table(table1):
    """
    Вывод заполненной таблицы.
    :param table1: Заполненный двумерный массив(таблица)
    :return:
    """
    for index in table1:
        for jindex in index:
            print("{:<25}".format(str(jindex)), end=' ')
        print()


def postprocessing(table1, lst_item, pack_volume):
    """
    Вывод итоговой ячейки, и уменеьшенный список товаров.
    :param table1: Двумерный массив.
    :param lst_item: список всех товаров
    :return:
    """
    cell = table1[len(table1) - 1][pack_volume - 1]
    for i in cell.lst:
        i.term = 15 - i.term
        lst_item.remove(i)
    for i in lst_item:
        i.term = 15 - i.term
    return cell, lst_item


def create_dict(item_list):
    item_dict = {}
    for item in item_list:
        if item.category in item_dict:
            item_dict[item.category].append(item)
        else:
            item_dict[item.category] = [item]
    # for k, v in item_dict.items():
    #     print("{0}: {1}".format(k, ", ".join(str(item) for item in v)))
    return item_dict


start_time = time.time()
rack_lst, lst_item = rnd()
print(len(lst_item))
item_dict = create_dict(lst_item)
result_rack_list = []
for rack in rack_lst:
    for key, value in item_dict.items():
        if (rack.category == key or rack.category is None) and len(value) > 0:
            value, table = preparation(value, rack.volume)
            table = fill(table, value)
            result_cell, value = postprocessing(table, value, rack.volume)
            rack.put_lst(result_cell.lst)
            result_rack_list.append(rack)

print()
for k, v in item_dict.items():
    print("{0}: {1}".format(k, ", ".join(str(item) for item in v)))
print()

chislo = 0
for rack in result_rack_list:
    chislo += len(rack.lst)
    print(str(rack))
print(chislo)
end_time = time.time()
print(end_time-start_time)