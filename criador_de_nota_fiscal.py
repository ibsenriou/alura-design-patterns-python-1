from nota_fiscal import NotaFiscal, Item


class CriadorDeNotaFiscal(object):
    def __init__(self):

        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def constroi(self):
        if self.__razao_social is None:
            raise Exception('Razão Social deve ser preenchida')

        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')

        if self.__itens is None:
            raise Exception('Itens deve ser preenchido')

        return NotaFiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            data_de_emissao=self.__data_de_emissao,
            detalhes=self.__detalhes
        )

