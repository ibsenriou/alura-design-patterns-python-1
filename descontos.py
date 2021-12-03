class DescontoPorCincoItems(object):

    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto

    def calcular(self, orcamento):
        if orcamento.total_items > 5:
            return orcamento.valor * 0.1
        else:
            return self._proximo_desconto.calcular(orcamento)


class DescontoPorMaisDeQuinhentosReais(object):

    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto

    def calcular(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self._proximo_desconto.calcular(orcamento)


class SemDesconto(object):

    def calcula(self, orcamento):
        return 0

