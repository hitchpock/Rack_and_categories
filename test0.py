class Item:
    def __init__(self, name, volume, price):
        self.name = name
        self.volume = volume
        self.price = price


class Cell:
    def __init__(self):
        self.crc = None
        self.lst = []

    def __str__(self):
        return "{0}: {1}".format(self.crc, self.lst)


gitar = Item('Гитара', 1, 1.5)
pleer = Item('Магнитофон', 4, 3)
notebook = Item('Ноутбук', 3, 2)
lst_item = [pleer, gitar, notebook]
pack_volume = 4

for i in lst_item:
    i.price = 15 - i.price

lst = []
for i in range(len(lst_item)):
    lst.append([])
    for j in range(pack_volume):
        lst[i].append(None)

for i, v in enumerate(lst_item):
    # print("{:<11}".format(v.name), ', '.join(str(item) for item in lst[i]))
    pass

for i in lst:
    for j in i:
        print(j, end=' ')
    print()

print(max(0 if lst[-1][-1] is None else lst[-1][-1], 1500))


def zapolnenie(i, j, lst1, lst_item1):
    """
    Заполнение клетки
    :param i: Строка
    :param j: Столбец
    :param lst1: Двумерный массив
    :return: Информация о ячейке
    """
    # if lst_item1[i].volume-1 <= j:
    #     res1 = 0 if lst1[i-1][j] is None else lst1[i-1][j]
    #     res2 = lst_item1[i].price + (0 if (lst1[i-1][j-lst_item1[i].volume] is None or i-1 < 0
    #                                        or j-lst_item1[i].volume < 0) else lst1[i-1][j-lst_item1[i].volume])
    #     return max(res1, res2)
    # else:
    #     return lst1[i-1][j]

    if lst_item1[i].volume-1 <= j:
        res1 = Cell()
        res2 = Cell()
        lst_test = []
        if lst1[i-1][j] is not None:
            res1.crc = lst1[i - 1][j].crc
            res1.lst += lst1[i - 1][j].lst
        else:
            res1.crc = 0
            res1.lst = []
        if lst1[i-1][j-lst_item1[i].volume] is None or i-1 < 0 or j-lst_item1[i].volume < 0:
            addition = 0
            lst_test.append(lst_item1[i].name)
        else:
            addition = lst1[i-1][j-lst_item1[i].volume].crc
            lst_test += lst1[i-1][j-lst_item1[i].volume].lst
        res2.crc = lst_item1[i].price + addition
        res2.lst += lst_test
        res2.lst.append(lst_item1[i].name)
        res2.lst = list(set(res2.lst))
        if res1.crc > res2.crc:
            return res1
        else:
            return res2
    else:
        res3 = Cell()
        if lst1[i-1][j] is not None:
            res3.crc = lst1[i-1][j].crc
            res3.lst.append(*lst1[i-1][j].lst)
            return res3
        else:
            return None


for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = zapolnenie(i, j, lst, lst_item)
        print(lst[i][j], end=' ')
    print()

print(lst[2][3])
