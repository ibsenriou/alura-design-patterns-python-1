from descontos import DescontoPorCincoItems, DescontoPorMaisDeQuinhentosReais, SemDesconto


class CalculadorDeDescontos(object):

    def calcula(self, orcamento):

        desconto = DescontoPorCincoItems(
            DescontoPorMaisDeQuinhentosReais(
                SemDesconto()
            )
        )

        return desconto.calcular(orcamento)



if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100))
    orcamento.adiciona_item(Item('Item B', 50))
    orcamento.adiciona_item(Item('Item C', 400))

    calculador_de_descontos = CalculadorDeDescontos()

    desconto = calculador_de_descontos.calcula(orcamento)

    print(f'Desconto calculado: {desconto:.2f}')


