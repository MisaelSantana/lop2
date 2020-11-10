class Arquivo:
    def abre_arquivo(self, nome, modo):
        self.arquivo_leitura = open(nome, modo)

    def mostrar_linhas(self):
        for linha in self.arquivo_leitura:
            print(linha)

    def fecha_arquivo(self):
        self.arquivo_leitura.close()

    def contar_setosa(self):
        find_setosa = self.arquivo_leitura.find('Iris-setosa')
        qtd_setosa = 0
        if(find_setosa >= 1):
            qtd_setosa += 1
            
    def contar_versicolor(self):
        find_versicolor = self.arquivo_leitura.find('Iris-versicolor')
        qtd_versicolor = 0
        if(find_versicolor >= 1):
            qtd_versicolor += 1

    def contar_virginica(self):
        find_virginica = self.arquivo_leitura.find('Iris-virginica')
        qtd_virginica = 0
        if(find_virginica >= 1):
            qtd_virginica += 1

    def abrir_saida(self, nome, mode):
        self.arquivo_escrita = open(nome, mode)

    def escrever_saida(self):
        for linha in self.arquivo_leitura:
            self.arquivo_escrita.writelines()

    def fechar_saida(self):
        self.arquivo_escrita.close()

##################################################
teste = Arquivo()
teste.abre_arquivo('iris.data', 'rt')
teste.mostrar_linhas()
teste.contar_setosa()
teste.contar_versicolor()
teste.contar_virginica()
teste.fecha_arquivo()
