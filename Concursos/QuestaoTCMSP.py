class FonteDeDados:
    def __init__(self, endereco):
        raise NotImplementedError()

    def proximoDado():
        raise NotImplementedError()

    def possuiDados():
        raise NotImplementedError()


class FonteArquivo(FonteDeDados):
    def __init__(self, endereco):
        self.__arquivo = open(endereco, 'r')
        self.__linhas = self.__arquivo.readlines()
        self.__linha_atual = 0

    def proximoDado(self):
        retorno = None
        if(not self.__arquivo.closed):
            self.__linha_atual += 1
            retorno = self.__linhas[self.__linha_atual]
        return retorno
        
    def possuiDados(self):
        linhasRestantes = len(self.__linhas) - self.__linha_atual
        return linhasRestantes > 0


if(__name__ == '__main__'):
    fa = FonteArquivo('/tmp/lista.txt')
    fa.possuiDados()
    fa.proximoDado()

    fa.possuiDados()
    fa.proximoDado()
    
    fa.possuiDados()
    fa.proximoDado()

    fa.possuiDados()
    fa.proximoDado()