"""
Динамическое программирование для одного стеллажа и одной категории.
"""

import random
from Item import Item
from Rack import Rack
from Cell import Cell
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


def output_table(table1, pack_volume):
    """
    Вывод заполненной таблицы.
    :param table1: Заполненный двумерный массив(таблица)
    :return:
    """
    for index in table1:
        for jindex in index:
            print("{:<25}".format(str(jindex)), end=' ')
        print()
    # return table1[len(table1) - 1][pack_volume - 1]


def postprocessing(table1, lst_item, pack_volume):
    """
    Вывод итоговой ячейки, и уменеьшенный список товаров.
    :param cell: Ячейка.
    :param lst_item: списо всех товаров
    :return:
    """
    cell = table1[len(table1) - 1][pack_volume - 1]
    for i in cell.lst:
        i.term = 15 - i.term
        lst_item.remove(i)
        print("{0}: {1}".format(i, i.term))
    print("1234")
    for i in lst_item:
        i.term = 15 - i.term
        print(str(i))
    return cell, lst_item


rack_lst, lst_item = rnd()
rack = rack_lst[0]
print(rack.volume)
lst_item, table = preparation(lst_item, rack.volume)
table = fill(table, lst_item)
result_cell, lst_item = postprocessing(table, lst_item, rack.volume)

rack.put_lst(result_cell.lst)
print(str(rack))
