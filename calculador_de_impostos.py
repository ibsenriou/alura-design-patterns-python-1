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

    calculador = CalculadorDeImpostos()
    print('ISS e ICMS')

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ISS com ICMS')

    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print('ICPP e ICKV')

    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print('ICPP com ICKV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
