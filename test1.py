import random


class Item:
    def __init__(self, name, volume, date):
        self.name = name
        self.volume = volume
        self.date = date

    def __str__(self):
        return self.name


class Cell:
    def __init__(self):
        self.lst = []

        def calc(lst1):
            result = 0
            for item in lst1:
                result += item.date
            return result

        self.crc = calc(self.lst)

    def __str__(self):
        return "{0:<4}: [{1}]".format(self.crc, ", ".join(str(item) for item in self.lst))


def preparation(lst_item1, pack_volume1):
    """
    Подготовка двумерного массива и списка товаров.
    :param lst_item1: Список товаров.
    :param pack_volume1: Размер занимаемого объема.
    :return: Обработанный список товаров и двумерный массив.
    """
    for index in lst_item1:
        index.date = 15 - index.date

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
        res2.crc = lst_item1[i].date + addition
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
            res3.lst.append(*lst1[i - 1][j].lst)
            return res3
        else:
            return None


def fill(table1):
    """
    Заполнение ячеек таблицы.
    :param table1: Таблица заполненная None.
    :return: Готовая таблица.
    """
    for index in range(len(table1)):
        for jindex in range(len(table1[index])):
            table1[index][jindex] = fill_cell(index, jindex, table1, lst_item)
    return table1


def output(table1):
    """
    Вывод заполненной таблицы
    :param table1: Заполненный двумерный массив(таблица)
    :return:
    """
    for index in table1:
        for jindex in index:
            print("{:<25}".format(str(jindex)), end=' ')
        print()
    return table1[len(table) - 1][pack_volume - 1]


def postprocessing(cell):
    """
    Вывод итоговой ячейки.
    :param cell: Ячейка.
    :return:
    """
    for i in cell.lst:
        i.date = 15 - i.date
        print("{0}: {1}".format(i, i.date))
    return cell


gitar = Item('Гитара', 1, 1.5)
pleer = Item('Магнитофон', 4, 3)
notebook = Item('Ноутбук', 3, 2)
lst_item = [pleer, gitar, notebook]
pack_volume = 4


lst_item, table = preparation(lst_item, pack_volume)
table = fill(table)

result_table = output(table)
result_cell = postprocessing(result_table)
