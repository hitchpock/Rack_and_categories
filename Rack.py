"""
Rack module.
Класс стелажа.
"""


class Rack:
    def __init__(self, volume, category=None):
        """
        :param self.category: Категория товаров на стелаже.
        :param self.volume: Объем стелажа.
        :param self.lst: Список товаров стелажа.
        """
        self.category = category
        self.lst = []
        self.volume_start = volume
        self.volume = volume

    def put(self, item):
        """
        Метод добавления товара на стелаж.
        :param item: Товар.
        :return:
        """
        self.lst.append(item)
        self.volume -= item.volume
        if self.category is None:
            self.category = item.category

    def put_lst(self, lst):
        for i in lst:
            self.put(i)

    def take(self, item):
        """
        Метод взятия со стелажа.
        :param item: Товар.
        :return: Товар.
        """
        self.lst.remove(item)
        self.volume += item.volume
        return item

    def __str__(self):
        # return "Rack: {0}, {1}, {2}".format(self.category, self.volume, self.lst)
        return "Rack: cat({0}), st_vol({1}), vol({2}), len({3}), lst({4})".format(self.category, self.volume_start,
                                                                                self.volume, len(self.lst),
                                                                     ", ".join(str(item) for item in self.lst))
