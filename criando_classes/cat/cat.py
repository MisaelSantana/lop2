# exercise cat

class cat:
    cor_do_pelo = ''
    rabo = ''
    patas = 4
    cor_dos_olhos = ''
    raca = ''

    def __init__(self, patas, nome):
        self.patas = patas
        self.nome = nome

    def miar(self, som="Miau"):
        print(som)
    
    def agachar(self):
        print(self.nome +'agachar com as patas' + self.patas)