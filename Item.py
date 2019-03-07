"""
Item module.
Класс товара.
"""


class Item:
    def __init__(self, category, volume, term):
        """
        :param self.category: Категория товара.
        :param self.volume: Занимаемый объем.
        :param self.term: Срок хранения.
        """
        self.category = category
        self.volume = volume
        self.term = term

    def __str__(self):
        # return "({0}, {1}, {2})".format(self.category, self.volume, self.term)
        return "Item: cat({0}), vol({1}), term({2})".format(self.category, self.volume, self.term)
