"""
Класс ячейки таблицы.
"""


class Cell:
    def __init__(self):
        self.lst = []

        def calc(lst1):
            result = 0
            for item in lst1:
                result += item.term
            return result

        self.crc = calc(self.lst)

    def __str__(self):
        return "{0:<4}:[{1}]".format(self.crc,
                                     ", ".join(str(item) for item in self.lst))
