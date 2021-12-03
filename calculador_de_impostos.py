class CalculadorDeImpostos(object):

    @staticmethod
    def realiza_calculo(orcamento, imposto):

        valor = imposto.calcula(orcamento)
        print(valor)


if __name__ == '__main__':

    from orcamento import Orcamento
    from impostos import ISS, ICMS

    orcamento = Orcamento(500)

    calculador_de_impostos = CalculadorDeImpostos()

    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
