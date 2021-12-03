class Orcamento(object):

    def __init__(self):
        self.__items = []

    @property
    def valor(self):
        total = 0.0
        for item in self.__items:
            total += item.valor
        return total

    def obter_items(self):
        return tuple(self.__items)

    @property
    def total_items(self):
        return len(self.__items)

    def adiciona_item(self, item):
        self.__items.append(item)


class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


