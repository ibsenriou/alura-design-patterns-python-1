class CalculadorDeImpostos(object):

    @staticmethod
    def realiza_calculo(orcamento, imposto):

        valor = imposto.calcula(orcamento)
        print(valor)


if __name__ == '__main__':

    from orcamento import Orcamento, Item
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador_de_impostos = CalculadorDeImpostos()
    print('ISS e ICMS')

    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    print('ICPP e ICKV')

    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())
