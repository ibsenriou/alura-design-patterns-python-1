from datetime import date

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class NotaFiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':

    from criador_de_nota_fiscal import CriadorDeNotaFiscal

    itens = [
        Item(
            'ITEM A',
            100
        )
    ]

    nota_fiscal = NotaFiscal(
        'FHSA Limitada',
        '01234556681234',
        itens,
        date.today(),
        ''
    )

    nota_fiscal_com_construtor = CriadorDeNotaFiscal()\
        .com_razao_social('FHSA LIMITADA')\
        .com_cnpj('0123923716238')\
        .com_itens(itens)

    nota_fiscal_com_construtor2 = CriadorDeNotaFiscal()\
        .com_cnpj('219831293789')\
        .com_razao_social('XABLAU CORP')\
        .com_itens(itens)
